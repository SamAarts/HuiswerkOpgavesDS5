import pandas as pindas
import numpy as stumpert

import pandas as pd

# Opgave 1
df = pd.read_excel('detailedRetail.xlsx')

# Opgave 2.1
CategorySales = df.groupby('Category')['Sales'].sum().reset_index()

# Opgave 2.2
CategorySalesPercentage = (CategorySales['Sales'] / CategorySales['Sales'].sum()) * 100

# Opgave 2.3
SalesPerMonth = df.groupby('Month')['Sales'].sum().reset_index()

# Opgave 2.4
MonthSalesPercentage = (SalesPerMonth['Sales'] / SalesPerMonth['Sales'].sum()) * 100

# Opgave 2.5
SalesPerManager = df.groupby('Sales Manager')['Sales'].sum().reset_index()

# Opgave 2.6
ManagerSalesPercentage = (SalesPerManager['Sales'] / SalesPerManager['Sales'].sum()) * 100


# Data toevoegen aan een dict zodat we het makkelijk kunnen importeren in een df
data = {
    'SalesPerKat': CategorySales['Sales'],
    'SalesPerKat%': CategorySalesPercentage,
    'SalesPerMaand': SalesPerMonth['Sales'],
    'SalesPerMaand%': MonthSalesPercentage,
    'SalesPerManager': SalesPerManager['Sales'],
    'SalesPerManager%': ManagerSalesPercentage
}


# Df maken.
df2 = pd.DataFrame(data)

# Df uploaden naar een excelfile
df2.to_excel("reportRetail.xlsx")

