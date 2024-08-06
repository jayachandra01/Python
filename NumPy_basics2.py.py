#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

# Create a 2D NumPy array
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Print the array
print(a)


# In[8]:


#get a specific element (row,column)
a[1,5]


# In[9]:


a[0,: ] #to get a specific row


# In[10]:


a[:, 2] #to get a specific column


# In[11]:


# [startindex:endindex:stepsize]
a[0, 1:6:2] #gives us ele 2 to 6 by steps of 2 ie 2,4,6


# In[12]:


a[1,5]=20 #changes fifth element of 2nd row to 20
print(a)


# In[14]:


a[:,2]=[1,2] #to change the second column to 1,2
print(a)


# In[15]:


a[:,2]=5 #to change the second column to 5
print(a)


# In[ ]:




