print("Datatypes.......")

print("--------- 1-Numeric Data Types ---------")

# Integer
x1 = 10 
print("x1 - " , type(x1) , " - " , x1)
# Output:- x1 -  <class 'int'>  -  10

# Float
y1 = 3.14  
print("y1 - " , type(y1) , " - " , y1)
# Output:- y1 -  <class 'float'>  -  3.14

# Complex number
z1 = 2 + 3j  
print("z1 - " , type(z1) , " - " , z1)
# Output:- z1 -  <class 'complex'>  -  (2+3j)

print("--------- 2-Sequence Data Types ---------")

# List: Ordered collection of elements, which can be of different data types and can be modified.
myList = [1, 2.5, "hello", True]
print("myList : ", myList)
# Output:- myList :  [1, 2.5, 'hello', True]
print("myList type : ", type(myList))
# Output:- myList type :  <class 'list'>

# tuple: Ordered collection of elements, which cannot be modified after creation.
my_tuple = (1, 2, 3)
print("my_tuple : ", my_tuple)
# Output:- my_tuple :  (1, 2, 3)
print("my_tuple type : ", type(my_tuple))
# Output:- my_tuple type :  <class 'tuple'>

# range: Represents a sequence of numbers, often used in loops.
my_range = range(5)
print("my_range : ", my_range)
# Output:- my_range :  range(0, 5)
print("my_range type : ", type(my_range))
# Output:- my_range type :  <class 'range'>

print("--------- 3-Mapping Data Type ---------")

# dict: Unordered collection of key-value pairs.
my_dict = {'name': 'Alice', 'age': 30}
print("my_dict : ", my_dict)
# Output:- my_dict :  {'name': 'Alice', 'age': 30}
print("my_dict type : ", type(my_dict))
# Output:- my_dict type :  <class 'dict'>

# set: Unordered collection of unique elements.
my_set = {1, 2, 3, 2}
print("my_set : ", my_set)
# Output:- my_set :  {1, 2, 3}
print("my_set type : ", type(my_set))
# Output:- my_set type :  <class 'set'>

# frozenset: Immutable version of a set.
my_frozenset = frozenset([1, 2, 3])
print("my_frozenset : ", my_frozenset)
# Output:- my_frozenset :  frozenset({1, 2, 3})
print("my_frozenset type : ", type(my_frozenset))
# Output:- my_frozenset type :  <class 'frozenset'>

print("--------- 4-Boolean Data Type ---------")

is_true = True
is_false = False

print("--------- 5-Binary Data Types ---------")

# bytes: Immutable sequence of bytes.
my_bytes = b'hello'
print("my_bytes : ", my_bytes)
# Output:- my_bytes :  b'hello'
print("my_bytes type : ", type(my_bytes))
# Output:- my_bytes type :  <class 'bytes'>

# bytearray: Mutable sequence of bytes.
my_bytearray = bytearray(b'world')
print("my_bytearray : ", my_bytearray)
# Output:- my_bytearray :  bytearray(b'world')
print("my_bytearray type : ", type(my_bytearray))
# Output:- my_bytearray type :  <class 'bytearray'>

print("--------- 6-Text Types ---------")

x6 = "Hello World"
print("Text : ", x6)
# Output:- Text :  Hello World
print("Text type : ", type(x6))
# Output:- Text type :  <class 'str'>