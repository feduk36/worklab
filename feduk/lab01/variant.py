
order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

position1_name = input("Название первой позиции: ")
position1_quantity = int(input("Количество первой позиции: "))
position1_price = float(input("Цена за единицу первой позиции (руб.): "))

position2_name = input("Название второй позиции: ")
position2_quantity = int(input("Количество второй позиции: "))
position2_price = float(input("Цена за единицу второй позиции (руб.): "))

delivery_cost = float(input("Стоимость доставки (руб.): "))

paid_amount = float(input("Внесённая сумма (руб.): "))
position1_cost = position1_quantity * position1_price
position2_cost = position2_quantity * position2_price
total_goods_cost = position1_cost + position2_cost
amount_with_delivery = total_goods_cost + delivery_cost
total_quantity = position1_quantity + position2_quantity
change = paid_amount - total_amount_with_delivery

# Вывод результатов
print(f"\nЗаказ: {order_name}")
print(f"Заказчик: {customer_name}")
print(f"\n{position1_name} | {position1_quantity} | {position1_price:.2f} | {position1_cost:.2f}")
print(f"{position2_name} | {position2_quantity} | {position2_price:.2f} | {position2_cost:.2f}")
print(f"\nИтоги:")
print(f"Стоимость товаров: {total_goods_cost:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"Общая сумма: {total_amount_with_delivery:.2f} руб.")
print(f"Общее количество: {total_quantity} ед.")
print(f"Сдача: {change:.2f} руб.")
