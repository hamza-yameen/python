print("Variables......")

print("---------------------------------------- 1")

x1 = 5
y1 = "John"
print("x1 : ", x1)
# Output:- x1 :  5
print("y1 : ", y1)
# Output:- y1 :  John

print("---------------------------------------- 2")

x2 = 5
x2 = "name"
print("x2 : ",x2)
# Output:- x2 :  name

print("---------------------------------------- 3")

# How to Get the Type of variable
x3 = "Python"
y3 = 3
print("x3 type : ", type(x3)) 
# Output:- x3 type :  <class 'str'>
print("y3 type : ", type(y3))
# Output:- y3 type :  <class 'int'>

print("---------------------------------------- 4")

# We can assign multiple values at once
x4, y4, z4 = "Python", "Javascript", "Typescript"
print(x4) # Python
print(y4) # Javascript
print(z4) # Typescript

print("---------------------------------------- 5")

# We assign a single value to multiple variable names at once.
x5 = y5 = z5 = "Python"
print(x5) # Python
print(y5) # Python
print(z5) # Python

print("---------------------------------------- 6")

# Unpack a Collection
programmingLanguages = ["Python", "JavaScript", "TypeScript"]
x6, y6, z6 = programmingLanguages
print(x6) # Python
print(y6) # JavaScript
print(z6) # TypeScript
