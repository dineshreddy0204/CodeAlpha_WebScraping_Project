# 📊 CodeAlpha Internship – Data Analytics Project

This repository contains my internship project for **CodeAlpha – Data Analytics Domain**.  
The project successfully completes **Task 1 (Web Scraping)** and **Task 2 (Exploratory Data Analysis – EDA)** using Python.

---

## ✅ Tasks Completed

### 🔹 Task 1: Web Scraping
- Extracted data from a public website using Python
- Collected structured data (Book Title, Price, Rating, Page Number)
- Stored the scraped data into a CSV file for analysis

**Technologies Used:**
- Python
- Requests
- BeautifulSoup
- Pandas

**Output File:**
- `data/books_large_data.csv` (1000 records)

**Script:**
- `scraper.py`

---

### 🔹 Task 2: Exploratory Data Analysis (EDA)
- Loaded the scraped dataset
- Explored dataset structure and data types
- Generated summary statistics
- Identified rating distribution
- Found top expensive books
- Created a detailed EDA report

**Analysis Performed:**
- Total records count
- Unique values
- Mean, min, max statistics
- Rating frequency analysis
- Data quality inspection

**Scripts & Output:**
- `eda.py`
- `eda_report.txt`

---

## 📁 Project Structure
CodeAlpha_WebScraping_Project/ │ ├── data/ │   └── books_large_data.csv │ ├── scraper.py          # Task 1 – Web Scraping ├── eda.py              # Task 2 – Exploratory Data Analysis ├── eda_report.txt      # EDA results │ ├── requirements.txt ├── README.md └── .gitignore
---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
## Run Web Scraping(Task 1)
python scraper.py
## Run Exploratory Data Analysis(Task 2)
python eda.py