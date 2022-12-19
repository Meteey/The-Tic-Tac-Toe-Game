import sys
import os


def check_list(game_table, turn):
    if game_table[0] != "-":
        ele = game_table[0]
    else:
        ele = "?"
    chk = True

    for item in game_table:
        if ele != item:
            chk = False
            break

    if chk and turn % 2 == 0:
        return True
    elif chk and turn % 2 != 0:
        return True
    else:
        return False


def win_checker(game_table, turn):
    x = []
    y1 = [0, 0, 0]
    y2 = [0, 0, 0]
    y3 = [0, 0, 0]
    z1 = [0, 0, 0]
    z2 = [0, 0, 0]
    for index_y in range(len(game_table)):
        x_axis_check = check_list(game_table[index_y], turn)
        x.append(x_axis_check)
        for index_x in range(len(game_table[index_y])):
            if index_x == 0:
                y1[index_y] = game_table[index_y][index_x]
            elif index_x == 1:
                y2[index_y] = game_table[index_y][index_x]
            elif index_x == 2:
                y3[index_y] = game_table[index_y][index_x]
            if index_x == index_y:
                z1[index_x] = game_table[index_y][index_x]
            if index_x + index_y == 2:
                z2[index_x] = game_table[index_y][index_x]
    y1_axis_check = check_list(y1, turn)
    y2_axis_check = check_list(y2, turn)
    y3_axis_check = check_list(y3, turn)
    z1_axis_check = check_list(z1, turn)
    z2_axis_check = check_list(z2, turn)

    total_check_list = x + [y1_axis_check, y2_axis_check, y3_axis_check, z1_axis_check, z2_axis_check]
    for item in total_check_list:
        if item:
            return True
    else:
        return False


def main():
    game_table = [["-", "-", "-"],
                  ["-", "-", "-"],
                  ["-", "-", "-"]]
    turn = 0

    while True:
        for display in range(len(game_table)):
            for block in range(len(game_table[display])):
                print(game_table[display][block], end=" ")
            print()

        if turn % 2 == 0:
            x = input("x:")
            while x not in ["1", "2", "3"]:
                x = input("x:")
            y = input("y:")
            while y not in ["1", "2", "3"]:
                y = input("y:")
            x = int(x)
            y = int(y)
            while game_table[y-1][x-1] in ["X", "O"]:
                print("There is full")
                os.system('cls')
                main()
            game_table[y-1][x-1] = "X"
            win_check = win_checker(game_table, turn)
            if win_check:
                print("X won")
                continue_check = input("To play again enter 1:")
                if continue_check == "1":
                    main()
                else:
                    sys.exit()
            else:
                turn += 1

        elif turn % 2 != 0:
            x = input("x:")
            while x not in ["1", "2", "3"]:
                x = input("x:")
            y = input("y:")
            while y not in ["1", "2", "3"]:
                y = input("y:")
            x = int(x)
            y = int(y)
            while game_table[y-1][x-1] in ["X", "O"]:
                print("There is full")
                os.system('cls')
                main()


            game_table[y-1][x-1] = "O"
            win_check = win_checker(game_table, turn)
            if win_check:
                print("0 won")
                continue_check = input("To play again enter 1:")
                if continue_check == "1":
                    main()
                else:
                    sys.exit()
            else:
                turn += 1


if __name__ == '__main__':
    main()
