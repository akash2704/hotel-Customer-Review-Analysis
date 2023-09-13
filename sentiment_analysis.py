import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
data=pd.read_excel('data.xlsx')
sia=SentimentIntensityAnalyzer()
data['polarity_scores']=data['Review'].apply(lambda x:sia.polarity_scores(x)['compound'])