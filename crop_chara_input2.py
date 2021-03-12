# -*- coding: utf-8 -*-

# construct the argument parser and parse the arguments
import numpy as np
import cv2
import ast
file1 = open('texte_localisation_chara.txt', 'r')
Lines = file1.readlines()

L = []
for i in range(len(Lines)):
    Lines[i] = ast.literal_eval(Lines[i])
    L += Lines[i][1]
S = []
for i in set(L) :
    S += (i , L.count(i))
print(len(set(L)))
print(S)


for i in range(len(Lines)):
    parts = Lines[i][0].split(".")[0].split("_")
    if parts[0][0] == 'D' :
        num_image = int(parts[0].split("D")[-1])
        eclairage = int(parts[2].split("L")[-1].split(" ")[0])
        if len(parts[2].split("L")[-1].split(" ")) > 1 :
            Lines[i][0] = "D{:04d}_{}_L{:04d} {}.jpg".format(num_image + 1, parts[1], eclairage + 1,
                                                             Lines[i][0].split(".")[0].split("_")[-1].split(" ")[-1])
        else :
            Lines[i][0] = "D{:04d}_{}_L{:04d}.jpg".format(num_image + 1, parts[1], eclairage + 1)
    else :
        num_image = int(parts[0].split("G")[-1])
        eclairage = int(parts[2].split("L")[-1].split(" ")[0])
        if len(parts[2].split("L")[-1].split(" ")) > 1 :
            Lines[i][0] = "G{:04d}_{}_L{:04d} {}.jpg".format(num_image + 1, parts[1], eclairage + 1,
                                                   Lines[i][0].split(".")[0].split("_")[-1].split(" ")[-1])
        else :
            Lines[i][0] = "G{:04d}_{}_L{:04d}.jpg".format(num_image + 1, parts[1], eclairage + 1)
    print(Lines[i][0])
    img = cv2.imread("input_L0002/"+Lines[i][0])
    img = cv2.resize(img,(1333,1000))
    img2 = img.copy()
    img2 = img[int(Lines[i][2]):int(Lines[i][2])+int(Lines[i][4]), int(Lines[i][3]):int(Lines[i][3])+int(Lines[i][5])]
    cv2.imwrite("Chara2/"+str(i)+Lines[i][1]+".jpg", img2)
    print(i)