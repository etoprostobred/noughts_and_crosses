def start():
    greeting = """
***********************************
*              ИГРА               *
*        «КРЕСТИКИ-НОЛИКИ»        *
*        ПРИВЕТСТВУЕТ ВАС!        *
***********************************

Вы же знаете правила игры?
     """
    print(greeting)

    while True:
        rools = """
Правила: 
Максимальное количество игроков — два.
Один игрок — крестик, второй — нолик.
Нужно по очереди ставить на свободные
клетки поля 3×3 свой знак таким образом,
чтобы занять весь ряд из трёх клеток
по вертикали, горизонтали или диагонали.
Первый игрок, занявший ряд, выигрывает.
Если все ячейки заполнены, но ни один ряд
так и не собрался, объявляется ничья.
Первым ходит крестик.

Теперь вы готовы. Поехали!"""
        knowledge = input("Введите «да» или «нет»: ")
        print(knowledge)
        if knowledge.lower() == "да":
            print("Окей, тогда начнём!")
            break
        if knowledge.lower() == "нет":
            print(rools)
            break
        else:
            print("Не понимаю, повторите ввод!")
            print("Нужно ввести «да» или «нет».")

    print("""
Чтобы поставить значок, введите номер клетки.
Напечатайте два числа без пробелов, где
первое —  строчка, а второе — столбец""")

def show_field():
    print(f'| - | 0 | 1 | 2 |')
    print(f'-----------------')
    for i in range(3):
        print(f'| {i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |')
        print(f'-----------------')


def insert_sorry_not_sorry():
    print("                   ")
    print("     ¯\_(ツ)_/¯    ")
    print("                   ")
    print("Попробуйте ещё раз!")
    print("                   ")
    return "____________________"

def make_step():  # Поменяй название
    while True:
        squares = input("Выбираем клеточку номер: ")

        if len(squares) != 2:
            print("                                       ")
            print("Что тут написано? Ничего не понимаю... ")
            insert_sorry_not_sorry()
            print("                                       ")
            print("(Пссс: введите два числа без пробелов и лишних символов.)")
            continue

        x, y = squares[0], squares[1]

        if not (x.isdigit()) or not (y.isdigit()):
            print("              ")
            print("Нужно использовать только цифры!")
            insert_sorry_not_sorry()
            continue

        x, y = int(x), int(y)

        if field[x][y] != " ":
            print("                      ")
            print("Упс... Тут уже занято!")
            insert_sorry_not_sorry()
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("                     ")
            print("Отправляемся в открытый космос!  ")
            print("Таких клеток нет на поле...  ")
            insert_sorry_not_sorry()
            continue

        return x, y


def check_win():
    win_squares = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                   ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                   ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for square in win_squares:
        symbols = []
        for j in square:
            symbols.append(field[j[0]][j[1]])
        if symbols == ["X", "X", "X"]:
            print("!!!Это победа!!!Крестик — чемпион!!!")
            return True

        if symbols == ["0", "0", "0"]:
            print("!!!Это победа!!!Нолик — чемпион!!!")
            return True

    return False


start()
field = [[" "] * 3 for i in range(3)]

step = 0
while True:
    step += 1
    show_field()
    if step % 2 == 1:
        print("***********************************")
        print("Ход крестика.")
    else:
        print("***********************************")
        print("Ход нолика.")

    x, y = make_step()

    if step % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if step == 9:
        print("Ничья... Пожмём руки...")
        break