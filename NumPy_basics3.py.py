#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[6]:


b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
b


# In[7]:


#get a specific element (work outside in)
b[0,1,1]    #0 is 1st matrix, 1 is 2nd row, 1 is second element ie element 4


# In[8]:


b[:,1,:]


# In[9]:


#just for visualisation
[
  [
    [1, 2],  # b[0, 0, :]
    [3, 4]   # b[0, 1, :]
  ],
  [
    [5, 6],  # b[1, 0, :]
    [7, 8]   # b[1, 1, :]
  ]
]


# In[11]:


#replace (for rows)
b[:,1,:]=[[9,9],[8,8]]
b


# In[12]:


#replace (for columns)
b[:, :, 1] = [[9, 9], [8, 8]]
b


# In[ ]:





# In[ ]:





# In[ ]:




