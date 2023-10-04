import pandas as pindas
import langdetect as ld
from textblob import TextBlob as tb
from nltk.sentiment import SentimentIntensityAnalyzer

# dit moet gebeuren voor het werkt:
#import nltk
#nltk.download('vader_lexicon')
#pip instal nltk
#pip instal textblob

def inlezen_excel(bestandsnaam:str='')->pindas.DataFrame:
    frame = pindas.read_excel(bestandsnaam)
    return frame

def taal_detecteren(bestandsnaam:str='')->pindas.DataFrame:
    frame = inlezen_excel(bestandsnaam=bestandsnaam)
    frame['language'] = ''
    frame['language'] = frame['language'].astype('object')
    for index in frame.index:
        tweet = frame.iloc[index, 3]
        try:
            frame.iloc[index,10] = ld.detect(tweet)
        except:
            frame.iloc[index,10] = 'Unknown'
    return frame

def analyze_sentiment_english(tweet:str='')->str:
    blob = tb(tweet)
    score = blob.sentiment.polarity
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

def analyze_sentiment_other(tweet:str='')->str:
    sia = SentimentIntensityAnalyzer()
    try:
        score = sia.polarity_scores(tweet)['compound']
    except:
        score = 0
        print(tweet)
        print(""" 
              oeps
              """)
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def apply_sentiment_check(frame:pindas.DataFrame)->pindas.DataFrame:
    frame['sentiment'] = ''
    frame['sentiment'] = frame['sentiment'].astype('object')
    for index in frame.index:
        tweet = frame.iloc[index, 3]
        language = frame.iloc[index, 10]
        if language == 'en':
            sentiment = analyze_sentiment_english(tweet)
            frame.iloc[index,11] = sentiment
        else:
            sentiment = analyze_sentiment_other(tweet)
            frame.iloc[index,11] = sentiment            
        
    return frame

def main(bestandsnaam:str='tweets.xlsx'):
    frame = taal_detecteren(bestandsnaam=bestandsnaam)
    frame = apply_sentiment_check(frame=frame)
    return frame
    
#if __name__ == '__main__':
frame = main()
print(frame.head(5))
      
#analyze_sentiment_english('Textblob is amazingly simple to use. What great fun!')
#print(ld.detect('alle eendjes zwemmen in het water'))