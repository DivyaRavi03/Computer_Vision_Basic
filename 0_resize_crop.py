# Image Resizing and Cropping

# This is an another fundamental image preprocessing techniques using python and OpenCV. The script loads an image, resized it to specific dimensions mentioned and crops a defined region of interest(ROI - specific part of image rather than whole).

import cv2
import numpy as np
img_path = "/home/divya/cv_projects/images/test_img.jpg"
img = cv2.imread(img_path)

if img is None:
	print(f"Error: Could not load image from {img_path}")
else:
	width= 300
	height = 450
	dimensions = (width, height)
	print("image is ready to resize and crop") 
	resize_img = cv2.resize(img, dimensions, interpolation = cv2.INTER_AREA)
	crop_img = img[100:500, 150:500]
	cv2.imshow("Orginial image",img)
	cv2.imshow("Resized image",resize_img)
	cv2.imshow("Cropped image", crop_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# Technologies used
# Ubuntu
# Python
# OpenCV
# Numpy
# What it does
# Loads an image from a file.
# Resizes the image to a predefined width and height using 'cv2.resize()' function.
# Crops a ROI (specific part of an image) from original using Numpy array slicing.
# Displays original, resized, and cropped images separately.
# Steps to follow
# Run the py file with image or image_path changed.
# Key concepts:
# Image Resizing - This allows to create uniform input sizes to feed machine learning models.
# Cropping using Numpy slicing - This is possible because images are changed to arrays (each pixels to matrix) using Numpy so that it can be manipulated directly and efficiently.
