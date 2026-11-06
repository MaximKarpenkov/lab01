# Ввод данных
subject1 = input("Название первого предмета: ")
lessons1 = int(input(f"Количество занятий по предмету '{subject1}' в неделю: "))
duration1 = int(input("Продолжительность одного занятия (мин): "))

subject2 = input("Название второго предмета: ")
lessons2 = int(input(f"Количество занятий по предмету '{subject2}' в неделю: "))
duration2 = int(input("Продолжительность одного занятия (мин): "))

available_hours = float(input("Доступное время на неделю (в часах): "))

# Вычисления
time1 = lessons1 * duration1
time2 = lessons2 * duration2
total_minutes = time1 + time2
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

# Вывод
print("\n" + "=" * 40)
print("УЧЕБНАЯ НАГРУЗКА")
print("=" * 40)
print(f"{subject1}: {time1} минут в неделю")
print(f"{subject2}: {time2} минут в неделю")
print(f"Общая нагрузка: {total_minutes} минут ({total_hours:.2f} часов)")
print(f"Остаток свободного времени: {free_hours:.2f} часов")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} часов")
print("=" * 40)

