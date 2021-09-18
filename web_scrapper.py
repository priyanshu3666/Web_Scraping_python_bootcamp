from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests,bs4
import re
def top_movie(url,top_num):
    request_ = requests.get(url)
    soup =bs4.BeautifulSoup(request_.text,'lxml')
    movie_id_list =[]
    for num in range(top_num):
        class_content  = soup.select('.titleColumn')[num]('a')[0]['href']
        movie_id_list.append((str(class_content).split("/"))[2])
    return movie_id_list



def get_synopsis(movies_id):
    base_url = "https://www.imdb.com/title/"
    synopsis_list = []
    for movie_id in movies_id:
        request_ = requests.get(base_url+movie_id)
        soup = bs4.BeautifulSoup(request_.text,'lxml')
        synopsis = soup.select('.ipc-html-content.ipc-html-content--base')[1]
        synopsis_list.append(synopsis.getText())
    return synopsis_list

movie_id_list = top_movie("https://www.imdb.com/chart/top/",1)
synopsis_list = get_synopsis(movie_id_list)



