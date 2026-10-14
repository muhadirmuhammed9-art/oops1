class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print("\nEmployee Information")
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

e1 = Employee(name, employee_id, salary)

e1.display_info()