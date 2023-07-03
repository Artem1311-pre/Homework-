def greet():
    print("-------------------")
    print("  Добро пожаловать ")
    print("      в игру     ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" Правила игры: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def look():
    print()
    print(f"  | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(field):
        row_str = f" {i}| {' | '.join(row)} | "
        print(row_str)
        print("---------------")
    print()
def ask():
    while True:
        items = input("      Сделайте ваш ход: ").split()
        if len(items) != 2:
            print(" Введите 2 координаты!!!")
            continue
        x, y = items
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите цифры!!!")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or y < 0 or y > 2:
            print(" Вы не попали в поле:)")
            continue
        if field[x][y] != " ":
            print(" Место занято!")
            continue
        return x, y
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    look()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break