import sys
sys.setrecursionlimit(10**6)

board = [[0, 0, 0, 0, 2, 0, 6, 0, 7],
        [3, 0, 2, 6, 0, 0, 0, 0, 9],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 5, 2],
        [0, 0, 7, 0, 0, 0, 8, 0, 0],
        [8, 5, 0, 0, 3, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [1, 0, 0, 0, 0, 8, 2, 0, 3],
        [7, 0, 3, 0, 5, 0, 0, 0, 0]]

def find_empty(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)

def valid_number(grid, num, pos):

    for row in range(len(grid[0])):
        if grid[pos[0]][row] == num and pos[1] != row:
            return False

    for col in range(len(grid)):    
        if grid[col][pos[1]] == num and pos[0] != col:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    
    return True

def prinf_board(grid):
    for row in range(len(grid)):
        if row%3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")

        for col in range(len(grid[0])):
            if col%3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(grid[row][col])
            else:
                print(str(grid[row][col]) + " ", end="") 

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
    
    for num in range(1, 10):
        if valid_number(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True
            
            grid[row][col] = 0

    return False


prinf_board(board)
solve(board)
print("---------------------------")
prinf_board(board)