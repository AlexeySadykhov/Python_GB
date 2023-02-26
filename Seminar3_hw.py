# Task 15

def get_input():
    arr_length = int(input("Enter the length of array:"))
    arr = [int(input("Enter the number:")) for _ in range(arr_length)]
    return arr, int(input("Enter desired number:"))


print("Task 15.")
array, x = get_input()
cnt = 0
for num in array:
    if num == x:
        cnt += 1
print(cnt)

# Ну вообще, я бы вот так сделал просто. Нет смысла даже в список преобразовывать.
print(input("Enter the array:").count(input("Enter desired number:")))

# Task 18
print("Task 18.")
array, x = get_input()
nearest = array[0]
for item in array:
    if abs(item - x) < abs(nearest - x):
        nearest = item
print(nearest)

# Task 20
letters = ["aeioulnstr", "dg", "bcmp", "fhvwy", "k",
           "jx", "qz", "авеинорст", "дклмпу", "бгёья",
           "йы", "жзхцч", "шэю", "фщъ"]
numbers = [1, 2, 3, 4, 5, 8, 10] * 2
dct = {k: n for w, n in zip(letters, numbers) for k in w}
word = input("Task 20.\nEnter a word:").lower()
sm = 0
for letter in word:
    if letter in dct:
        sm += dct[letter]
print(sm)
