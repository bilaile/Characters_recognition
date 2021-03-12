# -*- coding: utf-8 -*-


import numpy as np
import cv2
import ast
import tkinter as tk
from tkinter import simpledialog


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
		cv2.rectangle(img2, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", img2)        
        
        
file1 = open('texte_localisation.txt', 'r')
Lines = file1.readlines()
for i in range(len(Lines)):
    Lines[i] = ast.literal_eval(Lines[i])
count = 0
i = 0
Localisations = []
root = tk.Tk()
# Strips the newline character
while i < len(Lines):
    img = cv2.imread("inputs/"+Lines[i][0])
    img = cv2.resize(img,(1333,1000))
    img2 = img.copy()
    img2 = img2[int(Lines[i][1]):int(Lines[i][1])+int(Lines[i][3]),int(Lines[i][2]):int(Lines[i][2])+int(Lines[i][4])]
    img2_clone = img2.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", img2)
        key = cv2.waitKey(1) & 0xFF
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            img2 = img2_clone.copy()
        if key == ord("a"):
            img2 = img2_clone.copy()
            answer = simpledialog.askstring("Input", "What is the character?",parent=root)
            # if there are two reference points, then crop the region of interest
            # from teh image and display itc
            if len(refPt) == 2:
                              
                y = int(refPt[0][0]) + int(Lines[i][2])
                x = int(refPt[0][1]) + int(Lines[i][1])
                h = int((refPt[1][0] - refPt[0][0]))
                w = int((refPt[1][1] - refPt[0][1]))
                
                Localisations.append([Lines[i][0],answer,x,y,w,h])
                roi = img[x:x+w,y:y+h]
                roi = cv2.resize(roi,(667,500))
                cv2.imshow("ROI", roi)
                cv2.waitKey(0)
            # close all open windows
            cv2.destroyAllWindows()

            break
            # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            i+=1
            # close all open windows
            cv2.destroyAllWindows()
            break

with open("texte_localisation_chara.txt", 'w') as output:
    for row in Localisations:
        output.write(str(row) + '\n')   

