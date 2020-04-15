# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

inputTime = int(input('Введите время в секундах: '))
hours = inputTime // 3600
residue = inputTime % 3600
minutes = residue // 60
sec = residue % 60
print(f"В формате ЧЧ:ММ:СС: {hours}:{minutes}:{sec}")
