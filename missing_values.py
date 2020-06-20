# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:08:41 2020

@author: cs
"""


import pandas as pd
import numpy as np
import os
os.chdir("C:\\Users\\cs\\Documents\\Winter_Training")
# Read csv file into a pandas dataframe
df = pd.read_csv("property_data.csv")
print(df.head())
print (df['ST_NUM'])
print (df['ST_NUM'].isnull())
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property_data.csv", na_values = missing_values)
print (df['NUM_BATH'])
print (df['NUM_BATH'].isnull())
# Detecting numbers 
cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1

print("Total Count", cnt)
print(df['OWN_OCCUPIED'])
print (df.isnull().sum())

# Any missing values?
print (df.isnull().values.any())
# Total number of missing values
print (df.isnull().sum().sum())
# Replace missing values with a number
df['ST_NUM'].fillna(125, inplace=True)
print (df['ST_NUM'])
# Location based replacement
df.loc[2,'ST_NUM'] = 145
print (df['ST_NUM'])
# Replace using median 
median = df['NUM_BEDROOMS'].median()
df['NUM_BEDROOMS'].fillna(median, inplace=True)
print(df['NUM_BEDROOMS'])

# implenting normalization
from sklearn import preprocessing
x_array = np.array(df['NUM_BEDROOMS'])
#normalized_X = preprocessing.normalize([x_array])
normalized_X = preprocessing.normalize([df['NUM_BEDROOMS']])
print (normalized_X)

# Standardization

# Create the Scaler object
scaler = preprocessing.StandardScaler()
# Fit your data on the scaler object
x_array = np.array(df[['NUM_BEDROOMS']])
scaled_df = scaler.fit_transform(x_array)
scaled_df = pd.DataFrame(scaled_df)
print(scaled_df)