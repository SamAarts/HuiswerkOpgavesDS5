# ronde 2
import pandas as pindas
import datetime
import numpy as np

hotel_trivago = pindas.read_excel('hotelBookings.xlsx',sheet_name='hotel_bookings')
hotel_trivago.drop_duplicates(inplace=True)
    

def fix_year():
    for i in range(len(hotel_trivago)):
        hotel_trivago.at[i, 'arrival_date_year'] = 2015

def print_df():
    print(hotel_trivago)

def fix_month():
    for i in range(len(hotel_trivago)):
        if hotel_trivago.iloc[i, 'arrival_date_month'] == np.nan:
            if hotel_trivago.iloc[i, 'arrival_date_week_number'] == 31 and hotel_trivago.iloc[i, 'arrival_date_day_of_month'] < 2:
                hotel_trivago.at[i, 'arrival_date_moth'] = 'August'
                print(i)
            else:
                hotel_trivago.at[i, 'arrival_date_moth'] = 'July'
                print(i)

fix_year()
fix_month()
print_df()