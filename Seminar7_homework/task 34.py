def is_equal(array):
    for item in array:
        if item != array[0]:
            return False
    return True


vowels = "аеёиоуыэюя"

text = input("Enter the text:").split()
vowels_cnt = []
cnt = 0
for ph in text:
    for l in ph:
        if l in vowels:
            cnt += 1
    vowels_cnt.append(cnt)
    cnt = 0

print("Парам пам-пам" if is_equal(vowels_cnt) else "Пам парам")
