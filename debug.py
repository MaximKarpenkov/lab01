print("--- Фрагмент А ---")
first = "2"
second = "3"
# Вывод типов до преобразования
print(f"Типы до: {type(first)}, {type(second)}")
sum_a = int(first) + int(second)
# Вывод типов после
print(f"Типы после: {type(int(first))}, {type(int(second))}")
print(f"Сумма: {sum_a}")

print("\n--- Фрагмент Б ---")
age_str = input("Возраст: ")
print(f"Тип до: {type(age_str)}")
age = int(age_str)
print(f"Тип после: {type(age)}")
print(f"Возраст через год: {age + 1}")

print("\n--- Фрагмент В ---")
first_num = 4
second_num = 7
third_num = 10
# Исправление приоритета операций
average = (first_num + second_num + third_num) / 3
print(f"Среднее: {average}")
