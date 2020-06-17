class Promotion:
    def __init__(self, id,  external_id, price, expiration_date):
        self.id = id
        self.external_id = external_id
        self.price = price
        self.expiration_date = expiration_date
    
    def to_json(self):
        return {
            #'id':self.id,
            'external_id':self.external_id,
            'price':self.price,
            'expiration_date': self.expiration_date#.strftime("%m/%d/%Y, %H:%M:%S")
        }

    def from_json(self, j_son):
        #self.id = j_son[id]
        self.external_id =j_son['external_id']
        self.price = j_son['price']
        self.expiration_date = j_son['expiration_date']