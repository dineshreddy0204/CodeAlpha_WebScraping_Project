import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("article", class_="product_pod")

def scrape_all_books():
    all_books = []

    # PAGE 1 (different URL)
    print("Scraping page 1...")
    books = scrape_page("http://books.toscrape.com/")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("£", "")
        rating = book.p["class"][1]
        all_books.append([title, price, rating, 1])

    # PAGE 2–50
    for page in range(2, 51):
        print(f"Scraping page {page}...")
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        books = scrape_page(url)

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.replace("£", "")
            rating = book.p["class"][1]
            all_books.append([title, price, rating, page])

        time.sleep(1)

    df = pd.DataFrame(all_books, columns=["Book Title", "Price (£)", "Rating", "Page"])

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/books_large_data.csv", index=False)

    print("✅ SCRAPING DONE")
    print("📊 Total rows:", len(df))

if __name__ == "__main__":
    scrape_all_books()
