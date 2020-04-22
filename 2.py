def func2(name, surname, year, city, email, phonenum):
    return f'{name} {surname} {year} г.р, из города {city}, email: {email}, phone number: {phonenum}'


print(func2(name='Azat',
            surname='Shabanov',
            year=1997, city='Moscow',
            email='celiawaves@yandex.ru',
            phonenum='+79171309418'))