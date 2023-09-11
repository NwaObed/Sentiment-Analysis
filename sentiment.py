import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from textblob import TextBlob
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# %matplotlib inline
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected = True)
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings('ignore')
warnings.warn("this will not show")

pd.set_option('display.max_columns', None)

class CustomSentimentAnalyzer:
    
    def lower_case(df, column_name):
        rt = lambda x: re.sub("[^a-zA-Z]", ' ', str(x))
        df[column_name] = df[column_name].map(rt)
        df[column_name] = df[column_name].str.lower()
        return df
    
    def sentiment_analyzer(df, col_name):
        df[['polarity', 'subjectivity']] = df[col_name].apply(lambda Text : pd.Series(TextBlob(Text).sentiment))

        for index, row in df[col_name].iteritems():

            score = SentimentIntensityAnalyzer().polarity_scores(row)

            neg = score['neg']
            neu = score['neu']
            pos = score['pos']

            if neg > pos:
                df.loc[index, 'sentiment'] = 'Negative'
            elif pos > neg:
                df.loc[index, 'sentiment'] = 'Positive'
            else:
                df.loc[index, 'sentiment'] = 'Neutral'
        return df