# 📚 Book Data Scraper (Books to Scrape)

This project is a basic web scraping script built using **Python**, **BeautifulSoup**, and **Pandas**. It extracts book data such as title, price, and availability (if needed) from the [Books to Scrape](https://books.toscrape.com) website — a popular site designed for practicing web scraping.

---

## 🔍 What It Does

The script scrapes the homepage of the Books to Scrape site and collects:

- 📖 **Title** of each book  
- 💰 **Price** listed  
- 🛒 **Stock status** *(currently not extracted but placeholder is included in code for future use)*

The data is saved in a CSV file named `practice-book-data.csv`.

---

## 🛠 Technologies Used

- `requests` — Send HTTP requests to the website  
- `BeautifulSoup` — Parse and extract data from HTML  
- `pandas` — Structure the data and export it to CSV

---

## 🧾 How to Use

1. **Download** the file from this repository.

2. **Open** the file (`web_scarping_ecom.py`) in your favorite code editor (e.g., VS Code, PyCharm).

3. **Install dependencies** (if not already installed):

   ```bash
   pip install requests beautifulsoup4 pandas
   ```
4. **Run the script**:

   ```bash
   python web_scarping_ecom.py
   ```
5. **Check the output**:
   
    A file named practice-book-data.csv will be generated in the same folder with the scraped book data.

## 🧪 Sample Output

  | Title                 | Price   |
  |-----------------------|---------|
  | A Light in the Attic  | £51.77  |
  | Tipping the Velvet    | £53.74  |
  | Soumission            | £50.10  |

---

## 📌 Note

- This project is **for educational and practice purposes only**.
- The site [Books to Scrape](https://books.toscrape.com) is created specifically for web scraping practice.

---

## 🙋‍♂️ Author

**Dipesh Mahajan**  
Feel free to connect or ask questions!

