print("Numbers Types (Integer/Float/Complex)")

print("---------------------------------------- 1")

x1 = 1
y1 = 35656222554887711
z1 = -3255522

print(type(x1)) # <class 'int'>
print(type(y1)) # <class 'int'>
print(type(z1)) # <class 'int'>

print("---------------------------------------- 2")

x2 = 1.10
y2 = 1.0
z2 = -35.59

print(type(x2)) # <class 'float'>
print(type(y2)) # <class 'float'>
print(type(z2)) # <class 'float'>

print("---------------------------------------- 3")

x3 = 35e3
y3 = 12E4
z3 = -87.7e100

print(type(x3)) # <class 'float'>
print(type(y3)) # <class 'float'>
print(type(z3)) # <class 'float'>

print("---------------------------------------- 4")

x4 = 3+5j
y4 = 5j
z4 = -5j

print(type(x4)) # <class 'complex'>
print(type(y4)) # <class 'complex'>
print(type(z4)) # <class 'complex'>

print("---------------------------------------- 5")

# Integer
x4 = 10 
print("x4 - " , type(x4) , " - " , x4)
# Output:- x4 -  <class 'int'>  -  10

# Float
y4 = 3.14  
print("y4 - " , type(y4) , " - " , y4)
# Output:- y4 -  <class 'float'>  -  3.14

# Complex number
z4 = 2 + 3j  
print("z4 - " , type(z4) , " - " , z4)
# Output:- z4 -  <class 'complex'>  -  (2+3j)

print("---------------------------------------- 6")

x6 = int(1)
y6 = int(2.8)
z6 = int("3")
print(x6) # Output:- 1
print(y6) # Output:- 2
print(z6) # Output:- 3

print("---------------------------------------- 7")

x7 = float(1)
y7 = float(2.8)
z7 = float("3")
w7 = float("4.2")
print(x7) # Output:- 1.0
print(y7) # Output:- 2.8
print(z7) # Output:- 3.0
print(w7) # Output:- 4.2

print("---------------------------------------- 8")

x8 = complex(7)
print(x8) # output:- (7+0j)