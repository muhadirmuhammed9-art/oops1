class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increase_salary(self,percentage):
        increment =self.salary * percentage /100
        self.salary =self.salary + increment
    def display(self):
        print("employee name:",self.name)
        print("updated salary:",self.salary)
name= input("enter employee name: ")
salary= float(input("enter current salary: "))
percentage= float(input("enter salary increace percentage: "))
emp= employee(name,salary)
emp.increase_salary(percentage)
emp.display()
