'''Напишіть функцію, яка повертає максимальне з чотирьох чисел. Числа передаються як параметри.'''

def Max(x, y, z, f):
#    return max(x, y, z, f) - простий спосіб
    if x >= y and x >= z and x >= f:
        return x
    elif y >= x and y >= z and y >= f:
        return y
    elif z >= x and z >= y and z >= f:
        return z
    else:
        return f

print(Max(7, -3, 12, 0))