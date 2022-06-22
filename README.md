# News-Sentiment-Analysis


This project pulls the most recent articles from "https://www.aljazeera.com/where/mozambique/" and predicts the sentiment from it.

## Code Flow

## Step 1: Get NEWS link from given URL 
a. Pull the 10 most recent News articles about Mozambique from the Aljazeera using the package "request" and "BeautifulSoup".

b. I extracted all the valid clickable titles and used the articles according to their "recentness",

## Step 2: Get NEWS description and headlines from the extracted link 
a. Pull the Headline and Content of the article from all the clickable elements. 

b. Sometimes, not all content was not available in the main page of Aljazeera. So, I went in deeper into the child article link to get the entire content.

c. Use the 10 most recent articles

## Step 3: Data Cleaning 
Apply the below cleaning functions on the content of the article
    remove punctuation
    remove numbers
    convert to lowercase
    remove stop words
    lemmatize


## Step 4: Applied a State of the Art RoBERTa base model fine tuned on the Twitter Dataset

I used the content of each article, tokenized it using BERT base encoder and then predicted the sentiment. I verified the predicted sentiment with the actual. My classes were 'Positive', 'Negative' and 'Neutral'.

### *I referred to BERT, DistilBART, BART, T5, CamelBERT and I found that RoBERTa gave the most confident results*

### roBERTa:
RoBERTa stands for Robustly Optimized BERT Pre-training Approach. This roBERTa-base model trained on ~124M tweets from January 2018 to December 2021, and finetuned for sentiment analysis with the TweetEval benchmark. The original reference paper is TweetEval. This model is suitable for English.

I used this https://arxiv.org/abs/2202.03829 as my base model.


## Step 5: Visualization
a. Each bar represent the sum of all the probabilities of a sentiment. The height of each segment denotes the probability of a particular sentiment.

b. Visualization picture is stored in viz.png
<img width="1265" alt="viz" src="https://user-images.githubusercontent.com/40538922/172770776-def03178-b898-4c75-bbc5-61919030985f.png">

## Total Time: 5 Sec

# Data

The articles used are in results.json.

## *Please refer to results.json file in the repository for the Headline and Article data fetched from Url*

# How to Run the code 

1. Install python
2. Install all the packages from requirements.txt
3. Run main.py
4. Check the results.csv file for the results.
