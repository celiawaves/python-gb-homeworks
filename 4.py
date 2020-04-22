def func4(x, y):
    return 1 / x ** abs(y)


print(func4(3, -2))


# **************************************************Вариант решения****************************************************

def func_4(a, b):
    res = 1
    for i in range(abs(b)):
        res *= a
    if b >= 0:
        return res
    else:
        return 1 / res


print(func_4(3, -2))
