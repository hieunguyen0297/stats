#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[2]:


65/5


# In[3]:


39.2192 + 28.8


# In[5]:


15.34 * 0.64


# In[6]:


0.64 * 45


# In[7]:


# to find MS
# MS = SS / df

39.2192 / 4


# In[8]:


28.8 / 45


# In[9]:


9.80 / 0.64


# In[11]:


# F = MS(between groups DFG) / MS (winthin groups  DFE)
# F = MSG / MSE
# sp = np.sqrt(MSE) 

np.sqrt(0.64)


# In[8]:


1-0.999


# In[9]:


data = pd.read_csv(r"D:\IUPUI\FALL_2021\PUHL_B302\module_7\pulse.csv")


# In[12]:


print(data)


# In[16]:


pd.set_option('display.max_rows', None)


# In[17]:


data


# In[20]:


data.boxplot(by='exercise')


# In[22]:


data.groupby('exercise').count()


# In[30]:


data.groupby('exercise').mean().boxplot()


# In[92]:


data.groupby('exercise').mean()


# In[93]:


data.groupby('exercise').std(ddof =0)


# In[33]:


# calculate f, p
# group them together
pulse1 = data['pulse'][data['exercise'] == 1]
pulse2 = data['pulse'][data['exercise'] == 2]
pulse3 = data['pulse'][data['exercise'] == 3]


# In[43]:


F, p = stats.f_oneway(pulse1, pulse2, pulse3)


# In[44]:


F


# In[45]:


p


# In[51]:


data['group4'] = np.where(data['exercise'] == 1, "One", np.where(data['exercise'] == 2, "Two", "Three") )


# In[52]:


data


# In[57]:


# table 
# pulse ~ exercise give different values becuase number and number comparation
# we want to compare number with string (categorial values)
mod = ols("pulse ~ group4", data).fit()
anovaTbl = sm.stats.anova_lm(mod, typ = 2)
anovaTbl


# In[74]:


MSG = anovaTbl['sum_sq'][0] / anovaTbl['df'][0]
# msg = 1151.09 / 2


# In[75]:


MSE = anovaTbl['sum_sq'][1] / anovaTbl['df'][1]
# mse = 12013.666089 / 107


# In[76]:


print(MSG)

print(MSE)


# In[77]:


MSG /MSE


# In[78]:


sp = np.sqrt(MSE)


# In[79]:


sp


# In[80]:


7433.86 + 12579.6


# In[81]:


SST = 1151.097548 + 12013.666089


# In[82]:


SST


# In[83]:


# calculate R^2
# SSG / SST
1151.097548 / SST


# In[91]:


# question 12

p1 = 2 * (1 - stats.t.cdf(np.abs((np.mean(pulse1)-np.mean(pulse2)) / 
                                    (sp * np.sqrt(1 / len(pulse1) + 1 / len(pulse2)))), 
                                    len(pulse1) + len(pulse2) + len(pulse3) - 3))
p2 = 2 * (1 - stats.t.cdf(np.abs((np.mean(pulse2)-np.mean(pulse3)) / 
                                    (sp * np.sqrt(1 / len(pulse2) + 1 / len(pulse3)))), 
                                    len(pulse2) + len(pulse2) + len(pulse3) - 3))
p3 = 2 * (1 - stats.t.cdf(np.abs((np.mean(pulse1)-np.mean(pulse3)) / 
                                    (sp * np.sqrt(1 / len(pulse1) + 1 / len(pulse3)))), 
                                    len(pulse1) + len(pulse2) + len(pulse3) - 3))


# In[85]:


ptup = (p1, p2, p3)


# In[86]:


ptup


# In[89]:


reject, adjusted, ps, ps2 =  statsmodels.sandbox.stats.multicomp.multipletests(ptup, alpha = 0.05, method = 'Bonferroni')


# In[90]:


adjusted


# In[2]:


data = pd.read_csv(r"D:\IUPUI\FALL_2021\PUHL_B302\module_7\deadpoets.csv")


# In[3]:


data


# In[6]:


pd.set_option('display.max_rows', None)


# In[7]:


data


# In[5]:


data.boxplot(by='type1')


# In[8]:


data.groupby('type1').mean()


# In[9]:


data.groupby('type1').std(ddof=0)


# In[11]:


data.groupby('type1').count()


# In[12]:


group1 = data['age'][data['type1'] == 1]
group2 = data['age'][data['type1'] == 2]
group3 = data['age'][data['type1'] == 3]


# In[19]:


F, p = stats.f_oneway(group1, group2, group3)


# In[20]:


F


# In[21]:


p


# In[22]:


mod = ols("age ~ type", data).fit()
anovaTbl = sm.stats.anova_lm(mod, typ = 2)
anovaTbl


# In[3]:


25 * 15 - 15


# In[5]:


1- stats.f.cdf(4.727, 2, 94)


# In[ ]:




