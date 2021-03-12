# -*- coding: utf-8 -*-


# construct the argument parser and parse the arguments
import numpy as np
import argparse
import cv2
import os




Localisations = []
refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)        
        
def load_images_from_folder(folder):
    images = []
    nom_image = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            nom_image.append(filename)
    return images,nom_image

images,nom_image = load_images_from_folder('inputs')

Localisations = []
for i in range(130):
    # load the image, clone it, and setup the mouse callback function
    #nom_image = r"C:\Users\Bilal\Downloads\photo_test.jfif"
    #image = cv2.imread("inputs/"+nom_image[1])
    image = images[i]
    image = cv2.resize(image,(1333,1000))
    # load the image, clone it, and setup the mouse callback function
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    
    
        
    while True:
    	# display the image and wait for a keypress
    	cv2.imshow("image", image)
    	key = cv2.waitKey(1) & 0xFF
    	# if the 'r' key is pressed, reset the cropping region
    	if key == ord("r"):
    		image = clone.copy()
    	# if the 'c' key is pressed, break from the loop
    	elif key == ord("c"):
    		break
    # if there are two reference points, then crop the region of interest
    # from teh image and display it
    if len(refPt) == 2:
        y = refPt[0][0]
        x = refPt[0][1]
        h = refPt[1][0] - y
        w = refPt[1][1] - x
        roi = clone[x:x+w,y:y+h]
        Localisations.append([nom_image[i],x,y,w,h])
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)
    # close all open windows
    cv2.destroyAllWindows()
    
with open("texte_localisation.txt", 'w') as output:
    for row in Localisations:
        output.write(str(row) + '\n')

