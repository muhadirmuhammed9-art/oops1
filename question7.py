class book:
    def __init__(self,title,author,price):
        self.title= title
        self.author= author
        self.price= price
    def display(self):
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
title=(input("enter the title: "))
author=(input("enter author name: "))
price= (input("enter the price: "))

b1= book (title , author, price)
b1.display()

    

    
