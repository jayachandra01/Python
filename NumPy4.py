#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np


# In[16]:


#initializing many types of arrays


# In[17]:


np.zeros(5) #to create zero matrix


# In[19]:


np.zeros((2,3))


# In[20]:


np.zeros((2,3,3))


# In[21]:


np.zeros((2,3,3,2))


# In[22]:


np.ones((2,3)) #one matrix


# In[23]:


np.full((2,2),100) #any other number


# In[25]:


#random decimal numbers
np.random.rand(4,2)


# In[28]:


# Create a single 3x3 array of random numbers
single_array = np.random.rand(3, 3)

# Print the array
print(single_array)


# In[29]:


#to generate only integer values, 7 is the upper limit
np.random.randint(7,size=(3,3))


# In[30]:


#generates integer values between -100 and 100 
np.random.randint(-100,100,size=(3,3))


# In[31]:


#identity matrix
np.identity(3) 


# In[32]:


np.identity(10)


# In[ ]:




