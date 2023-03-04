import random
import sys

# Task 30
first = int(input("Task 30.\nEnter the first element of the progression:"))
diff = int(input("Enter the difference:"))
length = int(input("Enter the length of the progression:"))
print([first + i * diff for i in range(length)])

# Task 32
lst = [random.randint(-9, 9) for _ in range(10)]
print("Task 32.\nRandom numbers:", lst)
min_val = int(input("Enter min value:"))
max_val = int(input("Enter max value:"))
if max_val < min_val:
    print("Max value must be greater then min value.")
    sys.exit(1)
print([num for num in lst if min_val <= num <= max_val])
# Или так:
print(list(filter(lambda num: min_val <= num <= max_val, lst)))
