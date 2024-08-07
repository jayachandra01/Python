#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


#STATISTICS USING NUMPY


# In[4]:


stats=np.array([[1,2,3],[4,5,6]])
stats


# In[5]:


np.min(stats) #minimum element in the matrix


# In[6]:


np.max(stats) #maximum element in the matrix


# In[7]:


np.sum(stats) #sum of all elements in the matrix


# In[ ]:


#Reorganising arrays


# In[8]:


before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)


# In[9]:


after=before.reshape((8,1))
print(after)


# In[10]:


after=before.reshape((4,2))
print(after)


# In[11]:


#vertically stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([4,5,6,7])

np.vstack([v1,v2])


# In[12]:


#horizontally stacking vectors
np.hstack([v1,v2])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




