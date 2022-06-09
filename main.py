import requests
from bs4 import BeautifulSoup
import sentiment
import pandas as pd
from tqdm import tqdm
import utils, json

url = 'https://www.aljazeera.com/where/mozambique/'
base_url = 'https://www.aljazeera.com'
data = requests.get(url)

# my_data = []

html = BeautifulSoup(data.text, 'html.parser')
# print(html)
articles = html.select('.gc__title')

ans = []

plot_data = []

for i in tqdm(range(10)):
    article = articles[i]
    title = article.select('.u-clickable-card__link')[0].get_text()
    article_link = base_url + article.select('.u-clickable-card__link')[0].get_attribute_list('href')[0]
    article_page = BeautifulSoup(requests.get(article_link).text, 'html.parser')
    content = ''
    for para in article_page.select('.wysiwyg--all-content')[0].select('p'):
        content+=para.get_text()
    sentim, scores = sentiment.classify(content)

    plot_data.append([title, scores])
    
    ans.append({'Link': article_link, 'Title': title, 'Content': content, 'Sentiment': sentim})

df = pd.DataFrame(ans)

df.to_csv('results.csv', index=False)

json.dumps(ans)

utils.gradient_bar(plot_data)