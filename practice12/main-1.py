# Bubble sort
numbers = [67, 28, 34, 13, 74, 91, 10]
n = len(numbers)

for i in range(n - 1):
    for j in range(n - 1 - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)
