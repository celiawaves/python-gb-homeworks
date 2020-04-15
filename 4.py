# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Введите значение полученной выручки: '))
costs = int(input('Введите значение издержек фирмы: '))

if revenue > costs:
    profit = revenue - costs
    print(f'Ваша прибыль: {profit}')
    workers = int(input('Сколько сотрудников работает в вашей компании? '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit / workers}')
elif revenue == costs:
    print('Ваша фирма сейчас работает ровно в 0')
else:
    print('Ваша фирма терпит убытки')
