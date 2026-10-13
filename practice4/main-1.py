READ = 1
WRITE = 2
DELETE = 4

rights = READ | WRITE

print("Початкові права:", rights)
print("Читання:", (rights & READ) != 0)
print("Видалення:", (rights & DELETE) != 0)

rights = rights | DELETE
print("Після додавання права:", rights)

rights = rights & ~WRITE
print("Після видалення права на запис:", rights)

rights = rights ^ READ
print("Після перемикання права читання:", rights)