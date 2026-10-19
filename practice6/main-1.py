text = input("Введіть рядок: ")

big = 0
small = 0
digits = 0
other = 0

for char in text:
    code = ord(char)

    if code >= 65 and code <= 90:
        big += 1
    elif code >= 97 and code <= 122:
        small += 1
    elif code >= 48 and code <= 57:
        digits += 1
    else:
        other += 1

print("Великі літери:", big)
print("Малі літери:", small)
print("Цифри:", digits)
print("Інші символи:", other)