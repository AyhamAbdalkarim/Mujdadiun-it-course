# Built-in types (samples)

s = "Hello"
n = 42
f = 3.14
b = True
lst = [1, 2, 3]
tup = (1, 2, 3)
st = {1, 2, 3}
d = {"a": 1}
x = None

for name, val in [
    ("str", s),
    ("int", n),
    ("float", f),
    ("bool", b),
    ("list", lst),
    ("tuple", tup),
    ("set", st),
    ("dict", d),
    ("NoneType", x),
]:
    print(name, "->", type(val))
