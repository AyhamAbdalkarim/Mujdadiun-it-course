import greeting

print(greeting.hello("Ayham"))
print(greeting.PI)

from greeting import hello as hi

print(hi("World"))
