nums = [int(x) for x in input("Целые числа через пробел: ").split()]

if not nums:
    print("Нет данных")
else:
    maximum = max(nums)
    positions = [i for i, x in enumerate(nums) if x == maximum]
    print(positions)