def isValidSudoku(board):
    for row in board:
        seen = set()
        for cell in row:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)

    for col in range(9):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)

    for block_row in range(3):
        for block_col in range(3):
            seen = set()
            start_row = block_row * 3
            start_col = block_col * 3


            for i in range(3):
                for j in range(3):
                    cell = board[start_row + i][start_col + j]
                    if cell != '.':
                        if cell in seen:
                            return False
                        seen.add(cell)

    return True


def input_sudoku():
    board = []
    print("Введите доску Sudoku (9 строк по 9 символов):")
    print("Используйте цифры 1-9 для заполненных клеток и '.' для пустых")

    for i in range(9):
        while True:
            row_input = input(f"Строка {i + 1}: ").strip()

            if len(row_input) != 9:
                print("Ошибка: строка должна содержать ровно 9 символов!")
                continue

            if not all(c in '123456789.' for c in row_input):
                print("Ошибка: используйте только цифры 1-9 и '.'!")
                continue

            row = list(row_input)
            board.append(row)
            break

    return board


board = input_sudoku()

print("\nВведённая доска:")
for row in board:
    print(' '.join(row))

print(isValidSudoku(board))
