git remote add origin https://github.com/feduk36/feduk.git
git branch -M main
git push -u origin main\
print("Фрагмент А")
first = "2"
second = "3"

print("Типы до преобразования:", type(first), type(second))
first = int(first)
second = int(second)

print("Типы после преобразования:", type(first), type(second))
print("Сумма:", first + second)
print("\nФрагмент Б")

age = input("Возраст: ")
print("Тип до преобразования:", type(age))
age = int(age)

print("Тип после преобразования:", type(age))
print("Возраст через год:", age + 1)
print("\nФрагмент В")



first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Среднее:", average)