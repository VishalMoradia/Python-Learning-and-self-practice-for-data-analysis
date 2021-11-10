# -*- coding: utf-8 -*-
"""Series_tutorial_Udemy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vyl0qF2-nzyE56QzbBnxG6K8AagZ5y4G
"""

import pandas as pd
import numpy as np
import scipy.stats as stats

pd.read_csv('https://andybek.com/pandas-drinks')

pd.read_csv('https://andybek.com/pandas-drinks', usecols= ['country', 'wine_servings'])

alcohol = pd.read_csv('https://andybek.com/pandas-drinks', usecols= ['country', 'wine_servings'], index_col= 'country', squeeze=True)

alcohol.head()

type(alcohol)

alcohol.size

alcohol.is_unique

alcohol.nunique(dropna=False)

alcohol.is_monotonic

alcohol.isnull()

null_values = list(alcohol[alcohol.isnull()].index)

null_values

len(null_values)

alcohol.isnull().sum() #serves the same functionality as above.

alcohol.isna().sum()

alcohol.notnull().sum() # xounting non-null values

wine_serving = alcohol[alcohol.notnull()]

wine_serving

total_consumed = sum(wine_serving)

less_than_hundred = wine_serving[wine_serving < 100]

wine_serving.hist()

wine_serving.quantile(.25)

wine_serving.describe() #gives the series of all descriptive statistics

wine_serving.mode()

wine_serving[wine_serving==1].sum()

wine_serving.value_counts().iloc[0]

wine_serving.value_counts(normalize=True)

wine_serving.max()

wine_serving[wine_serving == wine_serving.max()]

wine_serving.idxmax()

wine_serving[wine_serving == wine_serving.min()]

wine_serving.sort_values(ascending=False) # sorts the copy of the series. Doesnt sort the source data

# using inplace parameter to sort the source data series in the function used above

wine_serving.sort_values(ascending=False, inplace=True)

wine_serving

wine_serving.nlargest(10)

wine_serving.index.isnull().sum() # there are no null values in the index column

fifty_plus = wine_serving[wine_serving > 50]

fifty_plus

fifty_plus.nsmallest(20).mean() #mean

fifty_plus.nsmallest(20).median() #median

fifty_plus.nsmallest(20).std() #standard deviation

# creating a function which will square the value if the value is less than 200

def multiply_if_min(x, min_value):
  if x < min_value:
    return x ** 2
  return x

alcohol.apply(multiply_if_min, min_value = 200)

# updating few values in the series using update()

alcohol.update(pd.Series(data=(20, 200), index=('Afghanistan', 'Algeria')))

alcohol.head(10)

alcohol.apply(multiply_if_min, min_value = 200)

beers = pd.read_csv('https://andybek.com/pandas-drinks', usecols= ['country', 'beer_servings'], index_col = 'country', squeeze=True)

beers.head(10)

type(beers)

beers.describe()

beers.median()

only_ten = beers[:10]

only_ten.describe()



mean_of_sample = only_ten.mean()

std_dev = only_ten.std()

def zee_score(x):
  return (x - mean_of_sample)/std_dev

zee_score(only_ten)

# If the mode is bigger than median than the skew is negative. 
# if the median is less than the mean then it is right skewed distribution.
# Vice versa is true for left skewed distribution

beers.hist()

# Taking the counts of the values which are below or above the mean

count_mean_diff = (beers - beers.mean()).apply(lambda x: 'low' if x < 0 else 'high').value_counts()

count_mean_diff