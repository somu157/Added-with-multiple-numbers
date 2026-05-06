from functools import reduce

numbers = [5, 10, 15, 20]

total = reduce(lambda x, y: x + y, numbers)

print("Sum:", total)
