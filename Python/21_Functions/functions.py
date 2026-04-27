def greet(name: str, polite: bool = True) -> None:
    if polite:
        print(f"Hello, {name}!")
    else:
        print(f"Hi {name}")


greet("Ayham")
greet("Sam", polite=False)


def total(*nums: int) -> int:
    return sum(nums)


print(total(1, 2, 3))


def keywords(**kw: str) -> None:
    for k, v in kw.items():
        print(k, v)


keywords(a="1", b="2")

square = lambda x: x * x
print(square(5))
