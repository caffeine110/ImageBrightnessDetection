# Image brightness detection

### Problem statement
Develop a generalized algorithm to detect the brightness of any image. Your algorithm should take an image as input and give a score between (0-10) as output (zero being low bright and 10 being high bright)

## Install Dependencies

    from PIL import Image
    from PIL import ImageStat
    import math
    import os
    import sys
    import matplotlib.pyplot as plt
    import csv


## Open interactive python Jupyter-notebook to visualise imageData

    Open findBrightness.ipynb in jupyter-notebook
    This file Gives Detail Explanation of Apporch to find solutionn
    Check code and output of each cell with comments for better understanding
    Scroll into outpul cell and observe the changes in value



## Command Line Approch to find Brightness of Single File

Detect for Single File :

    - Type accurate filePath along with file extension
    - $ python getBrightness.py test/1.jpg
    - Output will be displayed on terminal along with the popups


## Command Line Approch to find Brightness of Multiple Files in a Directory

Run the following command in terminal :

    - example -
      $ python getBrightnessCSV.py test/

    - where test/ is a directory containing all the images whose brightness has to be detected.
    - Directory Name must must be followed by / at the end
    - output of this file will be a "finalBrightness.csv" file

    - This "finalBRrightness.csv" file contains-
    - 4 Columns
        - MeanB     :
        - MedianB   :
        - RMSB      :
        - FinalB    :

        You can calculate accuracy on any of the columns
        - Values in Coloums FinalB may give bettter accuracy over wide range of imageDatasets