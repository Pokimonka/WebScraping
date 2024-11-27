import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def get_all_articles(resp):
    soup = bs4.BeautifulSoup(resp.text, features='lxml')
    articles_list = soup.select_one('div.tm-articles-list')
    all_articles = articles_list.select('article.tm-articles-list__item')
    return all_articles

def check_word(data):
    for keyw in KEYWORDS:
        if keyw in data.text or keyw.title() in data.text:
            return True

def get_all_articles_where_keywords(all_articles):
    for article in all_articles:
        link = 'https://habr.com' + article.select_one('a.tm-title__link')['href']
        article_response = requests.get(link)
        article_soup = bs4.BeautifulSoup(article_response.text, features='lxml')
        header = article_soup.select_one('h1').text
        time = article_soup.select_one('time')['datetime']
        all_data = article_soup.select_one('div.tm-article-body')
        if check_word(all_data):
            print(f'{time[:10].replace("-", ":")} - "{header}" - {link}')

if __name__ == '__main__':
    response = requests.get('https://habr.com/ru/articles/')
    articles = get_all_articles(response)
    get_all_articles_where_keywords(articles)














