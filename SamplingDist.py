#!/usr/bin/env python
# coding: utf-8

# <h1><center>PBHL B302 Biostatistics for Informatics</center><h1>
# <h2><center>Lecture 4: Sampling Distributions<br> Spencer Lourens, Ph.D.</center><h2>

# # Using Jupyter Notebook
# For the remainder of this class, Python code handouts will be created in Jupyter Notebooks, so you will need to utilize Jupyter notebook to access the code demonstration handouts. 

# ## Importing packages/modules:
# Almost every Jupyter Notebook you ever create will need to first load necessary external functionality that you use in your program. Below, we import **scipy.stats** and **numpy**:

# In[2]:


import scipy.stats as stats
import numpy as np


# ## Solving Normal Problems with scipy.stats (for the sample mean, $\bar{X}$)
# ### Calculating $P(\bar{X} \leq 4)$ for $X \sim N(5, 20)$ and $n = 25$:
# 
# We know from above that $n = 25$, so based on the notes, $\bar{X} \sim N(5, 20 / \sqrt{25}) = N(5, 20/5)= N(5, 4)$. We can proceed in two ways. We can standardize the probability $P(\bar{X} \leq 4)=P(Z \leq \frac{4 - 5}{4})=P(Z \leq \frac{-1}{4}) = P(Z\leq -0.25)$, or we can use the **scipy.stats.norm.cdf()** function with mean 5 and sd 4:
# 
# ### Method 1 (Standardization):

# In[13]:


## using scipy.stats.norm():
## Remember, Z ~ N(0, 1):
standardized = stats.norm.cdf(-0.25, 0, 1)
standardized


# ### Method 2 (Using mean and sd arguments to stats.norm.cdf()):

# In[14]:


## using scipy.stats.norm():
## Remember, Xbar ~ N(5, 4/5):
nonst = stats.norm.cdf(4, 5, 4)
nonst


# As expected, the answers are the same. One was arrived at by standardizing before calculating, and the other was arrived at by using the mean and SD arguments to **scipy.stats.norm()**. You **MUST** answer questions on the lab according to the rules given. Sometimes, we will force you to standardize before hand. Other times, we will allow you to modify the mean/sd arguments to **scipy.stats.norm()**. Please make one extra note here, because we set the special keyword **as**, we do not call **scipy.stats.norm()**, but the shortcut **stats.norm()**. Using **as** allows us to cut down on the amount of code we write.

# ### Another note on formatting, of course:
# Don't forget, you can format your code using string manipulation in Python, and then converting back to a float at the end of the manipulation, as below. When you turn in a lab, which should be a jupyter notebook format, you must format your answers accordingly when asked to.

# In[5]:


## norm.cdf takes first argument x, second of mean, third of sigma (SD)
## recall formatting for printing:
float("%.4f" % stats.norm.cdf(4, 5, 4))


# See, now we have the probability rounded to 4 decimals!

# ## Calculating $P(\bar{X} > 4)$ for $X \sim N(5, 20)$ with $n = 45$:

# Eventually, this problem will use the "1 minus" rule to obtain $P(\bar{X}>4)$ from $1-P(\bar{X}\leq4)$. However, as in the above problem, there are two ways to proceed:
# ### Method 1 Standardization:
# First we must note that since $X \sim N(5,20)$, $\bar{X} \sim N(5, 20/\sqrt{45}) \approx N(5, 2.98)$. How did we arrive at this answer? The code below shows how to calculate $20/\sqrt{45}$ using **numpy** (currently imported as **np**):

# In[10]:


20/np.sqrt(45)


# So, round the answer to two decimal places, and we have $\bar{X} \sim N(5, 2.98)$. Now we can standardize based on this information: $P(\bar{X} > 4) = P(Z > \frac{4-5}{2.98})\approx P(Z>-0.3356)$. The symbol $\approx$ means **approximately**, because we rounded $\frac{4-5}{2.98}$ to four decimal places, i.e. -0.3356. We can now employ "1 minus" rule: $P(\bar{X} > 4) = P(Z > -0.3356) = 1 - P(Z \leq -0.3356)$:

# In[15]:


standardized2 = 1 - stats.norm.cdf(-0.3356, 0, 1)
standardized2


# ### Method 2 (using mean and sd arguments to stats.norm.cdf()):

# In this case, after calculating $\mu_{\bar{X}}=5$ (remember, $\mu_{\bar{X}}=\mu$, the mean of the average is the mean of each observation), and $ SD(\bar{X})=\frac{SD(X)}{\sqrt{n}}=\frac{20}{\sqrt{45}}\approx 2.98 $, we can simply plug this information into **stats.norm.cdf** and use "1 minus" rule:
# 
# $P(\bar{X} > 4) = 1 - P(\bar{X} \leq 4)$

# In[16]:


nonst2 = 1 - stats.norm.cdf(4, 5, 2.98)
nonst2


# Can you explain why there is a small difference in answer based on the method we used? Could rounding error have something to do with it??

# ## Calculating $P(2<\bar{X}<4)$ as the difference of $P(\bar{X}<4)$ and $P(\bar{X}<2)$:
# We already have shown (twice) that $\bar{X}\sim N(5, 2.98)$, at least approximately, so:

# In[17]:


pg2l4 = stats.norm.cdf(4, 5, 2.98) - stats.norm.cdf(2, 5, 2.98)
pg2l4


# Thus, $P(2 < \bar{X} < 4)$ is equal to 0.2116, rounded to 4 decimal places.

# # Solving Inverted Normal Problems with scipy.stats
# ## You may encounter the following inverted normal problem when working with sample averages:
# Consider $X \sim N(10, 2)$, and a sample of size 10 is taken from this distribution. Find two numbers $x_1$ and $x_2$, such that the center 25% of the distribution of $\bar{X}$ is between them.

# ## Solution:
# To get started, we first must find $z_0$ such that $P(-z_0 < Z < z_0) = 0.25$. Recall that $P(-z_0 < Z < z_0) = 0.25$ means that $2P(Z\leq z_0) - 1 = 0.25$ which means that $P(Z \leq z_0) = 0.625$. We can then use the **stats.norm.ppf()** function to find $z_0$:

# In[36]:


z_0 = stats.norm.ppf(0.625, 0, 1)
z_0


# Let's round $z_0$ to 4 decimal points, i.e. $z_0 = 0.3186$ is our answer. Now, we must find the value of $x$ that corresponds to $-z_0$, and the value that corresponds to $z_0$:
# 
# $-z_0 = \frac{x_1-10}{2/\sqrt{10}}$, and $z_0 = \frac{x_2-10}{2/\sqrt{10}}$ which means:
# 
# $x_1 = \frac{(-0.3186)\times 2}{\sqrt{10}} + 10$ and 
# 
# $x_2 = \frac{0.3186 \times 2}{\sqrt{10}} + 10$
# 
# The code below solves these equations:

# In[3]:


x_1 = -0.3186 * 2 / np.sqrt(10) + 10
x_2 = 0.3186 * 2 / np.sqrt(10) + 10
x_1


# In[38]:


x_2


# Thus, the middle 25 percent of the distribution of $\bar{X}$ is between approximately 9.80 and 10.20.
