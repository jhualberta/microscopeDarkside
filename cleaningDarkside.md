## Cleanliness Control Programs at University of Alberta

Aksel Hallin, Jie Hu and Danial Papi

University of Alberta



The aim is to design and implement a cleaning procedure for the Darside-50 experiment.

cleanliness quality assurance protocols

additional radioactive contaminants are not introduced into the detector

This document is largely derived from [1].



#### Microscope Analyzing Platform



**Light Source for different Materials**

- Opaque 

metals, polymer-like materials such as  PTFE 

ultraviolet lights

- Translucent/Transparent

glass, acrylic

visible lights 



Motorized X-Y table



#### Cleaning Procedures

Items for cleaning will be cleaned in different ways depending on their sizes and the materials they were made of.

For example, the acrylic materials will never be washed by liquid containing alcohol. 

Compatibility of the materials with the certain cleaning chemicals must be checked.



**Large items**

- PMTs

- TPC components

Volume of the ultrasonic cleaner

**Small items**





ultra-pure water (UPW)





Rough Cleaning

If items are visibly dirty, greasy, or contaminated, they should be rough-cleaned.

Cleaning

Nitrogen gas flow cleaning

flow rate 25 lpm, flow 30 minutes.



An X-Y table can hold the sample tightly and moving by 1 mm (?) steps automatically. Then for a 1-cm$^2$ area, 100 scans needs to be performed. 



- Exposure to gas Argon and liquid Argon



Set up a multiple-purpose Argon system











Do we really need a color information? Does the color give us more information?

Tape lift 



#### Clean Room Monitoring

Several monitoring parameters of the clean room determine the dust fall out rates based on the SNO dust model.

Clean room air exchange rate $R_{AE}$

clean room volume $V$





Humidity (LZ lowest rate: 25 %, normal relative levels: 35-45 %)



Deionizing fans around the assembly to remove static charges on polymer-like materials to keep samples neutral to avoid attracting dusts



Plate-out

radon-laden air



radon-reduced clean room (RCR)

LZ ambient radon level averaging (< 0.5 Bq/m$^3$)

RCR recirculation rate:  8500 cubic feet per minute

plate-out rates onto materials

clean room setting

 







Moved into aluminized mylar and nylon bags to against Rn penetration



After cleaning in the L2-116, the items needs to be transferred to the Clean Room carefully.

sealed box and cart



#### Dust Data Analysis

Determine the dust fallout rate



(From Aksel)

Establish and verify monitoring techniques. 

Optical microscopy seems to be general tool of choice; perhaps with different light sources, and probably with a moving stage to enable sampling of sufficiently large areas. 

Measure deposition rates in various locations and various situations. Establish cleaning procedures. Measure rate at which liquid argon removes dust from surfaces.





### Software

The codes are available on GitHub: https://github.com/jhualberta/microscopeDarkside .

We can utilize two different software: Python Scikit and ImageJ.  OpenCV2

ImageJ is used in microscope images. 

Python package is more flexible and we can add in custom feature such as machine-learning in the future.

Zeiss dust particle has a commercial AI image processing. 



 

##### Python Scikit Image





Area calculation:

Find the edge and contour, then calculate the area of the contour

convex hull

Sobel operator

Canny algorithm



Hough transformation

pick up line or circle shape



##### ImageJ



https://forum.image.sc/

ImageJ2 (Fiji)Provide command line macro, batch processing and cluster computing.

java -jar path_to_install/Fiji.app/jars/ij-1.53t.jar -ijpath path_to_install/Fiji.app -macro processImage.ijm path_to_save

tif files



Automatic counting

https://imagej.net/imaging/particle-analysis

waterShed tool



Compare the analysis

TestExample_sample4_8Nov_center_10times.png











### References

[1] Akerib, D. S., et al. "The LUX-ZEPLIN (LZ) radioactivity and cleanliness control programs." *The European Physical Journal C* 80.11 (2020): 1-52.

[2]

[3]
