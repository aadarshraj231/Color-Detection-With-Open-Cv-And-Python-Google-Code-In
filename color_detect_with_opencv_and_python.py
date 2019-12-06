#!/usr/bin/env python
# coding: utf-8

# In[42]:


#importing cv2 module for computer visison 
import cv2
#importing matplotlib for ploting 
import matplotlib.pyplot as plt
#import numpy for mathematical and matrices 
import numpy as np


# In[46]:


#read image with cv2.imread
img=cv2.imread("img_1.jpg")


# In[47]:


#plotting a figure on matplolib
plt.figure(figsize=(20,8))
plt.imshow(img)
plt.show()


# In[48]:


#BGR=Blue,Green,Red  RGB=Red,Green,Blue
#convert image into BGR2RGB
cvt_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# In[49]:


#plotting a figure on matplotlib after Converting 
#BGR 2 RGB
plt.figure(figsize=(20,8))
plt.imshow(cvt_rgb)
plt.show()


# In[50]:


#converting BGR2HSV (hue, saturation, lightness)
cvt_hsv=cv2.cvtColor(cvt_rgb,cv2.COLOR_RGB2HSV)


# In[65]:


#In Array there are three values 1 is hue 2nd is saturation 3rd is lightness of image

#this is for black
lower_black = np.array([0,0,0])
upper_black = np.array([250,255,30])

#this is for white
lower_white = np.array([0,0,255])
upper_white = np.array([0,0,255])

#this is for red
lower_red = np.array([0,150,50])
upper_red = np.array([10,255,255])

#this is for green
lower_green = np.array([45,150,50])
upper_green = np.array([65,255,255])

#this is for yellow
lower_yellow = np.array([23,41,133])
upper_yellow = np.array([40,150,255])

#this is for light_blue
lower_light_blue = np.array([95,150,0])
upper_light_blue = np.array([110,255,255])

#this is for orange
lower_orange = np.array([15,150,0])
upper_orange = np.array([25,255,255])

#this is for dark_pink
lower_dark_pink = np.array([160,150,0])
upper_dark_pink = np.array([170,255,255])

#this is for pink
lower_pink = np.array([145,150,0])
upper_pink = np.array([155,255,255])

#this is cyan
lower_cyan = np.array([85,150,0])
upper_cyan = np.array([95,255,255])

#this is for dark_blue
lower_dark_blue = np.array([115,150,0])
upper_dark_blue = np.array([125,255,255])


# In[71]:


#mask_1 for color light_blue
mask_1=cv2.inRange(cvt_hsv,lower_light_blue,upper_light_blue)
#mask_2 for color red
mask_2=cv2.inRange(cvt_hsv,lower_red,upper_red)
#mask_3 for color yellow
mask_3=cv2.inRange(cvt_hsv,lower_yellow,upper_yellow)


# In[72]:


#final mask and masked. for combine mask_1 mask_2 mask_3 i use (bitwise_or) operator
mask=cv2.bitwise_or(mask_1,mask_2,mask_3)
target_color=cv2.bitwise_and(img,img,mask=mask)


# In[73]:


#plotting a figure after hue and mask
plt.figure(figsize=(20,8))
plt.imshow(mask)
plt.show()


# In[74]:


#after bitwise_or i using bitwise_and operator for right color detection
bitwise=cv2.bitwise_and(cvt_rgb,cvt_rgb,mask=mask)


# In[75]:


#plotting a figure after bitwise operator
plt.figure(figsize=(20,8))
plt.imshow(bitwise)
plt.show()


# In[ ]:




