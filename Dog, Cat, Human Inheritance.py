#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Dog:
    def __init__(self):
        pass
    
    def eat(self,animal_type,breed):
        print(f"The {animal_type} is eating and is a {breed}.")
        
    def sleeping(self,animal_type,breed):
        print(f"The {animal_type} is sleeping and is a {breed}.")
        
    def walking(self,animal_type,breed):
        print(f"The {animal_type} is walking and a {breed}.")


# In[30]:


class Cat(Dog):
    pass


# In[31]:


class Human(Cat):
    pass


# In[32]:


#What is an object and why do we need it?
#Objects are a copy of a class. We need it so we can get our own copy of it and use it which is how we get social media and video games.
#What is inheritance in python?
#When a class takes functions from another class.


# In[33]:


dog_obj = Dog()


# In[34]:


dog_obj.walking("Panda","weird")


# In[35]:


cat_obj = Cat()


# In[37]:


cat_obj.walking("Kitten","Sphinx")


# In[ ]:




