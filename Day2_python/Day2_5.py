import requests
from bs4 import BeautifulSoup

# url = 'http://jspstudy.co.kr'
# movie = requests.get(url)
# print(movie.text)


# url = 'http://finance.naver.com/'

# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")

# main_section = soup.find("div",{"class": "news_area"})
# top_news_ul = main_section.find("ul")

# top_news = top_news_ul.find_all("span")

# for article in top_news:
#     print(article.get_text())


url = 'https://www.nike.com/kr/t/gt-%EC%A0%90%ED%94%84-2-ep-%EB%82%A8%EC%84%B1-%EB%86%8D%EA%B5%AC%ED%99%94-FoAMPgqw/DJ9432-300'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

main_section = soup.find("div",{"class": "pr2-sm css-1ou6bb2"})
top_news_ul = main_section.find("h1")

#top_news = top_news_ul.find_all("span")

print(soup)
# for article in top_news_ul:
#     print(article.get_text()) 