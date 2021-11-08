#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


# Calculate t* in t-distribution with 90% of CI
stats.t.ppf(0.05, 19)


# In[5]:


# Confident interval
# x + stats.t.ppf(ci percent, k=n-1) * s / np.sqrt(n)
# x - stats.t.ppf(ci percent, k=n-1) * s / np.sqrt(n)


# In[10]:


# calculate p-value for t-test
# stats.t.cdf(t, k=n-1)
stats.t.cdf(-3.044, 19)


# In[14]:


# calculate 2*P(T>= |t|)
2*(1 - stats.t.cdf(0.905, 91))


# In[16]:


1-stats.t.cdf(2.537, 8)


# In[17]:


stats.t.ppf(0.05, 8)


# In[23]:





# In[ ]:





# In[26]:


# Question 1

(2.9 + 2.6 + 2.9 +2.6 + 2.4 + 2.0 + 2.3 + 2.2 + 2.5 + 2.3 + 2.8 + 2.5 + 2.7 + 2.6) / 14


# In[33]:


(2.52 - 2.3) / (1.4 / np.sqrt(14))


# In[72]:


1 - stats.norm.cdf(3.14, 0,1)


# In[34]:


1.4 / np.sqrt(14)


# In[85]:


(2.52 - 2.3) / (0.26 / np.sqrt(14))


# In[43]:


stats.t.cdf(0.05, 19) 


# In[14]:


2.52 + stats.norm.ppf(0.05) * 0.26 / np.sqrt(14)


# In[15]:


2.52 - stats.norm.ppf(0.05) * 0.26 / np.sqrt(14)


# In[50]:


2.52 - 0.66


# In[51]:


2.52 + 0.66


# In[65]:


stats.norm.ppf(0.05)


# In[70]:


2.52 - stats.norm.ppf(0.05) * 1.4 / np.sqrt(14) 


# In[75]:


stats.t.cdf(3.14, 13)


# In[77]:


stats.t.ppf(0.025, 13)


# In[106]:



# df = pd.DataFrame({ "data": [2.9,2.6 ,2.9 ,2.6 , 2.4 , 2.0 , 2.3 , 2.2 , 2.5 , 2.3 , 2.8 , 2.5 , 2.7 , 2.6] })


# In[107]:


df['data'].describe()


# In[108]:


df.hist()


# In[27]:


# 4
df1 = pd.read_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_6\FACEBOOKFRIENDS.csv')


# df1

# In[111]:


df1


# In[29]:


stats.t.interval(0.95, 29, df1.mean(), df1.std() / np.sqrt(30))


# In[112]:


df1.hist()


# In[113]:


df1.describe()


# In[116]:


np.std(df1, ddof=1) / np.sqrt(np.size(df1))


# In[117]:


29.57 / np.sqrt(30)


# In[122]:


stats.t.ppf(0.025, 29) 


# In[121]:


2.04 * 5.4


# In[123]:


2.045 * 29.57 / np.sqrt(30)


# In[124]:


119.06 + 11.04


# In[125]:


119.06 - 11.04


# In[128]:


# 5
data = pd.read_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_6\WEIGHTGAIN.csv')


# In[129]:


data


# In[130]:


data.describe()


# In[136]:


standar_error = np.std(data['wt_gain'], ddof=1) / np.sqrt(np.size(data['wt_gain']))


# In[132]:


1.75 / np.sqrt(16)


# In[134]:


stats.t.ppf(0.025, 15)


# In[139]:


2.13 * 0.44


# In[140]:


4.73 + 0.93


# In[141]:


4.73 - 0.93


# In[143]:


stats.norm.ppf(0.025) * 0.44


# In[144]:


(4.73 - 7.3) / 0.44


# In[149]:


2 * (1 - stats.t.cdf(5.84, 15)) 


# In[148]:


0.00001626 * 2


# In[2]:


data = pd.DataFrame({ "data": [2.9,2.6 ,2.9 ,2.6 , 2.4 , 2.0 , 2.3 , 2.2 , 2.5 , 2.3 , 2.8 , 2.5 , 2.7 , 2.6] })


# In[3]:


data


# In[4]:


data.describe()


# In[5]:


data.std()


# In[10]:


# 7b
stats.t.interval(0.90, 13, 2.5214, 0.2636 / np.sqrt(14))


# In[18]:


np.std(data['data'], ddof = 1)


# In[19]:


np.mean(data['data'])


# In[21]:


(2.52 - 2.3) / (0.263 / np.sqrt(14)) 


# In[24]:


np.round(1 - stats.t.cdf(3.13, 13), 4) 


# In[26]:


2 * (1 - stats.t.cdf(5.84, 15)) 


# In[31]:


# 6
min(32-1, 33-1)


# In[35]:


2 * (1 - stats.t.cdf(1.1899, 31)) 


# In[ ]:




