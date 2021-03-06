import json
import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime
import time


def get_first_news():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

    }

    url = "https://www.securitylab.ru/news/"
    r = requests.get(url, headers=headers)

    soup = BS(r.text, "lxml")
    articles_cards = soup.find_all("a", class_="article-card")

    news_dict = {}
    for article in articles_cards:
        article_title = article.find("h2", class_="article-card-title").text.strip()
        article_desc = article.find("p").text.strip()
        article_url = f'https://www.securitylab.ru{article.get("href")}'

        article_date_time = article.find("time").get("datetime")
        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]



        news_dict[article_id] = {
            "article_date_timestamp": article_date_timestamp,
            "article_title": article_title,
            "article_url": article_url,
            "article_desc": article_desc
        }

    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)




def main():
    get_first_news()


if __name__ == '_main_':
    main()





# import requests
# from bs4 import BeautifulSoup as BS
#
# URL = "https://www.securitylab.ru/"
#
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
# }
#
# def get_html(url, params=''):
#     req = requests.get(url, headers=HEADERS, params=params)
#     return req
#
# def get_data(html):
#     soup = BS(html, "html.parser")
#     items = soup.find_all('div', class_="article-card inline-card ")
#     news = []
#     for item in items:
#         news.append(
#             {
#
#                 article_title = article.find("h2", class_="article-card-title").text.strip(),
#                     article_desc = article.find("p").text.strip()
#                     article_url = f'https://www.securitylab.ru{article.get("href")}
#                 # "time": item.find('time', class_="article-card-details"),
#                 # article_title = article.find("h2", class_="article-card-title").text.strip(),
#                 # article_desc = article.find("p").text.strip(),
#                 # article_url = f'https://www.securitylab.ru{article.get("href")},
#                 # "title": item.find("h2", class_="article-card-title").text.strip(),
#                 # 'link': URL + item.find("p").text.strip(),
#                 # 'image': URL + item.find('div', class_='image-box').find('img').get('src')
#             }
#         )
#     return news
#
# def parser():
#     html = get_html(URL)
#     if html.status_code == 200:
#         news = []
#         for page in range (0, 1):
#             html = get_html(f"{URL}latest/{page}")
#             news.extend(get_data(html.text))
#             return news
#     else:
#         raise Exception("Error in parser!")
#
# print(parser())
#
# article_title = article.find("h2", class_="article-card-title").text.strip()
#         article_desc = article.find("p").text.strip()
#         article_url = f'https://www.securitylab.ru{article.get("href")}