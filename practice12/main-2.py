# Counting sort
numbers = [4, 5, 8, 3, 3, 1]
max_val = max(numbers)
count = [0] * (max_val + 1)
for num in numbers:
    count[num] += 1

sorted_numbers = []
for val in range(len(count)):
    sorted_numbers.extend([val] * count[val])
print(sorted_numbers)
