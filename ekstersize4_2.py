# ronde 2
import pandas as pindas

hotel_trivago = pindas.read_excel('hotelBookings.xlsx',sheet_name='hotel_bookings')

hotel_trivago.dropna(axis='columns',inplace=True)
hotel_trivago.dropna(axis='rows',inplace=True)
hotel_trivago.drop_duplicates(inplace=True)
print(hotel_trivago)

