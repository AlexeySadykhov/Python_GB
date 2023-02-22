import sys

# Task 10
arr_length = int(input("Task 10.\nEnter the length of the array:"))
nums = [int(input("Enter the number:")) for _ in range(arr_length)]
print(min([len(list(filter(lambda x: x == 0, nums))), len([x for x in nums if x == 1])]))

# Task 12
x = int(input("Task 12.\nEnter x:"))
y = int(input("Enter y:"))
for i in range(x):
    for j in range(y):
        if i + j == x and i * j == y:
            print(i, j)
            sys.exit(0)

# Task 14
n = int(input("Task 14.\nEnter n:"))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
