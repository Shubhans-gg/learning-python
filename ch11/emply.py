class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(odr1,odr2):      #dunder fxn for greater than
        return odr1.price>odr2.price

odr1=order("Coffee",20)
odr2=order("Tea",10)
print(odr1>odr2)