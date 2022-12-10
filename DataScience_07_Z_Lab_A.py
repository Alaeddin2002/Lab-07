#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("drinks.csv")


# In[4]:


df.head(10)


# In[5]:


beer_servings = []
for i in df["beer_servings"]:
    beer_servings.append(i)
print(beer_servings)


# In[6]:


for i in range(len(df["country"])):
    if df["continent"][i]=="SA" or df["continent"][i]=="NA":
        print(df.iloc[i,:])
    


# In[8]:


for i in range(len(df["country"])):
    if df["continent"][i]=="NA":
        print(df.iloc[i,:])
    


# In[9]:


north_america = ['Beer']
print( north_america)
america_continent = ['Champagne']
print(  america_continent)


# In[12]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "AF":
        wine += df["wine_servings"][i]
        number +=1
print(wine/number)


# In[15]:


wine = 0
people = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "NA" or df["continent"][i]=="SA":
        wine += df["wine_servings"][i]
        people += df["spirit_servings"][i] + df["beer_servings"][i] + df["wine_servings"][i]
        number +=1
print(wine/people/number)


# In[16]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "EU":
        wine += df["wine_servings"][i]
        people += df["spirit_servings"][i] + df["beer_servings"][i] + df["wine_servings"][i]
        number +=1
print(wine/people/number)


# # Exercises

# 1. Use ```pandas``` and read dataset drinks.csv
# 1. Show the first 10 rows of drinks
# 1. create a variable called beer_servings and use it to store the beer_servings column
# 1. Display a dataframe where the only rows are those with continent America
# 1. Display a dataframe where the only rows are those with continent North America
# 1. Create a new dataframe called north_america that holds your answer in 1. drinks (the dataframe) should remain unchanged.
# 1. Create a new dataframe called america_continent that holds your answer in 1. drinks (the dataframe) should remain unchanged.
# 1. What is the average wine consumption per person per year in Africa?
# 1. What is the average wine consumption per person per year in America?
# 1. What is the average wine consumption per person per year in Europe?
# 
# 1. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# ## Versions

# In[ ]:


from platform import python_version
print("python version: ", python_version())
get_ipython().system('pip3 freeze | grep qiskit')


# # References

# [0] source https://github.com/sinanuozdemir
# 
# [1] numpy https://numpy.org/
# 
# [2] scipy https://docs.scipy.org/
# 
# [3] matplotlib https://matplotlib.org/
# 
# [4] matplotlib.cm https://matplotlib.org/stable/api/cm_api.html
# 
# [5] matplotlib.pyplot https://matplotlib.org/stable/api/pyplot_summary.html
# 
# [6] pandas https://pandas.pydata.org/docs/
# 
# [7] seaborn https://seaborn.pydata.org/
# 

# In[ ]:




