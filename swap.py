first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print(f"\nИсходные значения: first_room = {first_room}, second_room = {second_room}")

# Обмен через третью переменную
temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена:   first_room = {first_room}, second_room = {second_room}")
