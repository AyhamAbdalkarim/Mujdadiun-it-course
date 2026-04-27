# List as dynamic array
items = [10, 20, 30]
items.append(40)
items[1] = 25
print(items)

# Standard library array (typed C array)
import array

nums = array.array("i", [1, 2, 3])
nums.append(4)
print(nums.tolist())
