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
