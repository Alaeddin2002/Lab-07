#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("drinks.csv")


# In[9]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "NA":
        wine += df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/number)


# In[27]:


wine = 0
people = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "SA":
        wine += df["wine_servings"][i]
        people += df["spirit_servings"][i] + df["beer_servings"][i] + df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/people/number)


# In[28]:


wine = 0
people = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "AS":
        wine += df["wine_servings"][i]
        people += df["spirit_servings"][i] + df["beer_servings"][i] + df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/people/number)


# In[14]:


plt.scatter(df['spirit_servings'],df['wine_servings'])


# In[20]:


df.nlargest(10, 'spirit_servings')
    


# In[21]:


ax = df.plot.hist(column=["continent"], by="EU", figsize=(10, 8))


# In[23]:


ax = df.plot.hist(column=["continent"], by="AS", figsize=(10, 8))


# In[3]:


ax = df.plot.hist(column=["continent"], by="OC", figsize=(10, 8))


# In[24]:


ax = df.plot.hist(column=["continent"], by="SA", figsize=(10, 8))


# In[25]:


ax = df.plot.hist(column=["continent"], by="NA", figsize=(10, 8))


# In[22]:


ax = df.plot.hist(column=["continent"], by="Nan", figsize=(10, 8))


# In[32]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "SA":
        wine += df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/number)


# In[31]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "EU":
        wine += df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/number)


# In[29]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "AS":
        wine += df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/number)


# In[30]:


wine = 0
number = 0
for i in range(len(df["continent"])):
    if df["continent"][i] == "NA":
        wine += df["wine_servings"][i]
        number +=1

if number == 0:
    print (0)
else:
     print(wine/number)


# In[37]:


df.groupby(['continent']).mean()


# # Exercises

# 1. Use ```pandas``` and read dataset drinks.csv
# 1. What is the average wine consumption per person per year in North America?
# 1. What is the average wine consumption per person per year in South America?
# 1. What is the average wine consumption per person per year in Asia?
# 1. Create a scatter plot between spirit servings and wine servings of all countries.
# 1. Show a list of the top 10 spirit drinking countries: show country names & spirit servings.
# 1. Plot 6 histograms of wine servings by continent.
# 1. What is the average wine consumption in South America?
# 1. What is the average wine consumption in Europe?
# 1. What is the average wine consumption in Asia?
# 1. What is the average wine consumption in North America?
# 1. Which continent has the highest on average wine consumption?
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




