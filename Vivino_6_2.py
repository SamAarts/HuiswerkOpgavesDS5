import pandas as PinoGrigio
import numpy as Malbec
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as s
import statsmodels.api as sm
import scipy.stats as sp
from statsmodels.formula.api import ols

# Opdracht 1a
Wijnkaart = PinoGrigio.read_csv("winequality-red.csv", delimiter=';') # Dataset inladen
# Opdracht 1b
settypes = set(Wijnkaart.dtypes) # Types ondekken
print("De structuur van de dataset is gestructureerd.") # Conclusie trekken
print(settypes) # Printen van de verschillende types in de data


# Opdracht 1c
print('Geen slechte data geconstateerd')

# Opdracht 1d
plt.figure(figsize=(8, 5))  # Oppervlakte maken voor de histogram
sns.countplot(x='quality', data=Wijnkaart)  # Dit is een simpel histogrammetje
plt.title('Distribution of Wine Quality Ratings') # Titeltje toevoegen
plt.xlabel('Quality Rating')    # Assen toevoegen
plt.ylabel('Count')
plt.show()  # daadwerkelijke plotten van de hist


sns.set(style="whitegrid") # Mega plot maken met veel te veel info maar heb er nu te veel tijd in zitten
                           # dus hij blijft lekker staan maar er ik doe er niks mee dus je kan het eigenlijk ook gewoon negeren als ik eerlijk ben.
attributes = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
sns.pairplot(Wijnkaart[attributes], hue='quality', height=2.5)
plt.show()

corr_matrix = Wijnkaart.corr() # Correlatie matrix maken 
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f") # Correlatie matrix plotten
plt.title('Correlation Matrix Heatmap') # titeltje toevoegen
plt.show() # laten zien wat er is gesjouwd


# Opdracht 1e
Trainingsetdf = Wijnkaart.iloc[:int(len(Wijnkaart['quality'])*0.8)] #trainings data maken
Testsetdf = Wijnkaart.iloc[int(len(Wijnkaart['quality'])*0.8):] #test data maken

# Opdracht 1f

X = Trainingsetdf[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides']] # modelelletje opstellen met deze variabelen aan de hand van de heatmap van correlatie tussen de punten
Y = Trainingsetdf['quality'] # uitkomst van de de variabelen
X = sm.add_constant(X) # zorgen dat het model uitkomt/werkt

# Opdracht 1g
model = sm.OLS(Y,X).fit()   # Data toevoegen aan het model
print(model.summary())  # Kijken naar de R2adjusted

X2 = Trainingsetdf[['fixed acidity','volatile acidity','citric acid','pH', 'density', 'alcohol']] # nieuw modelletje met andere variabele sjouwen
Y2 = Trainingsetdf['quality']
X2 = sm.add_constant(X2)
model2 = sm.OLS(Y2,X2).fit()
print(model2.summary()) # zoeken naar het verschil

# Opdracht 1j
print("Als we naar de verschillen kijken naar de verschillen in R^2 adj, zien we dat model 2 beter is, maar nogsteeds niet goed is.") #uitkomst
