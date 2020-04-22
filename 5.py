def sum_func():
    sum_result = 0
    do_exit = False
    while not do_exit:
        numbers = input('Введите числа через пробел или Q, чтобы выйти: ').upper().split()
        result = 0
        for i in range(len(numbers)):
            if numbers[i] == 'Q':
                do_exit = True
            else:
                result = result + int(numbers[i])
        sum_result = sum_result + result
        print(f'Текущая сумма всех элементов: {sum_result}')
    return f'Конечная сумма всех элементов: {sum_result}'


print(sum_func())
