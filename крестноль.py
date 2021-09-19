
pitch = [ [' '] * 3 for i in range(3)]

def draw_pitch():
    print('   | 0 | 1 | 2 |')
    print('-'* 17)

    for i, row in enumerate(pitch):
        row_str = f' {i} | {" | ".join(row)} |'
        print(row_str)
        print('-' * 17)


def ask():
    while True:
        vvod = input('Ваш ход:').split()

        if len(vvod) != 2:
            print('Ведите две координаты ')
            continue

        x, y = vvod

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
           print('вне диапазонa')
           continue

        if pitch[x][y] != ' ':
            print('клетка занята')
            continue
        return x, y
# ask()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(pitch[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл Х!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выиграл 0!')
            return True
    return False

num = 0
while True:
    num +=1
    draw_pitch()
    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask()
    if num % 2 == 1:
        pitch[x][y] = 'X'
    else:
        pitch[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print('ничья')
        break




