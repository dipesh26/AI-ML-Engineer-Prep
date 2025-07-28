import numpy as np

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return(i, j)
    return None

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

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def input_sudoku():
    board = []
    print("\n🔹 [0] For Empty Cell\n")
    
    for i in range(9):
        while True:
            user_input = input(f"Enter the {i+1} row: ").strip()
            if not user_input:
                print("\n❗ Row can't be empty.\n")
                continue
            try:
                row = list(map(int, user_input.split()))
                if len(row) != 9:
                    print("\n❗ Each row must have 9 numbers.\n")
                    continue
                board.append(row)
                break
            except ValueError:
                print("\n❗ Please enter only numbers.\n")
    return np.array(board)

def main():
    print("\n" + "="*10 + " Sudoku Solver " + "="*10)
    
    while True:
        print("\n"+"-"*40)
        print("🔸 Type [own] to enter your own puzzle.")
        print("🔸 Type [demo] to use a sample board.")
        print("-"*40)
        
        choice = input("\nChoose the Option ⬆️  : ").strip().lower()
        if not choice:
            print("\n❗ Option can't be empty.")
            continue
        elif choice == "demo":
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
            break
        elif choice == "own":
            board = input_sudoku()
            break
        else:
            print("\n❌ Invalid option. Please type 'own' or 'demo'.")
            continue
    
    print(f"\n{"➖"*15}\n")
    print(f"Original Puzzle:\n{"-"*16}\n")
    print_board(board)
    
    if solve_board(board): 
        print(f"\n✅ Solved Sudoku Puzzle:\n{"-"*16}\n")
        print_board(board)
        print()
    else:
        print("\n❌ No solution exists.")

if __name__ == "__main__":
    main()