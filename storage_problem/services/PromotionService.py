from storage_problem.services.ServiceModels.Promotion import Promotion
from storage_problem.services import redis_session
import json

class PromotionService:
    def __init__(self):
        pass

    def get(self,id)->Promotion:

        current = redis_session.get('current')
        if current:
            raw_data = redis_session.get("__{}__{}".format(current.decode('utf-8'),id))
            if raw_data:
                raw_data = raw_data.decode('utf-8')
                raw_data = raw_data.split(',')
                promotion = Promotion(None,raw_data[0],raw_data[1],raw_data[2])
                return promotion
        return None
    
    def create(self, promotion:Promotion):
        current = redis_session.get('current')
        key = '__{}__{}'.format(current.decode('utf-8'),id)
        value = '{},{},{}'.format(promotion.expiration_date,promotion.price,promotion.expiration_date)
        redis_session.set(key, value)
        return promotion
    
    def create_multiple(self, promotions:list):
        for i in promotions:
            self.create(i)