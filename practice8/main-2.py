energy = [10, 15, 12, 20, 18, 25]

prefix = [0]

for i in range(len(energy)):
    prefix.append(prefix[i] + energy[i])

left = 1
right = 4

total = prefix[right + 1] - prefix[left]

print("Енергоспоживання за вибраний період:", total)