#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


#to repeat an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


# In[4]:


output=np.ones((5,5))
print(output)


# In[ ]:


#NUMPY IN MATHEMATICS


# In[5]:


a=np.array([1,2,3,4])
a


# In[6]:


a+2


# In[7]:


a*2


# In[8]:


a/2


# In[9]:


b=np.array([1,0,1,0])
b


# In[10]:


a+b


# In[11]:


#Trigonometry
np.sin(a)


# In[12]:


np.cos(b)


# In[13]:


np.tan(a+b)


# In[ ]:


#Linear algebra


# In[15]:


a=np.ones((2,3))
a


# In[16]:


b=np.full((3,2),2)
b


# In[17]:


np.matmul(a,b)


# In[18]:


#to find the determinant
c=np.identity(3)
np.linalg.det(c)


# In[ ]:




