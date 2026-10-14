class cars:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
car1 =cars ("bmw",2014,1000000)
print("brand:",car1.brand)
print("moidel:",car1.model)
print("price:",car1.price)

car2=cars("benz",2013,2000000)
print("brand:",car2.brand)
print("model:",car2.model)
print("price:",car2.price)

car3=cars("audi",2015,3000000)
print("brand:",car3.brand)
print("model:",car3.model)
print("price:",car3.price)
