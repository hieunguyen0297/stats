#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
import numpy as np


# In[2]:


#Q 2a
1- stats.norm.cdf(140, 125, 10)


# In[3]:


# Q 2b
1 - stats.norm.cdf(140, 125, 10/np.sqrt(3))


# In[4]:


# Q 3c
1 - stats.norm.cdf(66000, 64571, 4000/np.sqrt(60))


# In[5]:


# Q 4a
1 - stats.norm.cdf(10500, 9000, 1000)


# In[20]:


#Q 4c
1 - stats.norm.cdf(15, 9000, 1000/np.sqrt(15))


# In[12]:


#Q 5a
1 - stats.norm.cdf(5,3.45, 1.63)


# In[21]:


#Q 5b
float("%.4f" % (1 - stats.norm.cdf(4, 3.45, 0.42)))


# In[19]:


#Q 5c
float("%.4f" % (1 - stats.norm.cdf(3.6, 3.45, 0.163)))


# In[ ]:




