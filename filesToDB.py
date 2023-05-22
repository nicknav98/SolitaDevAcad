# Solita Dev Academy - Files to Database
# Built with Python 3.9
# Author: Nicholas Navarro
# First Revision: 22.5.23


import os 
import pandas as pd
from sqlalchemy import create_engine
import numpy as np 
import glob
import shutil
import secretsVars

# handles connection to database, replace IP and table name to whatever database
# this uses a postgres docker container that is running on local machine
# IP address localhost.
engine = create_engine('postgresql+psycopg2://'+secretsVars.username+':'+secretsVars.password+'@localhost:5432/TestDB')


file2105 = './CSVData/2021-05.csv'
file2106 = './CSVData/2021-06.csv'
file2107 = './CSVData/2021-07.csv'
fileBikeInfo = './CSVData/Bikeinfo.csv'


#Reads CSV files and applies to dataframes df1,df2,df3 and BikeInfo 
df1 = pd.read_csv(file2105, sep=',', engine='python')
df2 = pd.read_csv(file2106, sep=',', engine='python')
df3 = pd.read_csv(file2107, sep=',', engine='python')
dfBikeInfo = pd.read_csv(fileBikeInfo, sep=',', engine='python')

#Drop rows with duration less than 10 seconds
df1 = df1[df1['Duration (sec.)'] >= 10]
df2 = df2[df2['Duration (sec.)'] >= 10]
df3 = df3[df3['Duration (sec.)'] >= 10]

#Drop rows with distance less than 10 meters
df1 = df1[df1['Covered distance (m)'] >= 10]
df2 = df2[df2['Covered distance (m)'] >= 10]
df3 = df3[df3['Covered distance (m)'] >= 10]

#Exports Dataframes with cleaned data to Postgres Container while creating a table for each day, if table exists, appends data. 
df1.to_sql('Journeys2105', engine, if_exists='append', index=False)
df2.to_sql('Journeys2106', engine, if_exists='append', index=False)
df3.to_sql('Jounreys2107', engine, if_exists='append', index=False)
dfBikeInfo.to_sql('StationInfo', engine, if_exists='append', index=False)


print('\nData succesfully transfered to Postgres\n')
