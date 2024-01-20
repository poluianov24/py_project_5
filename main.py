'''Напишіть функцію, яка перевіряє, чи є число простим. Число передається як параметр.
Якщо число просте потрібно повернути з методу true, в іншому разі — false.'''

def Prime(x):
    if x <= 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(Prime(7))