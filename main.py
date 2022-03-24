import requests
import json
import pandas as pd
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import psycopg2

TOKEN = '2cc5a9f00569e24c5f14d7a59ec03d57b979ca57'
COUNTRY = 'RU'
YEAR = '2022'

headers = {
    'accepts': 'application/json'
}

r = requests.get(f'https://calendarific.com/api/v2/holidays?&api_key={TOKEN}&country={COUNTRY}&year={YEAR}', headers=headers)

data = r.json()

# print(data)

name = []
description = []
country = []
date = []
type_of_holiday = []
location = []

for holiday in data['response']['holidays']:
    name.append(holiday['name'])
    description.append(holiday['description'])
    country.append(holiday['country']['name'])
    date.append(holiday['date']['iso'])
    type_of_holiday.append(holiday['type'])
    location.append(holiday['locations'])

holiday_dict = {
    'name': name,
    'holiday_description': description,
    'country_of_holiday': country,
    'date_of_holiday': date,
    'type_of_holiday': type_of_holiday,
    'locations_of_holiday': location
}

holiday_df = pd.DataFrame(holiday_dict, columns=['name', 'holiday_description', 'country_of_holiday', 'date_of_holiday', 'type_of_holiday', 'locations_of_holiday'])



print(holiday_df)
print(date, sep='\n')