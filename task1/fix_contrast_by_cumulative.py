
# This program is written to Fix a Low-Contrast Gray-Scale Image using cumulative function in Python 
 
#importing the required packages
import cv2 as c1
import numpy as np
import matplotlib.pyplot as plt

#read an display the image file
z = c1.imread('Low_Contrast.png')

#Convert into greyscale image
x = c1.cvtColor(z, c1.COLOR_BGR2GRAY)

#Create a histogram array
hist1, bins1=np.histogram(x.flatten(), 256, [0, 256])
print('Histogram array...')
print(hist1)
#find the cumulative sum
cms=hist1.cumsum()
print('Cumulative Sum...')
print(cms)
#Normalize the cumulative sum
cms_n=cms*float(hist1.max())/cms.max()
print('Normalized sum...')
print(cms_n)

#Plotting the histogram
plt.plot(cms_n, color='b')
plt.hist(x.flatten(), 256, [0, 256], color='r')
plt.show()

#Histogram Equalization and its plot
y = c1.equalizeHist(x)
hist1, bins1=np.histogram(y.flatten(), 256, [0, 256])
print('Histogram array...')
print(hist1)
cms=hist1.cumsum()
print('Cumulative Sum...')
print(cms)
cms_n=cms*float(hist1.max())/cms.max()
print('Normalized sum...')
print(cms_n)
plt.plot(cms_n, color='b')
plt.hist(y.flatten(), 256, [0, 256], color='r')
plt.show()

#stacking images
w=np.hstack((x, y))
#c1.imshow('Original Image', z)
c1.imshow('Transformed Images', w)
c1.waitKey()
