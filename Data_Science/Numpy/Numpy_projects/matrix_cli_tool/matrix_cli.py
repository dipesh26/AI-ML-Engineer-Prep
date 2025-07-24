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

def display_result(A, B, Oops, name):
    print(f"\n📌 Matrix Operation: {name}")
    print(f"\n📥 Matrix A:\n{A}")
    print(f"\n📥 Matrix B:\n{B}")
    print(f"\n🔷 {name} of Matrix A & B:\n{Oops}")
    print(f"\n{"-"*30}")

def display_single_result(A, B, Oops_1, Oops_2, name):
    print(f"\n📌 Matrix Operation: {name}")
    print(f"\n📥 Matrix A:\n{A}")
    print(f"\n📥 Matrix B:\n{B}")   
    print(f"\n🔷 {name} of Matrix A:\n{Oops_1}")
    print(f"\n🔷 {name} of Matrix B:\n{Oops_2}")
    print(f"\n{"-"*30}")

def add_matrix(A, B):
    name = "Addition"
    if A.shape == B.shape:
        add = np.add(A, B)
        display_result(A, B, add, name)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def sub_matrix(A, B):
    name = "Subtraction"
    if A.shape == B.shape:
        sub = np.subtract(A, B)
        display_result(A, B, sub, name)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def multi_matrix(A, B):
    name = "Multiplication"
    if A.shape[1] == B.shape[0]:
        multi = A @ B
        display_result(A, B, multi, name)
    else:
        print("\n❗Matrices must be of the same dimensions.")

def transpose(A, B):
    name = "Transpose"
    trans_A = A.T
    trans_B = B.T
    display_single_result(A, B, trans_A, trans_B, name)

def determinant(A, B):
    name = "Determinant"
    if A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        print("\n❗Both matrices must be square for this operation.")
        return
    else:
        deter_A = np.linalg.det(A)
        deter_B = np.linalg.det(B)
        display_single_result(A, B, deter_A, deter_B, name)

def inverse(A, B):
    name = "Inverse"
    if A.shape[0] != A.shape[1] or B.shape[0] != B.shape[1]:
        print("\n❗Both matrices must be square for this operation.")
        return
    else:
        try:
            inverse_A = np.linalg.inv(A)                        
        except np.linalg.LinAlgError:
            inverse_A = "❌ Matrix A is singular"  

        try:
            inverse_B = np.linalg.inv(B)                        
        except np.linalg.LinAlgError:
            inverse_A = "❌ Matrix B is singular"
        
        display_single_result(A, B, inverse_A, inverse_B, name)

def main():
    print("\n","="*10,"🧮 Matrix Operations CLI Tool 🧮","="*10)
    while True:
        print("\n🔹 Select Input Method:")
        print("   [m] ⌨️  Manually\n   [p] 📂  From File Path\n")
        option = str(input("choose the Option ⬆️  : ").strip()).lower()
        if option == 'm':
            A, B = get_two_matrices()
        elif option == 'p':
            A, B = get_path()
        else:
            print("❗Invalid input source option.")
        if A is None or B is None:    
            continue

        print("\n📘 Available Operations:")
        print("  [1] ➕  Add\n  [2] ➖  Subtract\n  [3] ✖️  Multiply\n  [4] 🔁  Transpose\n  [5] 🧮  Determinant\n  [6] 🔄  Inverse\n  [7] ❌  Exit\n")
        try:
            choice = int(input("Select an Operation ⬆️  : ").strip())
            print("\n🔹 Select Input Method:")
            match choice:
                case 1: add_matrix(A, B)
                case 2: sub_matrix(A, B)
                case 3: multi_matrix(A, B)
                case 4: transpose(A, B)
                case 5: determinant(A, B)
                case 6: inverse(A, B)
                case 7:
                    print("\n===== Thanks for Visiting. =====\n")
                    break
                case _: print("\n❌ Invalid Choice!")
        except ValueError:
            print("\n❌ Enter only Numbers From [1] - [6]")

if __name__ == "__main__":
    main()