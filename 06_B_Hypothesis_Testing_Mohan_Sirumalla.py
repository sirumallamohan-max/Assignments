#!/usr/bin/env python
# coding: utf-8

# # 06 B Hypothesis Testing
# ### HYPOTHESIS TESTING
# By **Mohan Sirumalla**
# ***

# **Background:**\
# Bombay hospitality Ltd. operates a franchise model for producing exotic Norwegian dinners throughout New England. The operating cost for a franchise in a week (W) is given by the equation W = $1,000 + $5X, where X represents the number of units produced in a week.\
# Recent feedback from restaurant owners suggests that this cost model may no longer be accurate, as their observed weekly operating costs are **higher**.\
# **Objective:**\
# To investigate the restaurant owners' claim about the increase in weekly operating costs using hypothesis testing.\
# **Data Provided:**
# - The theoretical weekly operating cost model: W = $1,000 + $5X
# - Sample of 25 restaurants with a mean weekly cost of Rs. 3,050
# - Number of units produced in a week (X) follows a normal distribution with a mean (μ) of 600 units and a standard deviation (σ) of 25 units
# 

# ## Assignment Tasks

# ### 1. State the Hypotheses statement:

# There a 2 main tyeps : 1) Null Hypothesis and 2) Alternative Hypothesis\
# weekly operating costs are **higher**.\
# Need to Calculate the weekly operating cost based on the forullla given


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[19]:


mean_units = 600 # given
Weekly_cost = 1000 +(mean_units * 5)
print(f"Mean_Unit :{mean_units}, Weekly Cost:{Weekly_cost}")
print(f"Null Hypothesis H0 of Wekely Cost is {Weekly_cost}")
print(f"Alternate Hypothesis H1 of Weekly Cost is Morethan {Weekly_cost}")



# Number of units produced in a week (X) follows a normal distribution with a mean (μ) of 600 units and a standard deviation (σ) of 25 units

# In[26]:


# get some sample data to represent normal distibution
polu_mean=600
polu_sd=25
sample_size=1000
data = np.random.normal(polu_mean, polu_sd, sample_size)
print("Actual Mean:", np.mean(data))
print("Actual Std Dev:", np.std(data))


plt.figure(figsize=(5, 3))
plt.hist(data, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title(f'Normal Distribution ($\mu={polu_mean}$, $\sigma={polu_sd}$)')
plt.xlabel('Units')
plt.ylabel('Density')
plt.axvline(data.mean(), color='k', linestyle='dashed', linewidth=2, label=f'Mean: {data.mean():.2f}')
plt.legend()
plt.show()


# ### 2. Calculate the Test Statistic:
# Use the following formula to calculate the test statistic(z):\
# where:\
# * $\bar{x}$ = sample mean weekly cost (Rs. 3,050)
# * μ = theoretical mean weekly cost according to the cost model (W = $1,000 + $5X for X = 600 units)
# * σ = 5*25 units
# * n = sample size (25 restaurants)
# 

# In[59]:


sample_mean_cost=3050
population_mean_cost=1000+(5*600)
population_std=5*25
sample_size=25
print("\u0078\u0304:", sample_mean_cost, "| μ:", population_mean_cost, "| σ:", polu_sd)


# Since the population standard deviation is known and the underlying distribution is normal, we use the Z-test statistic formula:
# $$Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$$

# In[61]:


Z=(sample_mean_cost-population_mean_cost)/(population_std/np.sqrt(25))
print(f"Z-test Statistics : {Z}")


# ### 3. Determine the Probability and compare:
# Using the alpha level of 5% (α = 0.05),
# Critical value for Alpha 0.05 from Z-Table
# Search the interior of a Standard Normal Distribution Table for the value closest to 0.9500.\
# The value \(0.9495\) corresponds to \(z=1.64\).\
# The value \(0.9505\) corresponds to \(z=1.65\).\
# Since \(0.9500\) is exactly halfway between these two values, the conventional practice is to interpolate and take the average of the two \(z\)-scores:\
# $z=\frac{1.64+1.65}{2}=1.645$

# ### 4. Make a Decision:
# Compare the test statistic with the critical value to decide whether to reject the null hypothesis.

# Using an alpha level of 5% (α = 0.05), for a **right-tailed test**,\

# In[76]:


alpha=0.05
area_left= 1- alpha
critical_value = (1.64+1.65)/2 # Z-table
p_value=1
print(f"area_left : { area_left}, critical_value{critical_value}, p-value: {p_value},alpha:{alpha} ")

if p_value <= alpha:
    print("Decision: Reject the null hypothesis (H0) because p-value <= alpha.")
else:
    print("Decision: Fail to reject the null hypothesis (H0) because p-value > alpha.")

#critical_value = stats.norm.ppf(1 - alpha)
print(f"Test Statistic: {Z:.4f}, Critical Value: {critical_value:.4f}")
if Z >= critical_value:
   print("Decision: Reject the null hypothesis (H0) because test statistic >= critical value.")
else:
   print("Decision: Fail to reject the null hypothesis (H0) because test statistic < critical value.")



# ### 5. Conclusion:
# Based on the decision in step 4, conclude whether there is strong evidence to support the restaurant owners' claim that the weekly operating costs are higher than the model suggests.
# 

# The test statistic is \(z=-38\). Since this value does not fall in the rejection region (\(z>1.645\)), we fail to reject the null hypothesis. There is no statistical evidence to support the restaurant owners' claim that weekly operating costs have increased

