from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_100_webpage = response.text

soup = BeautifulSoup(top_100_webpage, "html.parser")
movie_title = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movie_title]
movies = movie_titles[::-1]

with open("Top-100-Movies.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")









# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
#
# articles = soup.find_all(name="span", class_="titleline")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     article_text = article_tag.getText()
#     article_texts.append(article_text)
#     article_link = article_tag.get("href")
#     article_links.append(article_link)
#
# article_link_test = [link.getText() for link in articles.f("a",)]
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find(name="span", class_="score")]




























# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find_all(name="h3", class_="heading")
# print(section_heading) #add .getText at end to get text
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)