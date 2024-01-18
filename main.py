l = []
while True:
    inp = input('Введіть елементи списку (для продовження введіть "next"): ')
    if inp == 'next':
        break
    else:
        app = l.append(inp)

print(f'Ваш список такий {l}')
digit = input('Введіть число яке бажаєте знайти в списку: ')
s = ''.join(l)
res = s.count(digit)
print(res)
