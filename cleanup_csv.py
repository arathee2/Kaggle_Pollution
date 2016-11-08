'''
KAGGLE DATA: pollution_us_2000_2016.csv

input:   pollution_us_2000_2016.csv
output:  d_pollution_data.csv
         n_pollution_data.csv  

readme: work_log.txt   
'''

import csv
import pandas as pd
from datetime import datetime




# helper functions
def stripDatetime(local_date):
  '''converts local the string Date Local to
     three separate integer variables:
     year, month and day
  '''   	
  year_ , month_ , day_ = [], [], []

  for rec in range(0, len(local_date)): 
    datestring = local_date[rec]
    dt = datetime.strptime(datestring, '%Y-%m-%d')
    year_.append(dt.year)
    month_.append(dt.month)
    day_.append(dt.day)
  return year_, month_, day_





# main
PATH = '/Users/susmitadatta/Tutorials/Kaggle/Pollution_2000_2016/'
FILENAME = 'pollution_us_2000_2016.csv'

# open original file
infile = open(PATH+FILENAME)

# read original csv file as pandas dataframe (tabular data in R)
df = pd.read_csv(infile)



# convert quantities with unit 
# 'parts per million' (ppm) to 'parts per billion' (ppb)
# round all pollutant measures to 3 decimal places
#
# ==> What is the unit of AQI? Possibly unitless <==
# ==> AQI is not changed <==
#
precision = 3

df['O3 Mean'] = round(df['O3 Mean']*100, precision)
df['O3 1st Max Value'] = round(df['O3 1st Max Value']*100, precision)

df['CO Mean'] = round(df['CO Mean']*100, precision)
df['CO 1st Max Value'] = round(df['CO 1st Max Value']*100, precision)

df['NO2 Mean'] = round(df['NO2 Mean'], precision)
df['N02 1st Max Value'] = round(df['NO2 1st Max Value'], precision)

df['SO2 Mean'] = round(df['SO2 Mean'], precision)
df['SO2 1st Max Value'] = round(df['SO2 1st Max Value'], precision)



# delete separeate unit's column for each pollutant. 
# add one unit's column (ppb) for all pollutant
del df['NO2 Units']
del df['O3 Units']
del df['SO2 Units']
del df['CO Units']

df['Unit'] = 'ppb' # ppb: parts per billion


df.drop_duplicates()

# give each record a unique ID. 
# will be handy when merging the file
seq_id = list(range(0, len(df)))
df['ID'] = seq_id 



# add three new columns to the dataframe for year, month and day
# from Date Local string
# Column names: 'Year', 'Month', 'Day'
# ==> the function stripDatetime uses for loop <==
# ==> takes long, need to find a better method <==
year_, month_, day_ = stripDatetime(list(df['Date Local']))
df['Year'], df['Month'], df['Day'] = year_, month_, day_



# break the data into two dataframes
# create a dataframe with numeric data
# create a dataframe with descriptive data
df_d = df[['ID','Date Local','Site Num',\
           'State','State Code',\
           'County','County Code',\
           'City','Address']] 

df_n = df[['ID','Year','Month', 'Day', 'Unit',\
            'NO2 Mean', 'NO2 1st Max Value', 'NO2 1st Max Hour', 'NO2 AQI',\
            'O3 Mean', 'O3 1st Max Value', 'O3 1st Max Hour', 'O3 AQI',\
            'SO2 Mean', 'SO2 1st Max Value', 'SO2 1st Max Hour', 'SO2 AQI',\
            'CO Mean',  'CO 1st Max Value',  'CO 1st Max Hour',  'CO AQI' ]] 



#write dataframe as csv
df_d.to_csv('d_pollution_data.csv', sep=' ')
df_n.to_csv('n_pollution_data.csv', sep=' ')





