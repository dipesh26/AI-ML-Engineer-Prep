import numpy as np

board = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def solve_board(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            
            if solve_board(board):
                return True
            
            board[row][col] = 0
            
    return False

def is_valid(board, num, row, col):
    if num in board[row]:
        return False
    
    if num in board[:, col]:
        return False
    
    start_row = row - row % 3
    start_col = col - col % 3
    box = board[start_row:start_row+3, start_col:start_col+3]
    if num in box:
        return False
    
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return(i, j)
    return None

def main():
    print(f"\n{"="*10} Sudoku Solver {"="*10}\n")

    print("[0] For Empty Cell")
    for row in range(1, 10):
        user_input = int(input(f"Enter the {row} row: ").strip())
        
    
    print(f"Original Puzzle:\n{"-"*16}\n")
    print_board(board)
    
    if solve_board(board): 
        print(f"\n✅ Solved Sudoku Puzzle:\n{"-"*16}\n")
        print_board(board)
    else:
        print("\n❌ No solution exists.")

if __name__ == "__main__":
    main()