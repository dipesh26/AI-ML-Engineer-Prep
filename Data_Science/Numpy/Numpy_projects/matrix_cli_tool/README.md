# 🧮 Matrix Operations CLI Tool

A command-line calculator built with **Python + NumPy** that allows you to perform various matrix operations interactively.

---

## 📌 Features

- Enter matrices manually or from a `.txt` file
- Perform key matrix operations:
  - ➕ Add
  - ➖ Subtract
  - ✖️ Multiply
  - 🖁 Transpose
  - 🧮 Determinant
  - 🔄 Inverse
- Display matrices side-by-side with dimensions
- Clean and user-friendly interface with emoji prompts
- Proper error handling and validation

---

## 🚀 How to Run

1. **Clone this repo** (or download manually):

   ```bash
   git clone https://github.com/yourusername/matrix-cli-tool.git
   cd matrix-cli-tool
   ```

2. **Install requirements**:

   ```bash
   pip install numpy
   ```

3. **Run the tool**:

   ```bash
   python matrix_cli.py
   ```

---

## 🦾 Input Format (if using file)

Create a `.txt` file with two matrices like this:

```
Matrix A:
1 2 3
4 5 6

Matrix B:
7 8 9
10 11 12
```

---

## 📷 Example Output

```
📥 Matrix A              📥 Matrix B
   (2, 3)                  (2, 3)
[1 2 3]                [7 8 9]
[4 5 6]                [10 11 12]

📘 Available Operations:
  [1] ➕  Add
  [2] ➖  Subtract
  [3] ✖️  Multiply
  [4] 🖁  Transpose
  [5] 🧮  Determinant
  [6] 🔄  Inverse
  [7] 📥 New Matrices
  [8] ❌  Exit
```

---

## 📂 Project Structure

```
matrix_cli_tool/
│
├── matrix_cli.py      # Main script
├── sample_input.txt   # Optional: file input format example
└── README.md          # Project info
```

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)

---

## 🧑‍💻 Author

**Dipesh Mahajan**\
Passionate AI/ML enthusiast building practical tools with Python.\
📢 Contact: +91 6263807893\
📁 [Portfolio](https://dipesh-ml.vercel.app/)

---

## 📜 License

Free to use under MIT License.

