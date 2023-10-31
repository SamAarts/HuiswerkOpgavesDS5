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
print("De structuur van de dataset is gestructureerd.")
print(settypes) # Printen


# Opdracht 1c
plt.figure(figsize=(8, 5))
sns.countplot(x='quality', data=Wijnkaart)
plt.title('Distribution of Wine Quality Ratings')
plt.xlabel('Quality Rating')
plt.ylabel('Count')
#plt.show()

# 1d
sns.set(style="whitegrid")
attributes = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
sns.pairplot(Wijnkaart[attributes], hue='quality', height=2.5)
#plt.show()

corr_matrix = Wijnkaart.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# 1e

Trainingsetdf = Wijnkaart.iloc[:int(len(Wijnkaart['quality'])*0.8)]
Testsetdf = Wijnkaart.iloc[int(len(Wijnkaart['quality'])*0.8):]

# 1g

X = Trainingsetdf[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides']]
Y = Trainingsetdf['quality']
X = sm.add_constant(X)
model = sm.OLS(Y,X).fit()
print(model.summary())

X2 = Trainingsetdf[['fixed acidity','volatile acidity','citric acid','pH', 'density', 'alcohol']]
Y2 = Trainingsetdf['quality']
X2 = sm.add_constant(X2)
model2 = sm.OLS(Y2,X2).fit()
print(model2.summary())

# 1j
print("Als we naar de verschillen kijken naar de verschillen in R^2 adj, zien we dat model 2 beter is, maar nogsteeds niet goed is.")
