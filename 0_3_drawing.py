# Image Annotation Basics with OpenCV

# This project demonstrates how to perform basic image annotation by drawing shapes and writing text using Python and OpenCV. These skills are foundational for visualizing data and the output of computer vision models, such as drawing bounding boxes around detected objects.

import cv2
import numpy as np

img_path = "../images/test_img.jpg"

img = cv2.imread(img_path)

if img is None:
	print(f"Error in {img_path}")
else:
# for rectangle
	copy_img = img.copy()
	start_point = (150,100)
	end_point = (550,500)
	color = (0,255,0)
	thickness = 2
	cv2.rectangle(copy_img, start_point, end_point, color, thickness)
# for circle
	circle_center = (350, 300)
	circle_radius = 50 
	circle_color = (0, 0, 255)
	cv2.circle(copy_img, circle_center, circle_radius, circle_color, -1)
	text = "AI study session"
	text_origin = (20, 40)
	font_style = cv2.FONT_HERSHEY_SIMPLEX
	font_scale = 1.2
	font_color = (255,255,255)
	line_thickness = 2
	cv2.putText(copy_img,text, text_origin, font_style, font_scale, font_color, line_thickness) 
	cv2.imshow("Image with rectangle",copy_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# Features
# Draws a rectangle with a specific color, thickness, and size of box.
# Draws a filled mentioned color circle at a given center point and radius.
# Writes text onto the image using a specific font, scale, color and location.
# Demonstrates the use of a copy of the original image to preserve it from modifications.
# Technologies Used
# Ubuntu
# Python
# OpenCV
# NumPy
# Key Functions Learned
# cv2.rectangle() - draws a rectangele as a boundary box to detect objects
# cv2.circle() - draws a circle to keep only specific area from image
# cv2.putText()- adds text to image - annotation
