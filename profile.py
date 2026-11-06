# Запрос данных
last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет): "))
subject = input("Любимый предмет: ")
hours_per_week = float(input("Количество часов подготовки в неделю: "))

# Вычисления
age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
average_hours_per_day = hours_per_week / 7

# Вывод карточки
print("\n" + "=" * 40)
print("КАРТОЧКА СТУДЕНТА")
print("=" * 40)
print(f"Имя и фамилия: {first_name} {last_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age} лет")
print(f"Любимый предмет: {subject}")
print("-" * 40)
print(f"Возраст через 4 года: {age_in_4_years} лет")
print(f"Время подготовки за 4 недели: {hours_in_4_weeks:.2f} ч.")
print(f"Среднее время подготовки в день: {average_hours_per_day:.2f} ч.")
print("=" * 40)
