#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

rn = random.randint(1, 100)   #rn (random number) the random number that the system will choose
guess = None

while guess != rn:
    guess = input("guess a number between 1 and 100 ")
    guess = int(guess)

    if guess == rn :
      print("you won")
            
    elif guess >= rn :
     print("it's lower")
    
    elif guess <= rn :
     print("it's highr")
    

#i didn't know how to stop the loop of the word ("guess a number between 1 and 100 ") i hope we will discuss that next session 
        
     


# In[ ]:





# In[ ]:




