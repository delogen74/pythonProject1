# Поле
maps = [1,2,3,
        4,5,6,
        7,8,9]

pobeda = [[0,1,2],
          [3,4,5],
          [6,7,8],
          [0,3,6],
          [1,4,7],
          [2,5,8],
          [0,4,8],
          [2,4,6]]

# Результаты
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Делаем ход
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():
    win = ""

    for i in pobeda:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win

# Проверка линий
def check_line(sum_O, sum_X):
    step = ""
    for line in pobeda:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]

    return step

# Выбор хода
def AI():
    step = ""


    step = check_line(2, 0)


    if step == "":
        step = check_line(0, 2)


    if step == "":
        step = check_line(1, 0)


    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5


    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1

    return step

game = False
human = True

while game == False:

    print_maps()

    if human == True:
        symbol = "X"
        step = int(input("Ваш ход: "))
    else:
        print("Ход компьютера: ")
        symbol = "O"
        step = AI()

    if step != "":
        step_maps(step,symbol)
        win = get_result()
        if win != "":
            game = True
        else:
            game = False
    else:
        print("Ничья!")
        game = True
        win = "Ничья"

    human = not (human)

print_maps()
print("Победил", win)