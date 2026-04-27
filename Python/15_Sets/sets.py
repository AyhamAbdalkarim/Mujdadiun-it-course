a = {1, 2, 3, 2}
print(a)

a.add(4)
a.remove(1)
print(a)

b = {3, 4, 5}
print("union", a | b)
print("intersection", a & b)

fs = frozenset([1, 2])
print(fs)
