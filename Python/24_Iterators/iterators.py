it = iter([1, 2, 3])
print(next(it), next(it))


def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


for x in countdown(3):
    print(x)
