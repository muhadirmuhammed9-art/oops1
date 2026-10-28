class person:
    def __init__(self,name ,age):
        self.name =name
        self.age =age
    def  display_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
name = input("enter the name:")
age = input("enter the age:") 
person1=person(name,age)
person1.display_details()

        