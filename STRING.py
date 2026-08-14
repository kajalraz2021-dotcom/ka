# first python program
print("hello world")    
print("hello world")
# A variable is just a  lable for a value
name = "Kajal"
print(name)
# Dynamic typed
name = "Kajal"
print( name)

# Today it can point to a string
x = "hello"
print(type(x))
# Later it can point to an integer
x = 5
print(type(x))
# Updation of variable  
Name = "Kajal"
print(Name)
Name = "Rakhi"
print(Name)

a=10
b=20
c=a+b
print(c)
# Data type in python
a = 10
b = "Kaushik"
c = 10.5
d = True
h = None
# Dynamic - Python re -detects the data type
a = "Kajal"
# Built-in Functions
a = "Kajal"
print(type(a))
# Primitive-one value
a = 10
y = "Python"
z = None
# Collection- many values
nums = [1, 2, 3]
pair = (1, 2)
uniq = {1, 2, 3 }
info = {"a":1}
print((type(nums)))
# 1. Escape
print("Hello\"World\"")
# 2. Mix quote types
print('Hello "World"')
# 3. Triple quotes
print("""Hello
World""")
# Built-in 
print(len("Kajal"))
# External(after import)
import math
print(math.sqrt(4))
 # user-defined
def greet(name):
    return "Hello " + name
print(greet("Kajal"))
# Built-in functions
name = input("Enter your name: ")
print(name)
# Read text
name = input("25 ")
print(type(name))
# Read numbers
age = int(input("Enter your age: "))
print(type(age))

text = "Kajal"
num = 10
 # Function- work on either
print(type(text))
print(len(text))
# Methods- class-specific
print(text.upper())
print(num.bit_length())
