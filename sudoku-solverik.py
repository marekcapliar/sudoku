import tkinter as tk

root = tk.Tk()

fr = open("sudoku/sudoku.txt", "r", encoding="UTF-8")
sudoku = []


def inputParser(fr, sudoku):
    for row in fr:
        temp = []
        for cc in row.strip():
            temp.append(int(cc))
        sudoku.append(temp)


def check(x: int, y: int, n: int) -> bool:
    for j in range(9):
        if sudoku[j][x] == n or sudoku[y][j] == n:
            return False
    x0, y0 = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[y0 + i][x0 + j] == n:
                return False
    return True


def sudokuSolver():
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if check(x, y, n):
                        sudoku[y][x] = n
                        if sudokuSolver():
                            return True
                        sudoku[y][x] = 0
                return False
    return True


def drawGrid():
    global window
    for i in range(9):
        if i%3 == 0 and i != 0:
            canvas.create_line(i*window, 0, i*window, 9*window, width=5)
            canvas.create_line(0, i*window, 9*window, i*window, width=5)
        else:
            canvas.create_line(i*window, 0, i*window, 9*window, width=2)
            canvas.create_line(0, i*window, 9*window, i*window, width=2)


def drawNumbers(row, y):
    global window
    for i in range(9):
        canvas.create_text(i*window + 10, y*window + 5, text=row[i], font=('Helvetica', window-20), anchor=tk.NW)


window = 50
canvas = tk.Canvas(root, height=9*window, width=9*window, bg = 'white')
canvas.pack()
drawGrid()

count_row = 0
inputParser(fr,sudoku)
if sudokuSolver():
    for row in sudoku:
        print(' '.join(map(str, row)))
        drawNumbers(row, count_row)
        count_row += 1

fr.close()
root.mainloop()