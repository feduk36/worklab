data = input("Целые числа через пробел: ").split()

if not data:
    print("Нет данных")
else:
    nums = [int(x) for x in data]
    count = len(nums)
    total = sum(nums)
    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {min(nums)}")
    print(f"Максимум: {max(nums)}")
    print(f"Среднее: {total / count:.2f}")