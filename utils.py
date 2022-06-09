from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

STOPWORDS = stopwords.words('english')
LEMMATIZER = WordNetLemmatizer()

def clean(s):
    s = s.translate(str.maketrans('','',string.punctuation))
    s = s.translate(str.maketrans('','','0123456789'))
    s = s.lower()
    req = []
    for word in s.split(' '):
        if word not in STOPWORDS:
            req.append(word)
    return ' '.join(req)


def process_sent(s):
    s = clean(s)
    s = lemmatize_sentence(s)
    return s

def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

def lemmatize_sentence(sentence):
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:        
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(LEMMATIZER.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

def normalize(data):

    def standardize(x):
        return (x-mini) / (maxi - mini)
    mini = min(data)
    maxi = max(data)
    return list(map(standardize, data))

def gradient_bar(data):
    new_data = [[x, y[0], y[1], y[2]] for x,y in data]
    colors = {'pos':'green', 'neu':'yellow', 'neg':'red'}
    # print(new_data)
    df = pd.DataFrame(new_data, columns=['title', 'neg', 'neu', 'pos'])
    fig = px.bar(df, x = 'title', y = ['pos', 'neu', 'neg'], title='Sentiment of Articles', color_discrete_map={'pos':'green', 'neg':'red', 'neu':'yellow'}, labels={'x':'Article', 'y':'% '+'of confidence'})
    fig.show()
        
        
if __name__ == '__main__':
    pass