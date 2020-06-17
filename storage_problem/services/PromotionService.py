from storage_problem.services.ServiceModels.Promotion import Promotion
from storage_problem.services import redis_session
import json

class PromotionService:
    def __init__(self):
        pass

    def get(self,id)->Promotion:

        current = redis_session.get('current')
        print('geting data of key:__{}__{}'.format(current.decode('utf-8'),id))
        raw_data = redis_session.get("__{}__{}".format(current.decode('utf-8'),id))
        print('got raw data {}'.format(raw_data))
        if raw_data:
            raw_data = raw_data.decode('utf-8')
            raw_data = raw_data.split(',')
            promotion = Promotion(None,raw_data[0],raw_data[1],raw_data[2])
            return promotion
        else:
            return None
    
    def create(self, promotion:Promotion):
        redis_session.set(promotion.external_id, json.dumps(promotion.to_json()))
        return promotion
    
    def create_multiple(self, promotions:list):
        for i in promotions:
            self.create(i)