#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[68]:


array2=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("Vector:",array2)
a=array2.reshape(3,5)
print("Two dimensional array:",a)


# In[69]:


print("shape:",a.shape)
print("dimension:",a.ndim)
print("data type:",a.dtype.name)
print("size:",a.size)
print("type:",type(a))


# In[70]:


x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y)
print(x-y)
print(x**2)


# In[71]:


a=np.array([3,4,5])
d=a.copy()
print(d)
b=a
c=a
b[0]=5
print(a,b,c)


# In[73]:


a=np.array([3,4,5,6,7,8,9])
print(a[0])
print(a[0:5])


# In[74]:


reverse_array=a[::-1]
print(reverse_array)


# In[76]:


b=np.array([[6,7,8,9,10],[1,2,3,4,5]])
print(b)
print(b[1,1])
print(b[:,1])
print(b[1,:])
print(b[1,1:4])
print(b[-1,:])
print(b[:,-1])


# In[77]:


import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)

plt.hist(data,bins=30)
plt.title("histogram")
plt.xlabel("Values")
plt.ylabel("Frequencies")
plt.show()


# In[78]:


sizes=[30,25,15,10,5,5]
plt.pie(sizes)
plt.title("Pie Chart")
plt.show()

