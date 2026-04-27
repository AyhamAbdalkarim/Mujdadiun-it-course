for ch in "abc":
    print(ch)

for i in range(3):
    print("range", i)

words = ["one", "two"]
for idx, w in enumerate(words):
    print(idx, w)

for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)
