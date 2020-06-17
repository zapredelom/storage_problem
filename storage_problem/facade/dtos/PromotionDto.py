class PromotionDto:
    def __init__(self, external_id, price, expiratino_date):
        self.external_id = external_id
        self.price = price
        self.expiration_date = expiratino_date
    
    def to_json(self):
        return {
            'id':self.external_id,
            'price':self.price,
            'expiration_date': self.expiration_date#.strftime("%m/%d/%Y, %H:%M:%S")
        }