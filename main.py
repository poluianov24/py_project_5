try:
    l = []
    while True:
        inp = int(input('\033[33mВведіть елементи списку (для продовження введіть "0"): '))
        if inp == 0:
            break
        else:
            app = l.append(inp)
    print(f'\033[35mВаш список такий {l}')
    print(f'Сума всіх елементів {sum(l)}')
    print(f'Середньоарифметичне всіх еліметнів: {sum(l) / len(l)}')
except Exception as e:
    print('\033[31mЩось пішло не так, спробуйте ще раз :( \n\033[36mСпробуйте вводити лише цифри')
