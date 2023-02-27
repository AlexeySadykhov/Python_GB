import random
import advanced_functions as func
# Task 22


def get_input(user_input=True):
    length = int(input("Enter the length of the array:"))
    if not user_input:
        return [random.randint(0, 100) for _ in range(length)]
    else:
        return [int(input("Enter the number:")) for _ in range(length)]


# Вообще, нормальные люди вот так делают:
# n = set(map(int, input("Enter numbers splitting values by space:").split()))
# Зачем надо вот эту длину вводить вообще не понятно. Последовательность она
# и в Африке последовательность, у нее всегда есть длина. Ввод этих чисел
# с длиной в данном случае совершенно бесполезен и выглядит по-уродски.
# Ввели первую последовательность, ввели вторую и все. Так и должно быть.

print("Task 22.")
n = set(get_input())
# По приколу добавил рандомную последовательность:
m = set(get_input(user_input=False))
print(n, m)
print(sorted(m & n))
# Альтернативный вариант с сортировкой пузырьком:
print(func.bubble_sort(m & n))

# Task 24
print("Task 24.")
array = get_input(user_input=False)
print(array)
result = [array[i] + array[i - 1] + array[i + 1] for i in range(len(array) - 1)]
result.append(array[-2] + array[-1] + array[0])
print(max(result))
# Ну и, опять же, альтернативный поиск максимума ручками.
# Чтобы скучно не было)))
print(func.find_max(result))
