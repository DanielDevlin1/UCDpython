#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Assign url of file: url
url = 'http://localhost:8888/edit/anaconda3/pgaTourData.csv'


# In[3]:


# Read file into a DataFrame: pga_df
pga_df = pd.read_csv ('pgaTourData.csv')
print(pga_df.head)


# In[4]:


# Sort by Player Name
pga_df.sort_values("Player Name")


# In[20]:


# Drop duplicates
pga_df.drop_duplicates()


# In[5]:


# Sort Player Name by Index
print(pga_df.sort_index())


# In[6]:


# Print the mean of Fairway Percentage 
avg_fp = print(pga_df["Fairway Percentage"].mean())


# In[7]:


# Average Fairway Percentage per Year
fp_per_year = print(avg_fp.group('Year').mean()['Fairway Percentage'])


# In[9]:


# Print Rounds and replace NAN with 0
pga_df['Rounds'].fillna(0, inplace=True)
print(pga_df)


# In[10]:


# Group by Player Name; calculate total gir
pga_by_gir = pga_df.groupby("Player Name")["gir"].sum()

# Get proportion for each type
pga_propn_by_gir = pga_by_gir / sum(pga_by_gir)
print(pga_propn_by_gir)


# In[21]:


# Create a dictionary of lists with new data
scratch_dict = {
  'Average Score': [71.35],
  'Par 3 Score': [3.16],
  'Par 4 Score': [4.09],
  'Par 5 Score': [4.76],
  'Birdies per round':[2.67],
  'Driving Accuracy':[49.9],
  'Driving Distance (yards)':[260],
  'GIR':[62],
  'Approach Proximity (feet)':[60.7],
  'Putts per Round':[29.3],
  '1 putt %':[37],
  'Up and Down %':[56],
  'Sand Saves %':[44.34]  
}

# Convert dictionary into DataFrame
scratch_df = pd.DataFrame(scratch_dict)

# Print the new DataFrame
print(scratch_df)


# In[25]:


# Merging Dataframes df_merged
merge_pga = pga_df.merge(Scratch_df, left_on='GIR', right_on='GIR', how='left')
print(merge_pga)


# In[13]:


# conditional Statement
a = 70
b = 71.35 # 71.35 = Average Score
if b > a:
  print("b greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# In[26]:


#Looping
i = 23
# 29.3 = Average putts per round
while i < 29.3:
  print(i)
  i += 1
else:
  print("i is no longer less than 29.3")


# In[ ]:


# define a custom function to create reusable code python


# In[15]:


# Numpy functions 1
# Import the numpy package as np
import numpy as np

# Create a numpy array from pga: np_pga
np_pga = np.array(pga_df)

# Print out type of np_pga
print(type(np_pga))


# In[30]:


# Numpy functions 2
# Import numpy
import numpy as np

# Create a numpy array from scratch_df : np_scratch
np_Scratch = np.array(Scratch_df)

# Print out np_scratch
print(type(np_Scratch)


# In[35]:


# Generate two charts using Matplotlib
# Import the matplotlib.pyplot and name it plt
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
# Plot a histogram of "Rounds" for pga_df
ax.hist(pga_df["Average Score"])

# Compare  histogram of "Average Score" for df_Scratch
ax.hist(df_Scratch["Average Score"])

# Set the x-axis label to "Average Score"
ax.set_xlabel("Average Score")

# Set the y-axis label to "differences"
ax.set_ylabel("differences")

plt.show()


# In[33]:


fig, ax = plt.subplots()

# using Fairway Percentage and Avg Distance as x-y, index as color
ax.scatter(pga_df["Fairway Percentage"], pga_df["Avg Distance"], c=pga_df.index)

# Set the x-axis label to "Fairway Percentage"
ax.set_xlabel("Fairway Percentage")

# Set the y-axis label to "Avg Distance"
ax.set_ylabel("Avg Distance")

plt.show()


# In[ ]:


#  Derive (explain) five valuable insights from the analysis
1) while excluding the typical outliers, the longer you hit the ball the less fairways youre bound to hit.

2) the longest average drive at 320 yards is just above 55% fairway percentage, when the pga average is 61%

3) meanwhile, one of the lower averaged players for driving distance at 280 yards has an 80% fairway perventage which is incredible 

4) the average score for pga pros is 70.5 strokes. only the top 20 will average in the mid to high 60's

5) The higher end of the average scores for the pga pros is 73.5 which will essentially mean they are at risk of loosing their tour card


# In[ ]:


# Justify your insights with reference to the charts or analysis (Above charts)
well, with graph number 1. it is seen that the median is between 70.5 and 71.5 with the outliers being in the 60's for some of the best players in the world
and 73.5 for some players who are struggling to get their game in shape. The whole reason I inteded to compare the Average scores between the pga pros and average scratch golfers was to show that there is a fenominal difference between struggling pga pros shooting low 70's and scratch golfers on form averaging a 72.
My goal for this project was to shed some light on how good the top 200 players in the world are and how it really is 1 in 1 million to become the next tour player.

With graph number 2, my goal was to show that while distance off the tee is so important, it's not more important then finding the fairway more constistently. its guarenteed the more fairways you miss, theres a higher risk of finding the water or Out of Bounds and loosing strokes to the field. 


# In[ ]:


# Describe what kind of prediction you could perform in future using machine learning and/or deep learning
The most accurate prediction that can be performed using machine learning is as each year players get better, we can start to generate higher green in regulation (GIR) stats and compare that to higher putting strokes gained (less putts per round due to a higher green in regulation percentage)
and accurately predict the average scores being lower. 


# In[ ]:


# Would you use classification or regression methods? (explain why)

I'd choose regression methods for machine learning because linear regression is the most consistent of the types of regression methods.
Linear models work for pretty much everything. e.g. To go back to my scatter plot with average driving distance, if a man was to speed train, he would gradually see another 5 yards increase for every 5 months he trained consistently. 
there will always be outliers, but the majority of anything follows a Linear model.


# In[ ]:





# In[ ]:




