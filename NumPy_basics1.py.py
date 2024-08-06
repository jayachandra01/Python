#!/usr/bin/env python
# coding: utf-8

# In[64]:


# what is NumPy?
# it is a multidimensional array library (to store data in 1D,2D,3D arrays etc)
# it is faster than lists, because NumPy uses fixed types and uses less bytes of memory
# contiguous memory unlike lists ie all blocks of memory are right next to each other
# NumPy has a lot of additional features compared to lists eg: multiplication of vectors/matrices
# applications of NumPy: mathematics, plotting, backend, digital photography, machine learning


# In[65]:


import numpy as np


# In[66]:


a=np.array([1,2,3]) #1D array
a


# In[67]:


b = np.array([[2, 6, 8, 9, 0, 1], [3, 6, 8, 1, 4, 0]]) #2D array ie matrix
b


# In[68]:


a.ndim #get dimension


# In[69]:


b.ndim


# In[70]:


a.shape #length of array


# In[71]:


b.shape #rows and columns of matrix


# In[72]:


a.dtype


# In[73]:


b.dtype


# In[74]:


a.itemsize #size of each item in the array ie each int has 4 bytes


# In[75]:


b.itemsize


# In[76]:


a.size*a.itemsize #total size


# In[77]:


a.nbytes #total size, same as above


# In[78]:


b.nbytes 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




