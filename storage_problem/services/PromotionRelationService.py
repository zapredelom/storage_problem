from storage_problem.models.crud import Session
from storage_problem.services import redis_session
from storage_problem.services.ServiceModels.Promotion import Promotion
from storage_problem.models.Promotion import PromotionEntity
import json

class PromotionRelationService:
    def __init__(self):
        pass

    def get(self,id)->Promotion:
        session = Session()
        promotionEntity = session.query(PromotionEntity).filter(PromotionEntity.external_id == id).first()
        session.close()
        if promotionEntity:
            promotion = Promotion(id = promotionEntity.id, external_id = promotionEntity.external_id, price = promotionEntity.price, expiration_date= promotionEntity.expiration_date)
            return promotion
        else:
            return None
    
    def create(self, promotion:Promotion):
        session = Session()
        promotionEntity  = PromotionEntity(external_id = promotion.external_id, price = promotion.price, expiration_date = promotion.expiration_date)
        session.add(promotionEntity)
        session.commit()
        session.close()
        #return self.session.query(Promotion).filter(PromotionEntity.external_id == promotion.external_id).first()

    
    def create_multiple(self, promotions:list):
        
        bulk = []
        for p in promotions:
            promotionEntity  = PromotionEntity(external_id = p.external_id, price = p.price, expiration_date = p.expiration_date)
            bulk.append(promotionEntity)
        session = Session()
        session.bulk_save_objects(bulk)
        session.commit()
        session.close()
