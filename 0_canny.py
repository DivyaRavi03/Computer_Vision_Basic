# Canny Edge Detection with OpenCV
# This project implements the classic Canny Edge Detection algorithm using Python and OpenCV. It's a foundational technique in computer vision that identifies the structural outlines (edges) of objects in an image by detecting sharp changes in pixel intensity.

import cv2
import numpy

img_path = "test_img.jpg"

img = cv2.imread(img_path)

if img is None:
	print(f"Error  in image path: {img_path}")
else:
	print("Image loaded")
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,100,200)
	cv2.imshow("Original",img)
	cv2.imshow("Canny",edges)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# Features
# Loads an image from a local file.
# Converts the image to grayscale, a necessary preprocessing step for the Canny algorithm.
# Applies the Canny algorithm to produce a binary image showing the detected edges.
# Displays the original image and the final edge map side-by-side for comparison.
# Technologies Used
# Python
# OpenCV
# NumPy
# Theoretical Concepts
# This project utilizes the cv2.Canny() function, which encapsulates the five core stages of the Canny algorithm:

# Noise Reduction (using a Gaussian filter)
# Gradient Intensity Calculation
# Non-Maximum Suppression
# Double Thresholding
# Hysteresis Edge Tracking