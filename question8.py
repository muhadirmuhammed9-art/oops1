class mobile:
    def __init__(self,name,price):
        self.name = name 
        self.price = price
mobiles=[]
for i in range(5):
    name=input("enter the name: ")
    price=float(input("enter mobile price: "))
    mobiles.append(mobile(name,price))
print("mobiles above 20000: ")

for m in mobiles:
    if m.price > 20000:
        print(m.name,m.price)



    

    
        




