import pandas as np
import numpy as pd

def inladen(bestandsnaam_1:str='predictions_training.xlsx', bestandsnaam_2:str='training.xlsx')->np.DataFrame:
    'laad de dataset in'
    voorspelling = np.read_excel(bestandsnaam_1)
    voetbal_training = np.read_excel(bestandsnaam_2)
    return voorspelling, voetbal_training

def oppervlakte(df:np.DataFrame)->np.DataFrame:
    'bereknt de oppervlakte en maakt een kolom hiervoor'
    opslag = []
    for index in df.index:
        delta_r = abs(df.loc[index, 'min_r'] - df.loc[index, 'max_r'])
        delta_c = abs(df.loc[index, 'min_c'] - df.loc[index, 'max_c'])
        opslag.append(delta_r * delta_c)
    df['m2'] = opslag
    return df

def overlap(df_test:np.DataFrame, df_check:np.DataFrame)->np.DataFrame:
    'bereknt de overlap tussen twee vierkantjes en voegt hier een colomn voor toe'
    opslag = []
    for index in df_test.index:
        delta_r = abs(df_check.loc[index, 'min_r'] - df_test.loc[index, 'max_r'])
        delta_c = abs(df_check.loc[index, 'min_c'] - df_test.loc[index, 'max_c'])
        opslag.append(delta_r * delta_c)
    df_test['overlap'] = opslag
    return df_test

def union(df_test:np.DataFrame, df_check:np.DataFrame)->np.DataFrame:
    'berekent de som van de oppervlaktes en voegt een kolom toe'
    opslag = []
    for index in df_test.index:
        oppervlakte1 = df_test.loc[index, 'm2']
        oppervlakte2 = df_check.loc[index, 'm2']
        opslag.append(oppervlakte1 + oppervlakte2)
    df_test['uni'] = opslag
    return df_test

def IoU(df_test)->np.DataFrame:
    'voegt een kolom met een Intersect over union toe'
    opslag = []
    for index in df_test.index:
        intersect = df_test.loc[index, 'overlap']
        union = df_test.loc[index, 'uni']
        opslag.append(intersect/union)
    df_test['score'] = opslag
    return df_test

def main():
    'de main functie doet alles'
    voorspelling, data = inladen()
    
    voorspelling = oppervlakte(voorspelling)
    data = oppervlakte(data)
    
    voorspelling = overlap(df_test=voorspelling, df_check=data)
    voorspelling = union(df_test=voorspelling, df_check= data)
    
    voorspelling = IoU(df_test=voorspelling)

if __name__ == '__main__':
    main()
    print('Doet het')
