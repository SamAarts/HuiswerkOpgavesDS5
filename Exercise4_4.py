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
    ''' Een functie om een excel bestand in een pandas dataframe te zetten
    bestandsnaam kan mee gegeven worden als string inclusief bestands type
    .xlsx
    '''
    frame = pindas.read_excel(bestandsnaam)
    return frame

def taal_detecteren(bestandsnaam:str='')->pindas.DataFrame:
    '''een functie om een nieuwe collom toe te voegen aan een dataframe.
    in deze collom komt de taal van de string uit de 4de collom, column met index 3
    bestandsnaam is nodig omdat de inlees functie word aangeroepen
    '''
    frame = inlezen_excel(bestandsnaam=bestandsnaam)        # maken frame
    frame['language'] = ''                                  # maken nieuwe collumn
    frame['language'] = frame['language'].astype('object')  # type van collumn correct meegeven
    for index in frame.index:                               # naar elke rij kijken
        tweet = frame.iloc[index, 3]                        # string uit rij opslaan in variable tweet
        try:                                                # try functie zodat we niet stoppen als de taal detectie faalt
            frame.iloc[index,10] = ld.detect(tweet)         # als taal detectie lukt opslaan in eerder gemaakte collumn
        except:                                             # als taal detectie faalt unknown invullen in collumn
            frame.iloc[index,10] = 'Unknown'
    return frame                                            # terug geven van dataframe

def analyze_sentiment_english(tweet:str='')->str:
    ''' een functie om het sentiment van een string te bepalen, gegeven dat deze string in het engels is
    ontvangt een string en maakt gebruik van de blobtext library om punten te geven aan een string
    geeft een string terug op basis van de score
    '''
    blob = tb(tweet)                    # textblob object aanmaken
    score = blob.sentiment.polarity     # sentiment uitrekenen en de polariteit hieruit halen (eerste waarde uit de resulteerende tuple)
    if score > 0:                       # score groter dan nul, positief returnen
        return 'positive'
    elif score < 0:                     # score kleiner dan nul, negatief returnen
        return 'negative'
    else:                               # anders neutraal returnen
        return 'neutral'

def analyze_sentiment_other(tweet:str='')->str:
    '''een functie om het sentiment van een string te bepalen, in het geval dat deze string niet in het engels is
    ontvangt een string en maakt gebruik van de nltk library om punten te geven aan een string
    geeft een string terug op basis van de score
    '''
    sia = SentimentIntensityAnalyzer()                  # aanmaken sentimentintensityanalyzer object
    try:                                                # proberen een score te geven, bij falen is score nul
        score = sia.polarity_scores(tweet)['compound']  
    except:
        score = 0
    if score >= 0.05:                                   # score groter dan 0.05: positief
        return 'positive'
    elif score <= -0.05:                                # score kleiner dan - 0.05: negatief
        return 'negative'
    else:                                               # alle andere gevallen: neutraal
        return 'neutral'

def apply_sentiment_check(frame:pindas.DataFrame)->pindas.DataFrame:
    ''' Een functie om voor een dataframe met strings en een taal het sentiment te bepalen
    verwacht een pandas dataframe en retourneerd een zelfde frame met een extra collom
    '''
    frame['sentiment'] = ''                                     # nieuwe rij aanmaken
    frame['sentiment'] = frame['sentiment'].astype('object')    # type goed zetten
    for index in frame.index:                                   # voor iedere rij gaan kijken
        tweet = frame.iloc[index, 3]                            # string vinden
        language = frame.iloc[index, 10]                        # taal vinden
        if language == 'en':                                    # als het engels is engelse sentiment check uitvoeren
            sentiment = analyze_sentiment_english(tweet)        # opslaan in sentiment
            frame.iloc[index,11] = sentiment                    # in het frame terug plaatsen in de nieuwe collom
        else:                                                   # anders zelfde handeling met de algemene sentiment check 
            sentiment = analyze_sentiment_other(tweet)
            frame.iloc[index,11] = sentiment            
        
    return frame                                                # retourneren frame

def main(bestandsnaam:str='tweets.xlsx'):
    ''' Het uivoeren van de gehele opdracht, mogelijkheid om een ander bestand mee te geven maar tweets.xlsx als uitgangs punt
    detecteerd de taal, slaat deze op in een data frame,
    deze word mee gegeven met de sentiment check voor het frame en tot slot retourneren we het frame
    '''
    frame = taal_detecteren(bestandsnaam=bestandsnaam)
    frame = apply_sentiment_check(frame=frame)
    return frame
    
if __name__ == '__main__': # voert het belangrijkste stuk code uit
    frame = main()
    print(frame.head(5)) # visualisatie van het resultaat
      
#analyze_sentiment_english('Textblob is amazingly simple to use. What great fun!')
#print(ld.detect('alle eendjes zwemmen in het water'))