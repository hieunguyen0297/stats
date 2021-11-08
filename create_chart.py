#!/usr/bin/env python
# coding: utf-8

# In[157]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.DataFrame({'Pet': ['Dog'
# ,'None',
# 'Dog',
# 'Dog',
# 'Dog',
# 'Dog',
# 'None',
# 'Cat',
# 'Dog',
# 'Dog',
# 'Horse',
# 'Dog',
# 'Dog',
# 'None',
# 'Dog',
# 'Dog',
# 'Dog',
# 'Dog',
# 'Dog',
# 'None',
# 'Dog',
# 'Dog',
# 'Dog',
# 'Horse'
# ] })



df = pd.read_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_2\hw_2_data.csv')


# In[158]:


df


# In[159]:


# sort the df in ascending order then create plot bar chart chart
(df['Pet'].value_counts()).sort_values(ascending = True).plot.bar()


# In[160]:


(df['Pet'].value_counts()).sort_values(ascending = False).plot.bar(color= 'green')


# In[161]:


df1 = pd.DataFrame( { 'Ice Cream': ['Chocolate', 'Cookie Dough', 'Cookie & Cream', 'Mint Chip', 'Moose Tracks', 'Strawberry', 'Vanilla'], 'Count': [6,2,2,4,2,1,7], 'Percent': [6/24 *100,2/24 *100,2/24 *100,4/24 *100,2/24 *100,1/24 *100,7/24 *100] } )


# In[162]:


df1.round(1)


# In[163]:


df1.plot.bar(x = 'Ice Cream', y= 'Count')


# In[164]:


df1.plot.bar(x = 'Ice Cream', y= 'Percent')


# In[170]:


# create boxplot chart

fig , ax = plt.subplots()

bp = ax.boxplot(df['Minutes to Hometown'])
bp = ax.set_title('Boxplot of Minutes to Hometown')
bp = ax.set_xlabel('')
bp = ax.set_ylabel('Minute')


# In[166]:


df.describe()


# In[ ]:





# In[7]:


#  question 6
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df2 = pd.DataFrame( { 'age':['13-17', '18-24', '25-34', '35-54', '55+', 'unknown'], 'as of 1/04/2009': [5675,17192,11255,6989,955,23] })


# In[8]:


df2


# In[9]:


df2.plot.bar(x = 'age', y='as of 1/04/2009')


# In[10]:


df3 = pd.DataFrame( { 'age':['13-17', '18-24', '25-34', '35-54', '55+', 'unknown'], 'as of 1/04/2010': [10680,26076,25580,29918,9764,1068] })


# In[11]:


df3


# In[12]:


df3.plot.bar(x = 'age', y='as of 1/04/2010')


# In[13]:


df3.describe()


# In[14]:


df2.describe()


# In[15]:


# question 8

data = [0.00, 3.90, 5.64, 8.22, 0.00,5.62,3.92,6.81,30.61,0.00, 73.20,0.00,46.70,0.00,0.00,26.41,22.82,0.00,0.00,3.49,0.00,0.00,4.81,9.57,5.36,0.00 ,5.66,0.00,59.76,12.38,15.74,0.00 ,0.00,0.00,0.00,9.37,20.78,7.10,7.89,5.53]


# In[16]:


df4 = pd.DataFrame( { 'units': data })


# In[17]:


df4['units'].sort_values()


# In[18]:


df4.plot.bar(rot=0)


# In[19]:


df4.describe()


# In[20]:


df4.to_csv(index = False)


# In[21]:


df4.to_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_2\unit_data.csv', encoding = 'utf-8', index = False)


# In[22]:


from numpy import percentile


quartiles = percentile(df4['units'], [25,50,75])


# In[23]:


print(quartiles[0])


# In[24]:


print(quartiles[1])
print(quartiles[2])


# In[25]:


df4['units'].min()


# In[26]:


df4['units'].max()


# In[27]:


df4.boxplot()


# In[28]:


df4.hist()


# In[29]:


# question 9 

df9 = pd.read_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_2\LOSdata.csv')


# In[30]:


pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[31]:


df9


# In[32]:


df9.describe()


# In[33]:


quartiles = percentile(df9['LOS'], [10,25,50,75,90,95,99])


# In[34]:


quartiles[0]


# In[35]:


quartiles[1]


# In[36]:


quartiles[2]


# In[37]:


quartiles[3]


# In[38]:


quartiles[4]


# In[39]:


quartiles[5]


# In[40]:


quartiles[6]


# In[41]:


quartiles


# In[42]:


# CALCULATE RATE 
# WE CAN DO THIS WITH EXCEL
data = pd.read_csv(r'D:\IUPUI\FALL_2021\PUHL_B302\module_2\CLABSI data.csv')


# In[43]:


data


# In[50]:


# calculate infection rate
# create a collumn call Infection Rate and set data based on this formula
data['Infection Rate'] = round(1000 * data['Number of Infections'] / data['Patient Line Days'], 2)


# In[59]:


data


# In[54]:


data['Infection Rate'].hist()


# In[57]:


data['Device Util Rate'] = round( 100 * data['Patient Line Days'] / data['Patient Days'], 2)


# In[58]:


data['Device Util Rate']


# In[ ]:




