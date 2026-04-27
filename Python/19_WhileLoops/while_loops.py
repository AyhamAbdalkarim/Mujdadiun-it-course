n = 3
while n > 0:
    print(n)
    n -= 1

i = 0
while True:
    i += 1
    if i == 2:
        continue
    if i > 4:
        break
    print("i =", i)
