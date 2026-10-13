import math

a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2

    x = p * (p - a) * (p - b) * (p - c)

    if x >= 0:
        s = math.sqrt(x)
        print("Площа трикутника:", s)
    else:
        print("Помилка")
else:
    print("Такого трикутника не існує")
