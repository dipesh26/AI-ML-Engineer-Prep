import numpy as np

def input_matrix(name):
    while True:
        user_input = input(f"\nEnter dimensions of matrix {name} (rows cols): ").strip()
        if not user_input:
            print("\n❌ Rows & columns can't be empty.")
            continue
        try:
            rows, cols = map(int, user_input.split())
            break
        except ValueError:
            print("\n❌ Invalid Input! Please enter two integers like: 2 3")
        
    while True:
        user_input = input(f"Enter matrix {name} elements (row-wise): ").strip()
        if not user_input:
            print("\n❌ Elements can't be empty.\n")
            continue
        try:
            elements = list(map(float, user_input.split()))
            if len(elements) != rows * cols:
                print("\n❌ Element count does not match matrix dimensions.\n")
                continue
            else:
                return np.array(elements).reshape(rows, cols)
        except ValueError:
            print("\n❌ Invalid Input! Please enter valid numbers.\n")

def load_matrix(name):
    while True:
        path = input(f"\nEnter the path of matrix {name} : ").strip()
        if not path:
            print("\n❌ Path can't be empty.")
            continue
        try:
            matrix = np.loadtxt(path)
            return matrix
        except Exception as e:
            print(f"\n❌ Invalid File Path or File Error: {e}")          

def get_two_matrices():
    A = input_matrix("A")
    B = input_matrix("B")
    if A is None or B is None:
        return None, None    
    return A, B

def get_path():
    A = load_matrix("A")
    B = load_matrix("B")
    if A is None or B is None:
        return None, None    
    return A, B

def get_matrices(option):
    if option == 'm':
        A, B = get_two_matrices()
    elif option == 'p':
        A, B = get_path()
    else:
        print("❗Invalid input source option.")
        return None, None
    return A, B

def display_result(A, B, add):
    print(f"\nMatrix A:\n{A}\n")
    print(f"\nMatrix B:\n{B}\n")
    print(f"\nResult:\n{add}")

def add_matrix(option):
    A, B = get_matrices(option)
    if A.shape == B.shape:
        add = np.add(A, B)
        display_result(A, B, add)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def sub_matrix(option):
    A, B = get_two_matrices()
    if A.shape == B.shape:
        sub = np.subtract(A, B)
        print(f"\nResult:\n{sub}")
    else:
        print("\n❗Matrices must be of the same dimensions.")

def multi_matrix(option):
    A, B = get_two_matrices()
    if A.shape == B.shape:
        multi = A @ B
        print(f"\nResult:\n{multi}")
    else:
        print("\n❗Matrices must be of the same dimensions.")

def transpose(option):
    A = input_matrix("A")
    print(f"\nResult:\n{A.T}")

def determinant(option):
    A = input_matrix("A")
    if A.shape[0] != A.shape[1]:
        print("\n❗Matrix must be square for this operation.")
    else:
        deter = np.linalg.det(A)
        print(f"\nResult:\n{deter}")

def inverse(option):
    A = input_matrix("A")
    if A.shape[0] != A.shape[1]:
        print("\n❗Matrix must be square for this operation.")
    else:
        try:
            inverse = np.linalg.inv(A)                        
            print(f"\nResult:\n{inverse}")
        except np.linalg.LinAlgError:
            print("\n❌ Matrix is singular and cannot be inverted.")        

def main():
    print("\n========== 🧮 Matrix Operations CLI Tool 🧮 ==========")
    while True:
        print("\n[1] Add [2] Subtract [3] Multiply [4] Transpose [5] Determinant [6] Inverse [7] Exit")
        try:
            choice = int(input("Choose an operation☝️ : ").strip())
            print("\n[m] Manually [p] Path")
            option = str(input("choose the Option☝️ : ").strip()).lower()
            if option not in ['m', 'p']:
                print("❗Choose Valid option!")
                continue
            match choice:
                case 1: add_matrix(option)
                case 2: sub_matrix(option)
                case 3: multi_matrix(option)
                case 4: transpose(option)
                case 5: determinant(option)
                case 6: inverse(option)
                case 7:
                    print("\n===== Thanks for Visiting. =====\n")
                    break
                case _: print("\n❌ Invalid Choice!")
        except ValueError:
            print("\n❌ Enter only Numbers From [1] - [6]")

if __name__ == "__main__":
    main()