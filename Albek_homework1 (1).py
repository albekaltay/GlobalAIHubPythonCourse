#!/usr/bin/env python
# coding: utf-8

# In[28]:


list_one = [1,3,5,7,9]
list_two = [0,2,4,6,8]
list_merge = list_one + list_two

new_list  =  [i * 2 for i in list_merge]

for a in new_list:
    print(f"number: {a} - type: {type(a)}")


# In[ ]:




