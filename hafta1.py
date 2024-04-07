#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=15
var1=25
x="çarşamba"

print(a)
print(var1)
print(x)
type(x)


# In[2]:


var1=15
var2=20
var3=25
list_int=[15,20,25]
print(list_int)


# In[3]:


list_int[0]


# In[4]:


list_int[-1]


# In[5]:


list_int[0:3]


# In[8]:


list_int.append(30)
print(list_int)


# In[9]:


list_int.remove(25)
print(list_int)


# In[10]:


list_int.reverse()
print(list_int)


# In[11]:


list_int.sort()
print(list_int)


# In[12]:


x=10
for each in list_int:
    if(each>x):
        x=each
    else:
        continue
print(x)


# In[13]:


i=0
while(i<5):
    print(i)
    i=i+1


# In[15]:


def cember_cevre(r,pi=3.14):  #Pi is default value
    result=2*pi*r
    return result
cember_cevre(3) 


# In[16]:


def hesapla(x):
    result=x*x
    return result
hesapla(7)


# In[17]:


result=lambda x:x*x
print(result(7))


# In[18]:


dictionary={"betül":25,"beyza":22,"irem":30} 
print(dictionary)


# In[19]:


type(dictionary)


# In[20]:


dictionary.keys()  


# In[21]:


dictionary.values()


# In[22]:


b=dictionary.keys()

if "betül" in b:
    print("yes")
else:
    print("no")


# In[ ]:




