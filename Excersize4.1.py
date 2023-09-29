# we zijn van start
import pandas as pindas


def Excersize4_1(excelname, sheetname):
    project4dataframe = pindas.read_excel(excelname,sheet_name=sheetname)

    project4dataframe.drop_duplicates(inplace=True)
    project4dataframe.drop(index=[0,1,2,3], inplace=True)
    project4dataframe.columns =['Klant nummer',
                                'Postcode','CRM',
                                'Menu','Product',
                                'Merk','Inhoud',
                                '2018','2019',
                                '2020','2021',
                                '2022']
    df = project4dataframe.astype({'Klant nummer':'int',
                                'Inhoud':'float',
                                '2018':'float',
                                '2019':'float',
                                '2020':'float',
                                '2021':'float',
                                '2022':'float'})
    project4dataframe = df

    project4dataframe = project4dataframe[project4dataframe['CRM'] != 'Result']
    project4dataframe.reset_index(inplace=True, drop=True)
    return project4dataframe


print(Excersize4_1('dataProject4.xlsx', '20000-211000'))

