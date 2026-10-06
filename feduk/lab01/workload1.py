subject1 = input("Название первого предмета: ")
count1 = int(input("Количество занятий по первому предмету за неделю: "))

subject2 = input("Название второго предмета: ")
count2 = int(input("Количество занятий по второму предмету за неделю: "))

duration = int(input("Продолжительность одного занятия в минутах: "))
available_hours = float(input("Доступное время на неделю в часах: "))

time1 = count1 * duration
time2 = count2 * duration
total_minutes = time1 + time2
total_hours = total_minutes / 60

free_hours = available_hours - total_hours
four_weeks_minutes = total_minutes * 4
four_weeks_hours = four_weeks_minutes / 60

print(subject1, ":", time1, "минут")
print(subject2, ":", time2, "минут")
print("Общая нагрузка:", total_minutes, "минут")
print(f"Общая нагрузка: '{total_hours:.2f}' часов")
print(f"Свободное время: '{free_hours:.2f}' часов")
print(f"Нагрузка за 4 недели:", four_weeks_minutes, "минут")
print(f"Нагрузка за 4 недели: '{four_weeks_hours:.2f}' часов")