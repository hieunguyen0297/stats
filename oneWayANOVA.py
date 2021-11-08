#!/usr/bin/env python
# coding: utf-8

# <h1><center>PBHL B302 Biostatistics for Informatics</center><h1>
# <h2><center>Lecture 7: One-way Analysis of Variance (ANOVA)<br> Spencer Lourens, Ph.D.</center><h2>

# In[5]:


import scipy.stats as stats
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ## Learning objectives: 
# - Learn how to perform one-way analysis of variance in Python using **scipy.stats**
# - Learn how to create ANOVA table and gather more in depth information in Python using **statsmodels**
# 

# ### Calculating a one-way ANOVA
# First, use **pandas** to import the bone.csv data:

# In[8]:


bone = pd.read_csv("/Path/To/bone.csv")
bone


# Before proceeding, let's make some side by side boxplots to explore the data by group:

# In[38]:


bone.boxplot(by = 'Group')
## to make title look better
plt.title("")
## change "Boxplot grouped by Group"
plt.suptitle("Boxplot of Bone Density by Group")
plt.ylabel("Bone Density")
plt.xlabel("Group Membership")
plt.show()


# As can be seen above, there is some evidence that the groups have different means, but a statistical test is necessary to determine whether this may be due to chance alone.
# 
# It is also helpful to calculate means and SDs by group so that we can assess the SD rule learned in the notes (the largest SD should not be more than 2 times the smallest SD):

# In[39]:


## group means
bone.groupby('Group').mean()


# In[40]:


## group SDs
bone.groupby('Group').std(ddof = 1)


# In[41]:


## counts
bone.groupby('Group').count()


# Thus, $n_1=n_2=n_3=10$. **NOTE**: Be sure to remember that it's the number of bone density (outcome) measurements that mater here, just in case there is missing data. The number of observations in each treatment group is what matters, not the number of rows in each treatment group. Missing data could be a problem, for instance, if one group only had 7 observations, we'd want to take that into account when documenting the sample size above!
# 
# The function **stats.scipy.f_oneway()** may be used to conduct one-way ANOVA, but each sample must be entered as a separate argument to the function. First, let's split our sample into multiple datasets:
# 
# Because all that is really needed is the bone density measures (variable **BoneDensity** in **bone** dataframe), we can just extract these values and keep those corresponding to each group.

# In[16]:


bone1 = bone['BoneDensity'][bone['Group']==1]
bone2 = bone['BoneDensity'][bone['Group']==2]
bone3 = bone['BoneDensity'][bone['Group']==3]


# Now, using our newly created vectors for each group, use the **stats.scipy.f_oneway()** function:

# In[43]:


F, p = stats.f_oneway(bone1, bone2, bone3)


# Thus, the $F$-statistic value is:

# In[44]:


F


# and the $p$-value is

# In[45]:


p


# Thus, there is sufficient statistical evidence to conclude that there is a difference in bone density by group.

# We can also use the **statsmodels** package (imported as **sm**) to fit an ordinary least squares model for **BoneDensity** in terms of **Group**, and then create an ANOVA table using this information:
# 
# We must create a character version of the **Group** variable in order for this model to work correctly, or **statsmodels** will interpret the **Group** variable as being numeric (since it is coded as numeric), when we really want to represent **Group** as a categorical or string variable. We can use nested **np.where()** calls to do this:

# In[10]:


bone['GroupC'] = np.where(bone['Group'] == 1, "One", np.where(bone['Group'] == 2, "Two", "Three"))


# The code above creates a new variable, **GroupC**, and assigns the value "One" where **Group** is equal to 1, then checks where **Group** is equal to 2, and assignes the value "Two", and otherwise, the value is set to "Three"

# In[11]:


mod = ols("BoneDensity ~ GroupC", bone).fit()
anovaTbl = sm.stats.anova_lm(mod, typ = 2)
anovaTbl


# As can be seen above, the $I-1 = 2$ is the degree of freedom for groups (DFG), $N-I = 27$ is the degree of freedom for the residual (DFE), and the total degrees of freedom is $N-1=29$ (DFT). Also, recall that the $F$-statistic can also be calculated using the formula $F = MSG/MSE$:

# In[12]:


MSG = anovaTbl['sum_sq'][0]/anovaTbl['df'][0]
MSE = anovaTbl['sum_sq'][1]/anovaTbl['df'][1]
F = MSG/MSE
F


# As can be seen above, we observe the same $F$-statistic and $p$-values as using the **scipy.stats** functions. However, we now get the between group (**GroupC**) and within group (**Residual**) sums of squares, and their degrees of freedom! You can also easily calculate $s_p$ from this output:

# In[13]:


sp = np.sqrt(MSE) ## MSE = SSE / DFE - sp = sqrt(MSE)
sp


# To calculate the $R^2$ value, one can just divide the SSG by the SST. However, the anova table above does not give us the SST. This is found by summing up all of the squares of the data minus the **grand mean** as is done in the cell below. Then the R^2 is not difficult to find:

# In[14]:


meanBD = np.mean(bone['BoneDensity'])
SST = np.sum((bone['BoneDensity'] - meanBD)**2)
R2 = anovaTbl['sum_sq'][0] / SST
R2


# As can be seen, 37.1% or so of the variabiltiy in bone density was explained by the groups, control, low jump, and high jump! This is how we interpret the $R^2$ value here.

# ### Multiple comparisons: Bonferroni adjustment
# 
# If a significant effect is found when conducting ANOVA, you may use a Bonferroni adjustment to determine which of the groups being compared actually differ. **REMEMBER**: only do this after finding a significant effect when running the one-way ANOVA analysis using **scipy.stats.f_oneway()** or **statsmodels.api.stats.anova_lm()**. To conduct the Bonferroni adjustment, we first need to conduct all possible two-independent sample tests and gather the $p$-values. Sadly, we CANNOT use the **scipy.stats.ttest_ind()** or other functions which conduct two-sample independent $t$-tests. The reasons for this are pretty theoretical, and beyond the scope of this class. The code below does three things: 
# 
# (1) Calculates the test statistic (using the estimate for the pooled variance from anova, $s^2_p = \sqrt{MSE}$ calculated earlier
# 
# (2) Calculates the unadjusted $p$-values for each pairwise test (there are three of them). Notice that the degrees of freedom (df) are equal to $N-I$, just as they were in the ANOVA. This has to do with theoretical estimation issues that you might learn in an advanced Statistics course. For now, just remember that when you are adjusting for multiple comparisons, the df is $N-I$, i.e. the total number of observations minus the number of groups.
# 
# (3) Finally, the $p$-values are gathered into variable **ptup**:

# In[17]:


## create datasets for each group

p1 = 2 * (1 - stats.t.cdf(np.abs((np.mean(bone1)-np.mean(bone2)) / 
                                    (sp * np.sqrt(1 / len(bone1) + 1 / len(bone2)))), 
                                    len(bone1) + len(bone2) + len(bone3) - 3))
p2 = 2 * (1 - stats.t.cdf(np.abs((np.mean(bone2)-np.mean(bone3)) / 
                                    (sp * np.sqrt(1 / len(bone2) + 1 / len(bone3)))), 
                                    len(bone2) + len(bone2) + len(bone3) - 3))
p3 = 2 * (1 - stats.t.cdf(np.abs((np.mean(bone1)-np.mean(bone3)) / 
                                    (sp * np.sqrt(1 / len(bone1) + 1 / len(bone3)))), 
                                    len(bone1) + len(bone2) + len(bone3) - 3))
ptup = (p1, p2, p3)
ptup


# Now, use function **statsmodels.sandbox.stats.multicomp.multipletests**, passing **ptup** as the first argument, **alpha** (the significance level, usually 0.05), and the **method** of adjustment (here, Bonferroni):

# In[18]:


reject, adjusted, ps, ps2 =  statsmodels.sandbox.stats.multicomp.multipletests(ptup, alpha = 0.05, method = 'Bonferroni')
## rejection decisions using multiple comparisons:
reject


# Notice that the **multipletests()** function provides a couple of other pieces of information we don't need to use. These values essentially tell an analyst what the adjusted type I error rate is under two distinct calculation paradigms. There are **MANY** ways to adjust for multiple testing. You only need to understand the concept and know how to adjust for Bonferroni in this class.

# In[19]:


## adjusted p-values using Bonferroni
adjusted


# Thus, the test comparing bone1 and bone2, i.e. groups 1 and 2 (control and lowjump) should not be rejected using multiple comparisons ($p = 0.74$). However, there is sufficient statistical evidence to conclude that the mean bone density after 6 weeks differs between the low jump and high jump groups (2 and 3, $p \approx 0.034$) and the control and high jump groups (1 and 3, $p \approx 0.002$) 
