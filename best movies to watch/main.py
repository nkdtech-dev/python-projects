import requests
from bs4 import BeautifulSoup


empire_movies_url = "https://www.imdb.com/search/title/?groups=top_100"
data = requests.get(empire_movies_url).text

soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all("h3", class_="lister-item-header")

movie_anchor = []
position = []
rating = []
rating += soup.find_all("div", class_="inline-block ratings-imdb-rating")
for movie in movies:
    movie_anchor += movie.find("a")
    position += movie.find("span", class_="lister-item-index unbold text-primary")

top_movies = [item.getText() for item in movie_anchor]
position_rank = [int(item.getText().split(".")[0]) for item in position]
ranking = [float(item.find("strong").getText()) for item in rating]
most_rated = ranking.index(max(ranking))
for number in position_rank:
    film = top_movies[number-1]
    state = ranking[number-1]
    with open(file="top 50 films of all time.txt", mode="a") as films:
        films.write(f"{number}   |{film}  |{state}  \n")
