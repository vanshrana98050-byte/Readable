board = [list(input()) for _ in range(9)]

def valid(r, c, ch):

    for i in range(9):
        if board[r][i] == ch:
            return False

        if board[i][c] == ch:
            return False

    sr = (r // 3) * 3
    sc = (c // 3) * 3

    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == ch:
                return False

    return True

def solve():

    for i in range(9):
        for j in range(9):

            if board[i][j] == ".":

                for ch in "123456789":

                    if valid(i, j, ch):
                        board[i][j] = ch

                        if solve():
                            return True

                        board[i][j] = "."

                return False

    return True

solve()

for row in board:
    print(" ".join(row))