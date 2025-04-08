#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Create List 

fruits = ["Mango", "Banana", "Orange"]

fruits


# In[2]:


print(fruits)


# In[3]:


type(fruits)


# In[4]:


print(fruits[2])


# In[5]:


print(fruits[0])


# In[6]:


# Modifying List
fruits[0] = "Cheery"


# In[7]:


print(fruits)


# In[8]:


fruits[0]


# In[9]:


fruits = "Guava"


# In[12]:


print(fruits)


# In[38]:


# Tuple in python

colors = ('red', 'green', 'blue')


# In[39]:


colors


# In[15]:


type(colors)


# In[16]:


colors[1]


# In[41]:


fruits


# In[42]:


fruits.append("guava")


# In[43]:


fruits


# In[44]:


fruits.append("Pomogranate")


# In[45]:


print(fruits)


# In[46]:


fruits.insert(3,3)


# In[47]:


fruits


# In[50]:


a = [1,2]
b = [3,4]

c = a+b


# In[51]:


c


# In[53]:


a = [1,2,3]
b = [3,5,6]

c = a+b
c


# In[54]:


# Get square of even number of list

num = [1,2,3,4,5,6]

square = [x**2 for x in num if  x%2 == 0]
print(square)


# In[55]:


num = [2,4,5,6,7,8,9,10]

square = [x**2 for x in num if x % 2 == 0]

print(square)


# In[56]:


num1 = [2,3,4,5,6,7,8]
square = [x**2 for x in num1 if x % 2 == 0]
print(square)


# In[57]:


# nested List

nested = [[1,2], [3,4], [4,5]]

flattent_list= [item for sublist in nested for item in sublist]

print(flattent_list)


# In[58]:


nested = [[2,3], [2,4], [4,5], [6,7]]

counting_list = [item for sublist in nested for item in sublist]

counting_list


# In[60]:


# Remove duplicates

items = [1,2,2,3,3,4,4,4]

unique = []

[unique.append(x) for x in items if x not in unique]


print(unique)


# In[61]:


items = [2,2,2,3,3,3,4,44,5,5,5]

unique = []

[unique.append(x) for x in items if x not in unique]
print(unique)


# In[ ]:




