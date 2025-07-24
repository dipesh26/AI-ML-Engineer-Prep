def add_matrix():
    pass

def subtract_matrix():
    pass

def multiply_matrix():
    pass

def transpose_matrix():
    pass

def determinant_matrix():
    pass

def inverse_matrix():
    pass

def main():
    print("\n========== Welcome to the Matrix Operations CLI Tool! ==========")
    while True:
        print("\n[1] Add [2] Subtract [3] Multiply [4] Transpose [5] Determinant [6] Inverse [7] Exit")
        try:
            choice = int(input("Choose an operation☝️ : ").strip())
            match choice:
                case 1:
                    add_matrix()
                case 2:
                    subtract_matrix()
                case 3:
                    multiply_matrix()
                case 4:
                    transpose_matrix()
                case 5:
                    determinant_matrix()
                case 6:
                    inverse_matrix()
                case 7:
                    print("\n===== Thanks for Visiting. =====\n")
                    break
                case _:
                    print("❌ Invalid Choice!")
        except ValueError:
            print("❌ Invalid Input!")

if __name__ == "__main__":
    main()