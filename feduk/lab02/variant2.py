
total_volume = int(input("Введите общий объём (целое неотрицательное число): "))
capacity = int(input("Введите вместимость одной единицы (положительное число): "))

filled_units = total_volume // capacity

remainder = total_volume % capacity

min_units = (total_volume + capacity - 1) // capacity

print()
print("Общий объём:", total_volume)
print("Вместимость единицы:", capacity)
print()
print("Количество полностью заполненных единиц:", filled_units)
print("Остаток:", remainder)
print("Минимальное число единиц для размещения всего объёма:", min_units)
