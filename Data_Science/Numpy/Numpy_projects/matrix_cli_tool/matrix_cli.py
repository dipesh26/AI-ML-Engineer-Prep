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
        path = input(f"\nEnter the path of matrix {name}: ").strip()
        if not path:
            print("\n❌ Path can't be empty.")
            continue
        try:
            matrix = np.loadtxt(path, delimiter=',')
            return matrix
        except Exception as e:
            print(f"\n❌ Invalid File Path or File Error: {e}")          

def get_two_matrices():
    A = input_matrix("A")
    B = input_matrix("B")
    if A is None or B is None:
        return None, None    
    print("\n✅ Matrices loaded successfully!")
    return A, B

def get_path():
    A = load_matrix("A")
    B = load_matrix("B")
    if A is None or B is None:
        return None, None
    print("\n✅ Matrices loaded successfully!")        
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

def load_single_matrix(option):
    if option == 'm':
        A = input_matrix("A")
    elif option == 'p':
        A = load_matrix("A")
    else:
        print("❗Invalid input source option.")
        return None
    return A

def display_result(A, B, Oops, name):
    print(f"\n📌 Matrix Operation: {name}")
    print(f"\n📥 Matrix A:\n{A}")
    print(f"\n📥 Matrix B:\n{B}")
    print(f"\n🔷 {name} of Matrix A & B:\n{Oops}")
    print(f"{"-"*20}")

def display_single_result(A, Oops, name):
    print(f"\n📌 Matrix Operation: {name}")
    print(f"\nV📥 Matrix A:\n{A}")
    print(f"\n✅ Result:")    
    print(f"\n🔷 {name} of Matrix A:\n{Oops}")

def add_matrix(option):
    name = "Addition"
    A, B = get_matrices(option)
    if A.shape == B.shape:
        add = np.add(A, B)
        display_result(A, B, add, name)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def sub_matrix(option):
    name = "Subtraction"
    A, B = get_matrices(option)
    if A.shape == B.shape:
        sub = np.subtract(A, B)
        display_result(A, B, sub, name)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def multi_matrix(option):
    name = "Multiplication"
    A, B = get_matrices(option)
    if A.shape[1] == B.shape[0]:
        multi = A @ B
        display_result(A, B, multi, name)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def transpose(option):
    name = "Transpose"
    A = load_single_matrix(option)
    trans = A.T
    display_single_result(A, trans, name)

def determinant(option):
    name = "Determinant"
    A = load_single_matrix(option)
    if A.shape[0] != A.shape[1]:
        print("\n❗Matrix must be square for this operation.")
    else:
        deter = np.linalg.det(A)
        display_single_result(A, deter, name)

def inverse(option):
    name = "Inverse"
    A = load_single_matrix(option)
    if A.shape[0] != A.shape[1]:
        print("\n❗Matrix must be square for this operation.")
    else:
        try:
            inverse = np.linalg.inv(A)                        
            display_single_result(A, inverse, name)
        except np.linalg.LinAlgError:
            print("\n❌ Matrix is singular and cannot be inverted.")        

def main():
    print("\n","="*10,"🧮 Matrix Operations CLI Tool 🧮","="*10)
    while True:
        print("\n📘 Available Operations:")
        print("  [1] ➕  Add\n  [2] ➖  Subtract\n  [3] ✖️  Multiply\n  [4] 🔁  Transpose\n  [5] 🧮  Determinant\n  [6] 🔄  Inverse\n  [7] ❌  Exit\n")
        try:
            choice = int(input("Select an Operation ⬆️  : ").strip())
            print("\n🔹 Select Input Method:")
            print("   [m] ⌨️  Manually\n   [p] 📂  From File Path\n")
            option = str(input("choose the Option ⬆️  : ").strip()).lower()
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