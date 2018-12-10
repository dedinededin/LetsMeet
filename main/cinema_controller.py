from bs4 import BeautifulSoup as soup

import requests


def get_films():
    url = "http://www.beyazperde.com/filmler/vizyondakiler/en-iyi-filmleri/kullanici-puani/"

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    r = requests.get(url, headers=headers)
    page_html = r.text

    page_soup = soup(page_html, "html.parser")

    films_data = page_soup.findAll("li", {"class": "mdl"})
    films = []
    id = 0;
    for film_data in films_data:
        name = film_data.find("a").text

        img = film_data.find('img')
        raw_img = str(img)
        start = raw_img.find("src=")
        end = raw_img.find('"', start + 10)
        img_url = raw_img[start + 5:end]

        date = film_data.find("span", {"class": "date"}).text
        description = film_data.find("div", {"class": "content-txt"}).text
        film = {'id': id, 'name': name, 'img': img_url, 'date': date, 'description': description}
        films.append(film)
        id = id + 1
    return films
