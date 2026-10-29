original = [int(x) for x in input("Целые числа через пробел: ").split()]
new = [abs(x) if x < 0 else x for x in original]

print(f"Исходный список: {original}")
print(f"Новый список: {new}")