epsilon = 0.01

n = int(input("Кількість товарів: "))

suma = 0

for i in range(n):
    cina = float(input("Введіть ціну товару: "))
    suma = suma + cina

print("Сума товарів: ", round(suma, 2))