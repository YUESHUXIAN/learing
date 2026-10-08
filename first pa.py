import requests
from bs4 import BeautifulSoup
import csv
import json



def scrape_books():
    books=[]
    rating_map = {
        'One': 2,
        'Two': 4,
        'Three': 6,
        'Four': 8,
        'Five': 10
        }
#作用：伪装成浏览器。如果没有：网站可能认为：这是机器人访问,然后拒绝
    headers = { 'User-Agent': 'Mozilla/5.0'}
    for page in range(1, 4):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response=requests.get(url, headers=headers )
        response.encoding="utf-8"
        soup = BeautifulSoup(  response.text,  "html.parser")
        book_list = soup.select("article.product_pod")
        for book in book_list:
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text.strip()
            rating_class = book.select_one(".star-rating")["class"]
            rating_name = rating_class[1]
            rating = rating_map[rating_name]
            books.append({
                "title":title,
                "rating":rating,
                "price":price
            })
            return books

def save_csv(books):
    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "rating", "price"])
        writer.writeheader()
        writer.writerows(books)

def merge_movies(books):
    try:
        with open("movies.json", "r", encoding="utf-8") as f:
            old_movies = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        old_movies = []

    # 把新的数据追加进去
    old_movies.extend(books)

    # 写回 JSON
    with open("movies.json", "w", encoding="utf-8") as f:
        json.dump(
            old_movies,
            f,
            ensure_ascii=False, # 中文不转义，直接保存中文
            indent=4    # 格式化缩进4空格，方便阅读
        )

if __name__ == "__main__":  #只有直接运行这个 py 文件的时候，下面这一大段代码才会执行

    books = scrape_books()

    print("一共爬取：", len(books), "本书")

    # 保存 CSV
    save_csv(books)
    print("CSV 保存成功：scraped_movies.csv")

    # 合并 JSON
    merge_movies(books)
    print("JSON 合并成功：movies.json")