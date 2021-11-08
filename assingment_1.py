#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


df = pd.read_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_1\assignment_1\Lab1Data.csv')


# In[2]:


df


# In[4]:


df.sample(5, replace = False )


# In[5]:


df.sample(5, replace = False )


# In[6]:


df.sample(5, replace = False )


# In[7]:


df.sample(5, replace = False )


# In[8]:


df.sample(5, replace = False )


# In[9]:


df['school'] == 'Public Health'


# In[16]:


df[df['School'] == 'Public Health']


# In[ ]:




