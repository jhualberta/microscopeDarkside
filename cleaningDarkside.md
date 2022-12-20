# Cleanliness Control Programs at University of Alberta

Author: Aksel Hallin, Jie Hu and Danial Papi

University of Alberta

## Abstract

The aim is to design and implement a cleaning procedure for the Darside-50 experiment.

cleanliness quality assurance protocols

additional radioactive contaminants are not introduced into the detector

This document is largely derived from [1].



### Dust Measurement Devices



#### Microscope Analyzing Platform



Multiple USB-microscope system in a Changeable Frame

Skybasic 50X-1000X Magnification WiFi Portable Handheld Microscopes

 16.21 x 11.71 x 4.7 cm; 322 Grams



 A jig constructed from extruded aluminum framing





**Light Source for Different Materials**

- Opaque materials 

The light-opaque materials include metals (such as aluminum, stainless steel, copper, or titanium), polymer-like materials (such as  PTFE, teflon). 

For these opaque materials, the light source is required to from the top. The metal parts can be shinny or dark.

Ring light or ultraviolet light.



- Translucent/Transparent

The light-translucent or transparent materials include acrylic/PMMA, glass

visible lights 

from the bottom.



**Motorized X-Y table**

A motorized X-Y table automatically scans the samples can save people time and reduce the personnel activities in the clean room. 

Price





### Cleaning Procedures

Items for cleaning will be cleaned in different ways depending on their sizes and the materials they were made of.

For example, the acrylic materials will never be washed by liquid containing alcohol. 

Compatibility of the materials with the certain cleaning chemicals must be checked.



**Large items**

- PMTs

- TPC components

Volume of the ultrasonic cleaner

**Small items**





ultra-pure water (UPW)





#### Rough Cleaning

Steps

Items that are visibly dirty, greasy or otherwise contaminated should be rough-cleaned as appropriate.
This can be accomplished with brushes, rags, solvent or detergent solution as appropriate and followed
with a tap-water rinse. Isopropyl alcohol will usually remove most residue; acetone can be used but
care should be taken around plastics. Acetone cleaning should be followed by an isopropyl alcohol rinse
which will help remove residual acetone. Items should be washed and rinsed until no significant dirt,
grease or contaminants are visible. Tubes or pipes should be scrubbed internally with pipe cleaners and
a warm (best for 60 $^\circ$C, but be careful with the chemical compatibility of the materials!) 

1% Alconox [4] solution, and then rinsed with tap water. Items that will be welded or citric acid
passivated should be ultrasonically cleaned (with either tap water or UPW) and rinsed with tap water
then allowed to dry.

UPW at least run for 5 minutes

Handled with powder-free polyethylene gloves



Ultra-sonic clean

If the cleanliness/history
of the cleaning solution is unknown, the cleaner should be emptied, rinsed, and refilled. 



Cleaning

Nitrogen gas flow cleaning

flow rate 25 lpm, flow 30 minutes.



Hand vacuum/car vacuum



rinsing tanks



rough-cleaned, polished, buffed or ground to
remove weld discoloration and then passivated, then cleaned according to the standard procedure
below.



An X-Y table can hold the sample tightly and moving by 1 mm (?) steps automatically. Then for a 1-cm$^2$ area, 100 scans needs to be performed. 



- Exposure to gas Argon and liquid Argon



Set up a multiple-purpose Argon system



#### Acrylic aka PMMA Chemical Compatibility Chart 

https://www.industrialspec.com/resources/acrylic-aka-pmma-chemical-compatiblity-chart/acrylic-aka-pmma-chemical-compatiblity-chart-i-j-k-l/

![image-20221207143533628](image-20221207143533628.png)



Do we really need a color information? Does the color give us more information?

Tape lift 



### Storage and Transfer



vacuum storage bags

Ultra High Vacuum (UHV) Aluminum or polyethylene film and capped,   

taped with masking tape (preferably green painter’s tape) [2]

Tape should not be used on surfaces that will be welded (since fabricators may not properly clean residual glue before welding)

polyethylene bags





List of Price

UHV AL Foil  18''wide  500 ft long,  0.0015'' thickness  part number FOILA18.0015   Can$575.51



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





##### Software

The codes are available on GitHub: https://github.com/jhualberta/microscopeDarkside .

We utilize two different software: Python Scikit and ImageJ.  Both of the two software are platform independent, which requires minimum efforts to run on Linux, windows and MacOS.



OpenCV2

ImageJ is used in microscope images. 

Python package is more flexible and we can add in custom feature such as machine-learning in the future.

Zeiss dust particle has a commercial AI image processing. 



 

###### Python Scikit Image

Area calculation:

Find the edge and contour, then calculate the area of the contour

###### Convex hull

###### Sobel operator

###### Canny algorithm

###### Hough transformation

pick up line or circle shape



##### ImageJ

ImageJ is available on https://imagej.nih.gov/ij/. A manual and developer resources can also be found on the website.

We recommend to use Fiji (download and install via https://imagej.net/software/fiji). Fiji is a distribution of ImageJ providing many useful plugins contributed by the community, and it is frequently updated. It provides command line macro, batch processing and cluster computing. There is even a deep learning plugin, deepimageJ, which might be useful: https://deepimagej.github.io/deepimagej/download.html. 

Java-8 is required for preinstall. A forum is useful for asking question and resolve the issues: https://forum.image.sc/.

To avoid the installation, there is also an online browser interface: ImJoy, which is available at https://ij.imjoy.io/.

An example to run by command-line (Linux) (see https://imagej.net/scripting/headless in details)

`java -jar path_to_install/Fiji.app/jars/ij-1.53t.jar -ijpath path_to_install/Fiji.app -macro processImage.ijm path_to_save`

`./ImageJ-win64.exe --headless --console -macro ./RunBatch.ijm 'folder=../folder1 parameters=a.properties output=../samples/Output`

windows

```
ImageJ-win64.exe -macro Test D:\In.tif#D:\Out3.tif
```



### Measurement of the Dusts

A series of tests and their results are described in this section. These preliminary tests were performed from October to December in 2022, aiming to prepare for more sophisticated procedures in future.

#### Samples

Multiple acrylic strips (were originally prepared for SNO+ chemical compatibility study)

The dimensions of each strips are about 17.8 cm × 2.5 cm x . 



Both of the sides were glued with pieces of paper for protection. The protection paper pieces were teared off to let the strips expose to the lab air. Each strips were marked a number and an "A"-mark to distinguish between the up and down. We inspect one side of the sample with a total area of 17.8 cm × 2.5 cm.



#### Microscope

Microscope (Model NJF-120 A) with Plan 4-times and 10- times magnification objectives. Pictures captured by a 20 Megapixels Sony CMOS Camera  mounted on the top.



###### A Simple Walk-through of the Image Processing

A picture taken on 8 November, 2022 for Sample 4

ImageJ processing

processing of the images:

TestExample_sample4_8Nov_center_10times.png



watershed 





tif files



Automatic counting

https://imagej.net/imaging/particle-analysis

waterShed tool



deepImageJ

links to the respective Python packages.



Compare the analysis

TestExample_sample4_8Nov_center_10times.png



#### Cleaning Procedures





### References

[1] Akerib, D. S., et al. "The LUX-ZEPLIN (LZ) radioactivity and cleanliness control programs." *The European Physical Journal C* 80.11 (2020): 1-52.

[2] M. Boulay,  DEAP-SOP-801, Ultrahigh Purity Cleaning Procedure for DEAP Process Components

[3] imageJ