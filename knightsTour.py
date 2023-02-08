def is_valid_move(x, y, N, sol):
    return (x >= 0 and x < N and
            y >= 0 and y < N and
            sol[x][y] == -1)

def print_solution(sol):
    for i in range(len(sol)):
        for j in range(len(sol)):
            print(sol[i][j], end=" ")
        print()

def solveKT(N):
    sol = [[-1 for x in range(N)] for y in range(N)]
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]

    sol[0][0] = 0
    pos = 1
    if not solveKTUtil(0, 0, pos, sol, xMove, yMove):
        print("Solution does not exist")
        return False

    print_solution(sol)
    return True

def solveKTUtil(x, y, pos, sol, xMove, yMove):
    if pos == N ** 2:
        return True

    for i in range(8):
        x_ = x + xMove[i]
        y_ = y + yMove[i]
        if is_valid_move(x_, y_, N, sol):
            sol[x_][y_] = pos
            if solveKTUtil(x_, y_, pos + 1, sol, xMove, yMove):
                return True
            sol[x_][y_] = -1
    return False

# Driver code to test above functions
N = 8
solveKT(N)

