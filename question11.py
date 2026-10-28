
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def calculate_total(self):
        return self.mark1 + self.mark2 + self.mark3
    def calculate_average(self):
        return self.calculate_total() / 3
    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "Fail"
    def display(self):
        print("\nStudent Name:", self.name)
        print("Total Marks:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.calculate_grade())
name = input("Enter student name: ")
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

student = Student(name, mark1, mark2, mark3)
student.display()
