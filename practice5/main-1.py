numbers = [8, -4, 8, 0, 7, -9]

total = 0
minimum = numbers[0]
maximum = numbers[0]

positive = 0
negative = 0
zero = 0
count = 0

for num in numbers:
    total += num
    count += 1

    if num < minimum:
        minimum = num

    if num > maximum:
        maximum = num

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

average = total / count

print("Список:", numbers)
print("Сума:", total)
print("Середнє арифметичне:", average)
print("Мінімум:", minimum)
print("Максимум:", maximum)
print("Додатних чисел:", positive)
print("Від'ємних чисел:", negative)
print("Нулів:", zero)