# Basic variables
x = 5
y = "John"

print(x)
print(y)

# Reassigning changes the value (and can change the type)
x = 4  # int
x = "Sally"  # now str
print(x)

# Casting examples
x = str(3)  # '3'
y = int(3)  # 3
z = float(3)  # 3.0
print(x, y, z)

# Inspect types
x = 5
y = "John"
print(type(x))
print(type(y))

# Valid variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Invalid names (uncomment to see SyntaxError):
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
