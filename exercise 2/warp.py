import sys
import cv2 as cv
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image

#Arxika tha paro se metablites ta orismata pou moy dinei
arxiki_eikona = sys.argv[1]
teliki_eikona = sys.argv[2]

#twra tha diabaso tin eikona kai tha thn balw se enan pinaka
image=Image.open(arxiki_eikona)
img=np.array(image)

print("Kleikare mou ta 4 shmeia ksekinontas apo to pano aristera meta sto pano deksia synexizoume sto kato deksia kai telos sto kato aristera")

position=[] #pinakas o opoios krataei ta 4 shmeia
def four_clicks(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN: #an pathsei aristero klik pairno tis sintetgmenes tou simeiou
    	position.append([x,y])
        
cv.namedWindow("granma",cv.WINDOW_NORMAL)
cv.resizeWindow("granma",800,600) #emfanizo tim eikona se diastaseis pou mporo na tis epekserasto
cv.setMouseCallback("granma",four_clicks)

while(1):
    cv.imshow("granma",img)
    if cv.waitKey(1) and len(position)==4: #otan paro ta 4 shmeia stamatao kai kleino to parathiro
       break
cv.destroyAllWindows()

#--------SEIMIOSI--------
#Kano klik stin eikona: Arxika pano aristera meta pano deksia
# amesos meta kato deksia kai telos kato aristera
#--------#TELOS SEIMIOSIS--------

A=np.array([ #dimiourgo ton pinaka a opws stis diafaneies
[position[0][0],position[0][1],1,0,0,0,-position[0][0]*0,-position[0][1]*0],
[0,0,0,position[0][0],position[0][1],1,-position[0][0]*0,-position[0][1]*0],
[position[1][0],position[1][1],1,0,0,0,-position[1][0]*1000,-position[1][1]*1000],
[0,0,0,position[1][0],position[1][1],1,-position[1][0]*0,-position[1][1]*0],
[position[2][0],position[2][1],1,0,0,0,-position[2][0]*1000,-position[2][1]*1000],
[0,0,0,position[2][0],position[2][1],1,-position[2][0]*1000,-position[2][1]*1000],
[position[3][0],position[3][1],1,0,0,0,-position[3][0]*0,-position[3][1]*0],
[0,0,0,position[3][0],position[3][1],1,-position[3][0]*1000,-position[3][1]*1000],
],np.int32)

'''
x1',y1'=0,0
x2',y2'=1000,0
x3',y3'=1000,1000
x4',y4'=0,1000
'''
b=np.array([0,0,1000,0,1000,1000,0,1000]) #dimiourgo ton pinaka b opws stis diafaneies
A=np.linalg.inv(A) #ypologizo ton antistrofo tou A
x=np.matmul(A,b) #polaplasiazo ton A antistrofo me to b oste na bro to dianisma x

probolikos=np.array([ #dimiourgo ton pinaka 3*3 opws stis diafaneies
[x[0],x[1],x[2]],
[x[3],x[4],x[5]],
[x[6],x[7],1],
],np.float32)

warp=cv.warpPerspective(img,probolikos,(1000,1000)) #efarmozo ton metasximatismo me tin sinartisi warpPerspective
cv.namedWindow("WARP",cv.WINDOW_NORMAL)
cv.resizeWindow("WARP",800,600)
while(1):
	cv.imshow("WARP",warp)
	if cv.waitKey(1) & 0xFF==ord('x'): #emfanizo tin teliki eikona kai OTAN PATISEI x KLEINEI TO PARATHIRO kai termatizei to programma
		break
cv.destroyAllWindows()

#apothikeuo tin teliki eikona
teliko=Image.fromarray(warp.astype(np.uint8))
teliko.save(teliki_eikona)