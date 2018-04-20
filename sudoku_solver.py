import math
import time


def discard_vertical(puzzle):
    for i in range(9):
        for j in range(9):
            if isinstance(puzzle[i][j], int):
                number_to_discard = puzzle[i][j]
                k = j
                while k < 9:
                    if isinstance(puzzle[i][k], set):
                        puzzle[i][k].discard(number_to_discard)
                    k += 1
                k -= 1
                while k > -1:
                    if isinstance(puzzle[i][k], set):
                        puzzle[i][k].discard(number_to_discard)
                    k -= 1


def check_if_valid(puzzle):
    list_to_check = []
    for i in range(9):
        for j in range(9):
            try:
                list_to_check.append(puzzle[i][j])
            except IndexError:
                pass
    if len(list_to_check) != 81:
        print(f"You have entered invalid number of arguments, your string should contain 81 elements,"
              f"not {len(list_to_check)}")
        return False
    for i in range(9):
        for j in range(9):
            try:
                puzzle[i][j] = int(puzzle[i][j])
            except ValueError:
                print(f"Your string contains letter {puzzle[i][j]}, be sure to input only integer elements")
                return False
    return True


def sudoku_solver(puzzle):
    timeout = time.time() + 2

    is_valid = check_if_valid(puzzle)
    if not is_valid:
        return

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                puzzle[i][j] = set(range(1, 10))

    while True:

        discard_vertical(puzzle)
        discard_vertical([*zip(*puzzle)])

        for i in range(9):
            for j in range(9):
                if isinstance(puzzle[i][j], int):
                    number_to_discard = puzzle[i][j]
                    i_square_start = int(math.floor(i // 3) * 3)
                    j_square_start = int(math.floor(j // 3) * 3)
                    for k in range(3):
                        for z in range(3):
                            if isinstance(puzzle[i_square_start + k][j_square_start + z], set):
                                puzzle[i_square_start + k][j_square_start + z].discard(number_to_discard)

        for i in range(9):
            for j in range(9):
                if isinstance(puzzle[i][j], set) and (len(puzzle[i][j]) == 1):
                    puzzle[i][j] = list(puzzle[i][j])
                    puzzle[i][j] = puzzle[i][j][0]

        if all(isinstance(puzzle[i][j], int) for i in range(9) for j in range(9)):
            break

        if time.time() > timeout:
            print(f"Your input {puzzle} is not a valid sudoku or it can't' be solved deterministically.")
            return

    return puzzle


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solved = sudoku_solver(puzzle=puzzle)
    print(solved if solved is not None else '')
