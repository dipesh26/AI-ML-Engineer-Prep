# 🧹 NumPy Data Cleaner & Normalizer

A simple and interactive Python CLI tool that helps **clean**, **normalize**, and **export** tabular numeric data using **NumPy**.  
It reads a `.csv` file, handles missing values, normalizes the data, and allows exporting or viewing the original cleaned data.

---

## 📦 Features

- ✅ Load and parse CSV file with headers
- ✅ Automatically detect and clean missing values (`NaN`) using column-wise mean
- ✅ Normalize data between 0 and 1
- ✅ Denormalize back to original values
- ✅ View data in tabular format with headers
- ✅ Export cleaned + normalized data to a new CSV
- ✅ CLI menu with multiple actions

---

## 📁 Input Format

- Format: `.csv` file
- First line: Headers
- Data: Numeric only
- Missing values: Leave blank (e.g. `5.1,,7.2`)

---

## 📥 How to Download

Clone this repository:

```bash
git clone https://github.com/dipeshml/numpy-data-cleaner.git
cd numpy-data-cleaner
```

Or download the ZIP and extract it manually.

---

## ⚙️ Requirements

- Python 3.6+
- NumPy

Install the required packages using:

```bash
pip install numpy
```

---

## ▶️ How to Run

Once inside the project folder, run the script using:

```bash
python numpy_data_cleaner.py
```

Then follow the on-screen instructions in your terminal:

```
========== Numpy Data Cleaner ==========
Enter the File name: sample.csv

✅ File loaded...
✅ Missing values cleaned...
✅ Data Normalized...

Normalized & Cleaned Data:
--------------------------
Age     Height  Weight
0.25    0.75    0.44
0.50    0.50    0.61
...

---------------------------------
🔸[y] See Original Cleaned Data
🔸[s] Save to .csv file
🔸[n] New
🔸[e] To Exit
---------------------------------
Select the Options ⬆️  :
```

## 📤 Output

A cleaned and normalized file will be saved as:

```bash
Normalized & cleaned data.csv
```

---

## 🙋‍♂️ Author

**Dipesh Mahajan**\
📢 Contact: +91 6263807893\
📁 [Portfolio](https://dipesh-ml.vercel.app/)

---

## 📜 License

This project is free and open-source. Use it for learning, personal, or educational purposes.

---