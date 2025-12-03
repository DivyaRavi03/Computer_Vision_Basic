# Basic Image Manipulation with OpenCV

# This project is my first step in my Computer Vision journey. It's a simple python script like "print("Hello World!") but for computer vision, this demonstrates fundamental image processing operations using OpenCV library.

import cv2
image_path = "../images/test_img.jpg"
image = cv2.imread(image_path)
if image is None:
   print(f"Error:{image_path}")
else:
   height, width, channels = image.shape
   print(f"Dimensions:{width}, wide by:{height}, channels: {channels}")
   grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   cv2.imshow("Original image", image)
   cv2.imshow("Grayscale image", grayscale)
   cv2.waitKey(0)
   cv2.destroyAllWindows()



# Technologies Used
# Ubuntu
# Conda for environment management
# Python
# OpenCV
# Numpy
# What it does
# Loads ang image from a local file.
# Converts the loaded image into grayscale.
# Displays both the original and the grayscale images and also its dimensions.
# Steps to follow
# Clone or download repository
# Ensure you have a python environment with required libraries installed (OpenCV, Numpy).
# Place an image file in main directory and rename it to 'test_image.jpg" or modify 'image_path' variable in 'load_img.py' script.
# Run the script from terminal: python load_img.py
