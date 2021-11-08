#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
import numpy as np


# In[2]:


66.2 + stats.norm.ppf(0.025) * 4.1 / 20


# In[3]:


66.2 - stats.norm.ppf(0.025) * 4.1 / 20


# In[4]:


stats.norm.ppf(0.025) * 4.1 / 20


# In[5]:


stats.norm.ppf(0.025) * 4.1 / 10


# In[6]:



stats.norm.ppf(0.025)


# In[7]:


63+ 69+ 62+ 66


# In[8]:


260 / 4


# In[9]:


2.4/ 2


# In[11]:


stats.norm.ppf(0.005) * 2.4 / np.sqrt(4)


# In[13]:


(stats.norm.ppf(0.005) * 2.4 / 1)**2


# In[15]:


2*(1 - stats.norm.cdf(2.12))


# In[17]:


stats.norm.cdf(2.12)


# In[18]:


(116.2 - 115) / (25 / np.sqrt(25))


# In[19]:


2*stats.norm.cdf(0.24)


# In[20]:


2*(1 - stats.norm.cdf(0.24))


# In[4]:


#12
np.round(1 - stats.norm.cdf(1.63, 0, 1), 3)


# In[5]:


1 - stats.norm.cdf(1.63, 0, 1)


# In[6]:


stats.norm.cdf(1.63, 0, 1)


# In[7]:


2 * ( 1 - stats.norm.cdf(1.63, 0, 1) )


# In[12]:


#13
10.0023 + stats.norm.ppf(0.01) * 0.0002 / np.sqrt(5)


# In[13]:


10.0023 - stats.norm.ppf(0.01) * 0.0002 / np.sqrt(5)


# In[16]:


(stats.norm.ppf(0.01) * 0.0002 / 0.0001)**2


# In[18]:


#10

x = (5.4 + 5.2 + 4.5 + 4.9 + 5.7 + 6.3) / 6
print(x)


# In[19]:


5.33 + stats.norm.ppf(0.025) * 0.9 / np.sqrt(6)


# In[21]:


5.33 - stats.norm.ppf(0.025) * 0.9 / np.sqrt(6)


# In[27]:


(5.33 - 4.8) / (0.9 / np.sqrt(6)) 


# In[31]:


1 - stats.norm.cdf(1.442477,0 ,1)


# In[3]:


#14 
(5.2 - 4.8) / (1 / np.sqrt(30)) 


# In[5]:


1 - stats.norm.cdf(2.19, 0, 1) 


# In[8]:


#11
(2453.7 - 2403.7)  / (880 / np.sqrt(100)) 


# In[10]:


1 - stats.norm.cdf(0.568, 0, 1) 


# In[11]:


(2453.7 - 2403.7)  / (880 / np.sqrt(600))


# In[13]:


1 - stats.norm.cdf(1.39, 0, 1) 


# In[ ]:




