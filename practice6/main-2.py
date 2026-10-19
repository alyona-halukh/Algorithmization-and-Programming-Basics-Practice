text = input("Введіть рядок: ")

text = text.lower()

left = 0
right = len(text) - 1

palindrome = True

while left < right:
    if text[left] != text[right]:
        palindrome = False

    left += 1
    right -= 1

print("Паліндром:", palindrome)