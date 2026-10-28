def convert_currency(amount, rate):
    if amount < 0:
        raise ValueError("Сума не може бути від'ємною")

    if rate <= 0:
        raise ValueError("Курс має бути більшим за нуль")

    result = amount * rate
    return result


# Перевірка роботи функції
assert convert_currency(100, 40) == 4000
assert convert_currency(50, 2) == 100
assert convert_currency(0, 40) == 0

# Перевірка помилок
try:
    convert_currency(-100, 40)
    assert False
except ValueError:
    pass

try:
    convert_currency(100, 0)
    assert False
except ValueError:
    pass

print("Результат:", convert_currency(100, 40))
print("Автотести пройшли успішно")