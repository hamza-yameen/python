print("Welcome to the Python Learning Series...")

print("---------------------------------------- 1")

name = input("Enter Your Name?")
print("Hello, " + name + "!")
# Output:- Hello, python!

print("---------------------------------------- 2")

age1 = input("Enter Your age?")
print("Age : " + age1)
# Output:- Age : 45
print("Type of the Age: ", type(age1))
# Output:- Type of the Age:  <class 'str'>
print("Convert into Int : ", type(int(age1)))
# Output:- Convert into Int :  <class 'int'>

print("---------------------------------------- 3")

age2 = int(input("Enter your age?\n"))
city = input("Enter your city?\n")
print(f"You are {age2} years old and live in {city}.")
# Output:- You are 34 years old and live in Lahore.

print("---------------------------------------- 4")

while True:
    number = input("Enter a number (or 'quit' to exit): ")
    if number == "quit":
        break
    print(int(number) ** 2)