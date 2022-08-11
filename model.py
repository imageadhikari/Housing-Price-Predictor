import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/PuneHouseData.csv")

df1 = df.drop(["area_type","availability","society"], axis=1)

import math
median_bath = math.floor(df1.bath.median())
df1.bath = df1.bath.fillna(median_bath)

df1.balcony = df1.balcony.fillna('0')

df2 = df1.dropna()

df2['Bedrooms'] = df2['size'].apply(lambda x: int(x.split(' ')[0]))

df3 = df2.drop('size', axis=1)

df3['balcony'] = df3['balcony'].astype(float) 

def average_sqft(x):
    a = x.split('-')
    if len(a) == 2:
        return (float(a[0].strip())+float(a[1].strip()))/2
    try:
        return float(x)
    except:
        return None

df3['total_sqft'] = df3['total_sqft'].apply(average_sqft)

df3 = df3.dropna()

df4 = df3.copy()
df4['price_per_sqft'] = df4['price']*100000/df4['total_sqft']

df4.location = df4.site_location.apply(lambda x: x.strip())
location_stats =df4['site_location'].value_counts(ascending=False)

location_stats_less_than_10 = location_stats[location_stats<=10]

df4.location = df4.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)

df4[df4.total_sqft/df4.Bedrooms<300].head(10)

df5 = df4[~(df4.total_sqft/df4.Bedrooms<300)]

def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key, subdf in df.groupby('site_location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = subdf[(subdf.price_per_sqft>(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
df6 = remove_pps_outliers(df5)

def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('site_location'):
        global bhk_stats
        bhk_stats = {}
        for Bedrooms, bhk_df in location_df.groupby('Bedrooms'):
            bhk_stats[Bedrooms] = {
                'mean': np.mean(bhk_df.price_per_sqft),
                'std': np.std(bhk_df.price_per_sqft),
                'count': bhk_df.shape[0]
            }
        for Bedrooms, bhk_df in location_df.groupby('Bedrooms'):
            stats = bhk_stats.get(Bedrooms-1)
            if stats and stats['count']>5:
                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis='index')
df7 = remove_bhk_outliers(df6)

bhk_stats.get(2)

df8 = df7[df7.bath<df7.Bedrooms+2]

dummies = pd.get_dummies(df8.site_location)

df9 = pd.concat([df8,dummies],axis='columns')
df10 = df9.drop('site_location',axis='columns')

X = df10.drop('price', axis=1)
y = df10.price

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

lr = LinearRegression()
lr.fit(X_train, y_train)