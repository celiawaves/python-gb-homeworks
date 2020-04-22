def my_func(x, y, z):
    my_list = [int(x), int(y), int(z)]
    my_list.sort()
    return sum([my_list[-2], my_list[-1]])


print(my_func(33, 66, 34))