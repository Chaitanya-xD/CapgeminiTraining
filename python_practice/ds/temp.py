from bs4 import BeautifulSoup as bs
import requests

def main(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    response = requests.get(url,headers=header)
    soup = bs(response.content,'html.parser')

    # print(soup)

    movies = soup.find_all('h3',class_='ipc-title__text')

    movies = movies[0:5]

    # print(movies)

    movies_titles = [movie.get_text(strip=True) for movie in movies]
    
    ans = []  

    for title in movies_titles:
        ans.append(title)

    print(*ans,sep='\n')

main("https://www.imdb.com/search/title/?title_type=feature&release_date=2011-01-01,2011-12-31")