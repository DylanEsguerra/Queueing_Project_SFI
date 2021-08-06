#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from numpy import savetxt
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


step = 10000
raw = pd.read_csv("",header=None) 
df = raw.groupby(raw.index // step).mean()


# In[3]:


plt.scatter(range(1000),df)
plt.xlabel("every 10,000")
plt.ylabel("means")
plt.show


# In[5]:


df.to_numpy()
error = df - 10
error.hist(bins='auto')
plt.grid(False)
plt.xlabel("error")
plt.ylabel("frequency")
plt.show()
