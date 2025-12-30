# 📊 Web Scraping & Data Analysis Project  
**CodeAlpha – Data Analytics Internship**

This project demonstrates a complete data analytics workflow using Python, including **web scraping, exploratory data analysis (EDA), and data visualization**.  
All tasks were completed as part of the **CodeAlpha Data Analytics Internship**.

---

## 🧩 Project Structure
Web_Scraping_Project/ │ ├── data/ │   └── books_large_data.csv │ ├── visuals/ │   ├── price_distribution.png │   ├── rating_distribution.png │   ├── price_vs_rating.png │   └── top_10_expensive_books.png │ ├── scraper.py ├── eda.py ├── visualization.py ├── eda_report.txt ├── requirements.txt └── README.md
---

## ✅ Task 1: Web Scraping
**Objective:**  
To collect book-related data from a website and store it in a structured format.

**Description:**  
- Implemented web scraping using Python
- Extracted book details such as:
  - Book Title  
  - Price  
  - Rating  
- Cleaned and organized the data
- Stored the scraped data into a CSV file for further analysis

**Output File:**  
- `data/books_large_data.csv`

**Script Used:**  
- `scraper.py`

---

## ✅ Task 2: Exploratory Data Analysis (EDA)
**Objective:**  
To analyze and understand the scraped dataset and identify useful patterns.

**Description:**  
- Loaded and inspected the dataset
- Handled missing and invalid values
- Performed basic statistical analysis
- Studied price and rating distributions
- Generated textual insights based on observations

**Output Files:**  
- `eda_report.txt`

**Script Used:**  
- `eda.py`

---

## ✅ Task 3: Data Visualization
**Objective:**  
To visually represent insights from the dataset for better understanding.

**Visualizations Created:**
1. Price Distribution of Books  
2. Rating Distribution  
3. Price vs Rating Relationship  
4. Top 10 Most Expensive Books  

**Tools Used:**  
- Pandas  
- Matplotlib  

**Output Folder:**  
- `visuals/` (contains all generated plots)

**Script Used:**  
- `visualization.py`

---

## 🛠 Technologies & Libraries Used
- Python
- Pandas
- Matplotlib
- BeautifulSoup
- Requests

Install all required libraries using:
```bash
pip install -r requirements.txt
🚀 How to Run the Project
Run the scripts in the following order:
python scraper.py
python eda.py
python visualization.py
🎯 Key Learnings
Web scraping using Python
Data cleaning and preprocessing
Exploratory data analysis techniques
Data visualization using Matplotlib
Git and GitHub version control
📌 Internship Information
Internship: CodeAlpha – Data Analytics
Tasks Completed: Task 1, Task 2, Task 3
Project Status: ✅ Successfully Completed
