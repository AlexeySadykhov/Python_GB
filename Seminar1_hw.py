# Task 2
def sum_of_digits(number):
    return sum(map(int, number))


print(sum_of_digits(input("Task 1.\nEnter the number:")))

# Task 4
# Пусть x - количество журавликов для Пети и для Сережи. Мы точно знаем что это одно и то же число.
# Тогда получаем уравнение:
# 2(x + x) + x + x = s
# Соответственно:
# 4x + 2x = s
# 6x = s
# Ответ: x = s / 6
s = int(input("Task 4.\nEnter S:"))
x = s // 6
print(x, x * 4, x)

# Task 6
num = input("Task 6.\nEnter the number:")
print("yes" if sum_of_digits(num[3:]) == sum_of_digits(num[:3]) else "no")

# Task 8
n = int(input("Task 8.\nEnter n:"))
m = int(input("Enter m:"))
k = int(input("Enter k:"))
print("yes" if k < n * m and (k % n == 0 or k % m == 0) else "no")
