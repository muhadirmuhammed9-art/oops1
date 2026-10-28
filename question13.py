
class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        print("Temperature in Celsius:", celsius)


temp = Temperature()

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    temp.celsius_to_fahrenheit(celsius)

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temp.fahrenheit_to_celsius(fahrenheit)

else:
    print("Invalid choice")
