from sqlalchemy import Column, Float, Float, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from storage_problem.models import Base

class PromotionEntity(Base):
    __tablename__ = 'promotion'

    id = Column(Integer, primary_key=True)
    external_id = Column(String)
    price = Column(Float)
    expiration_date = Column(DateTime)
    
    def __repr__(self):
        return  "<promotion(id='%s', external_id='%s', price='%s, expiration_Date=%s')>" % (
                             self.id, self.external_id, self.price, self.expiration_date)
    
    def to_json(self):
        return {
                'external_id': self.external_id,
                'price':self.price,
                'expiration_date':self.expiration_date}
    def from_json(self,j_son):
        #self.id = j_son[id]
        self.external_id =j_son['external_id']
        self.price = j_son['price']
        self.expiration_date = j_son['expiration_date']