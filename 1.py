def func1(x, y):
    try:
        print(int(x) / int(y))
    except ZeroDivisionError:
        print('Попытка деления на ноль!')
    except TypeError:
        print('Неверный формат данных!')
    except ValueError:
        print('Неверный формат данных!')


func1(x=input('Введите делимое: '), y=input('Введите делитель: '))