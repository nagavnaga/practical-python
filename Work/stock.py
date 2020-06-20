class Stock:
    def __init__(self,name,share,price):
        self.name = name
        self.share = share
        self.price = price

    @property
    def cost(self):
        return self.share * self.price



