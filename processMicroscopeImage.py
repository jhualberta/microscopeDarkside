# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:55:00 2018

@author: Amirber

Danial Papi 16 Nov, 2022
Jie Hu 23 Nov, 2022

Use openCV and skimage to analyze microscope slide showing particles.
image source and previous work from:
    https://publiclab.org/notes/mathew/09-03-2015/opt

Parts are adapted from: https://peerj.com/articles/453/
"""
from cv2 import imread, morphologyEx
import cv2
from skimage import data, color, io, filters, feature
import numpy as np
from numpy import sqrt, pi, multiply, power
import matplotlib.pyplot as plt
# Label image regions.
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label

imgPath = 'TestExample_sample4_8Nov_center_10times.png'
# Insert a um to pixel conversion ratio
um2pxratio = 0.22 ## 0.22 micrometer/pixel at 10x lens
image = imread(imgPath,0)# data.coins()  # or any NumPy array!

# remove noise
image = cv2.GaussianBlur(image,(3,3),0)

#save processed image
cv2.imwrite("processed_image.png", image)

# #Show histogram
# values, bins = np.histogram(image,
#                             bins=np.arange(256))
# plt.figure()
# plt.plot(bins[:-1], values)
# plt.title("Image Histogram")
# plt.show()

#Calculate Soble edges
edges_sob = filters.sobel(image)

# #Show histogram of non-sero Sobel edges
# values, bins = np.histogram(np.nonzero(edges_sob) ,
#                             bins=np.arange(1000))
# plt.figure()
# plt.plot(bins[:-1], values)
# plt.title("Use Histogram to select thresholding value")

#Using a threshold to binarize the images, consider replacing with an adaptice
# criteria. raisng the TH to 0.03 will remove the two tuching particles but will 
# cause larger oarticles to split.

edges_sob_filtered = np.where(edges_sob>0.01,280,0)

print(edges_sob)
print(edges_sob_filtered)
ret,th2_edge_sob = cv2.threshold(edges_sob,0,255,cv2.THRESH_BINARY_INV)
cv2.imwrite("edges_sob_filtered.png", th2_edge_sob)


#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges_canny = cv2.Canny(image,10,100)

contours, _ = cv2.findContours(edges_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0,0,255), thickness = 2)

contour_area = []
print("found ", len(contours), "contours of dust particles.")
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    contour_area.append(area)

print("contour area", contour_area)

ret,th2 = cv2.threshold(edges_canny,0,255,cv2.THRESH_BINARY_INV)
## cv2.imshow("img",th2)
cv2.imwrite("edges_canny.png", th2)


#Use lable on binnary Sobel edges to find shapes
label_image = label(edges_sob_filtered)
fig,ax = plt.subplots(1,figsize=(20,10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('Labeled items', fontsize=24)
ax.axis('off')

#Do not plot regions smaller thn 5 pixels on each axis
sizeTh=10
### calculate by rectangle area
for region in regionprops(label_image):
    # Draw rectangle around segmented coins.
    if ((region.bbox[2]-region.bbox[0])>sizeTh and (region.bbox[3] - region.bbox[1])>sizeTh):
        
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr),
                                maxc - minc,
                                maxr - minr,
                                fill=False,
                                edgecolor='red',
                                linewidth=2)
        ax.add_patch(rect)

#Sort all found shapes by region size
# area by square
sortRegions = [[(region.bbox[2]-region.bbox[0]) * (region.bbox[3] - region.bbox[1]),region.bbox] 
                for region in regionprops(label_image) if
                ((region.bbox[2]-region.bbox[0])>sizeTh and (region.bbox[3] - region.bbox[1])>sizeTh)]
sortRegions = sorted(sortRegions, reverse=True)

#Check particle sizes distribution
particleSize = [size[0] for size in sortRegions]
particleRadius  = [sqrt(size[0]/pi) for size in sortRegions]
particleMass = [] ### volume = 4./3*pi*pow(radius,3);
##      double mass = volume*0.001;
## h.Fill(radius,mass)

check_list_area = [val for val in np.multiply(np.power(um2pxratio,2), particleSize)]
check_list_radius = [val for val in np.multiply(np.power(um2pxratio,2), particleRadius)]

#Show histogram of non-sero Sobel edges
plt.figure()
plt.hist(check_list_radius, bins=20,linewidth=2)
plt.xlabel('Particle radius',fontsize=14)
plt.ylabel('Particle count',fontsize=14)
plt.title("Particle area distribution",fontsize=16)
plt.show()
#show 5 largest regions location, image and edge
answer = input("show 5 largest regions location, image and edge (y/n): ") 
if answer == 'y':
   for region in sortRegions[:5]:
       # Draw rectangle around segmented coins.
       minr, minc, maxr, maxc = region[1]
       fig, ax = plt.subplots(1,3,figsize=(15,6))
       ax[0].imshow(image, cmap=plt.cm.gray)
       ax[0].set_title('full frame', fontsize=16)
       ax[0].axis('off')
       rect = mpatches.Rectangle((minc, minr),
                             maxc - minc,
                             maxr - minr,
                             fill=False,
                             edgecolor='red',
                             linewidth=2)
       ax[0].add_patch(rect)
   
       ax[1].imshow(image[minr:maxr,minc:maxc],cmap='gray')
       ax[1].set_title('Zoom view', fontsize=16)
       ax[1].axis("off")
       ax[1].plot([0.1*(maxc - minc), 0.3*(maxc - minc)],
                [0.9*(maxr - minr),0.9*(maxr - minr)],'r')
       ax[1].text(0.15*(maxc - minc), 0.87*(maxr - minr),
             str(round(0.2*(maxc - minc)*um2pxratio,1))+'um',
             color='red', fontsize=12, horizontalalignment='center')
   
       ax[2].imshow(edges_sob_filtered[minr:maxr,minc:maxc],cmap='gray')
       ax[2].set_title('Edge view', fontsize=16)
       ax[2].axis("off")
       ## plt.show()
   

# Find contours, calculate areas (pixels), sum to get whole area (pixels) for certain level
### cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
### cnts = cnts[0] if len(cnts) == 2 else cnts[1]
### area = np.sum(np.array([cv2.contourArea(cnt) for cnt in cnts]))
### 
### # Whole area (coordinates) from canvas area (pixels), and x_min, x_max, etc.
### area = area / np.prod(mask.shape[:2]) * (x_max - x_min) * (y_max - y_min)
### print('Area:', area)


# #Show 5 smallest regions location, image and edge
# for region in sortRegions[-5:]:
#     # Draw rectangle around segmented coins.
#     minr, minc, maxr, maxc = region[1]
#     fig, ax = plt.subplots(1,3,figsize=(15,6))
#     ax[0].imshow(image, cmap=plt.cm.gray)
#     ax[0].set_title('full frame', fontsize=16)
#     ax[0].axis('off')
#     rect = mpatches.Rectangle((minc, minr),
#                           maxc - minc,
#                           maxr - minr,
#                           fill=False,
#                           edgecolor='red',
#                           linewidth=2)
#     ax[0].add_patch(rect)

#     ax[1].imshow(image[minr:maxr,minc:maxc],cmap='gray')
#     ax[1].set_title('Zoom view', fontsize=16)
#     ax[1].axis("off")
#     ax[1].plot([0.1*(maxc - minc), 0.3*(maxc - minc)],
#              [0.9*(maxr - minr),0.9*(maxr - minr)],'r')
#     ax[1].text(0.15*(maxc - minc), 0.87*(maxr - minr),
#           str(round(0.2*(maxc - minc)*um2pxratio,1))+'um',
#           color='red', fontsize=12, horizontalalignment='center')

#     ax[2].imshow(edges_sob_filtered[minr:maxr,minc:maxc],cmap='gray')
#     ax[2].set_title('Edge view', fontsize=16)
#     ax[2].axis("off")
#     plt.show()
    
#Add fractal dimension estimation https://github.com/scikit-image/scikit-image/issues/1730

print( "particle size (um^2)", np.multiply(np.power(um2pxratio,2), particleSize) )
print( "particle radius (um)", np.multiply(np.power(um2pxratio,2), particleRadius) )

