fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "apricot")
print(fruits)

nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)

squares = [n * n for n in range(5)]
print(squares)

a = [1, 2]
b = a.copy()
b.append(3)
print("a", a, "b", b)
