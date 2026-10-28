class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        return self.price * self.quantity
    def display(self):
        print("product name:",self.name)
        print("product price:",self.price)
        print("product quantity:",self.quantity)
        print("total price:",self.calculate_total())
name=input("enter the name: ")
price=float(input("enter the price: "))
quantity=int(input("enter the quantity: "))
product=product(name,price,quantity)
product.display()







    


        