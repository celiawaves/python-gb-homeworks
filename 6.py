def int_func(user_input):
    """
    Функция перебирает каждый символ на принадлежность его к диапазону 97-122 в таблице ASCII
    с помощью цикла for-in, сохраняет в список symbol_list,
    затем с помощью метода .join() возвращает строку с методом .title()


    """
    symbol_list = []
    for symbol in user_input:
        if 97 <= ord(symbol) <= 122 or ord(symbol) == 32:
            symbol_list.append(symbol)
        else:
            return 'Введите предложение из маленьких латинских букв'
    return ''.join(symbol_list).title()


print(int_func(user_input=input(
    'Введите строку из слов, разделённых пробелами из латинских букв в нижнем регистре:\n"Q" для выхода:  ')))
