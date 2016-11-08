#KAGGLE DATA: pollution_us_2000_2016.csv
#
#input:   pollution_us_2000_2016.csv
#output:  d_pollution_data.csv
#         n_pollution_data.csv  
#----------------------------------------

PATH = '/Users/susmitadatta/Tutorials/Kaggle/Pollution_2000_2016/'
FILENAME = 'pollution_us_2000_2016.csv'


# open original file
df <- read.csv('pollution_us_2000_2016.csv', header = TRUE, sep = ",")


# convert quantities with unit 
# 'parts per million' (ppm) to 'parts per billion' (ppb)
# round all pollutant measures to 3 decimal places
#
# ==> What is the unit of AQI? Possibly unitless <==
# ==> AQI is not changed <==
#
precision = 3

df['O3.Mean'] = round(df['O3.Mean']*100, precision)
df['O3.1st.Max.Value'] = round(df['O3.1st.Max.Value']*100, precision)

df['CO.Mean'] = round(df['CO.Mean']*100, precision)
df['CO.1st.Max.Value'] = round(df['CO.1st.Max.Value']*100, precision)

df['NO2.Mean'] = round(df['NO2.Mean'], precision)
df['N02.1st.Max.Value'] = round(df['NO2.1st.Max.Value'], precision)

df['SO2.Mean'] = round(df['SO2.Mean'], precision)
df['SO2.1st.Max.Value'] = round(df['SO2.1st.Max.Value'], precision)



