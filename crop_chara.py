# -*- coding: utf-8 -*-


import cv2
file1 = open('texte_localisation_chara.txt', 'r')
Lines = file1.readlines()

L = []
for i in range(len(Lines)):
    Lines[i] = ast.literal_eval(Lines[i])
    L += Lines[i][1]
S = []
for i in set(L) :
    S += (i , L.count(i))


for i in range(len(Lines)):
    img = cv2.imread("inputs/"+Lines[i][0])
    img = cv2.resize(img,(1333,1000))
    img2 = img.copy()
    img2 = img[int(Lines[i][2]):int(Lines[i][2])+int(Lines[i][4]), int(Lines[i][3]):int(Lines[i][3])+int(Lines[i][5])]
    cv2.imwrite("Chara/"+str(i)+Lines[i][1]+".jpg", img2)