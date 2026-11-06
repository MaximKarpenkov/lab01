print("--- Оформление заказа (Вариант 1: Канцелярия) ---")
order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

# Позиция 1
item1_name = input("\nНазвание первой позиции: ")
item1_qty = int(input("Количество: "))
item1_price = float(input("Цена за единицу (руб.): "))

# Позиция 2
item2_name = input("\nНазвание второй позиции: ")
item2_qty = int(input("Количество: "))
item2_price = float(input("Цена за единицу (руб.): "))

# Доставка и оплата
delivery_cost = float(input("\nСтоимость доставки (руб.): "))
paid_amount = float(input("Внесённая сумма (руб.): "))

# Вычисления
item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
goods_total = item1_total + item2_total
grand_total = goods_total + delivery_cost
total_qty = item1_qty + item2_qty
change = paid_amount - grand_total

# Вывод чека
print("\n" + "=" * 50)
print(f"ЗАКАЗ: {order_name}")
print(f"Заказчик: {customer_name}")
print("=" * 50)
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {item1_total:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {item2_total:.2f}")
print("-" * 50)
print(f"Стоимость товаров: {goods_total:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"ИТОГО К ОПЛАТЕ: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")
print("=" * 50)
