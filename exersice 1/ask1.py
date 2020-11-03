import sys
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image

#Arxika tha paro se metablites ta orismata pou moy dinei
arxiki_eikona = sys.argv[1]
katwfliwmeni_eikona = sys.argv[2]
theshold =float(sys.argv[3])

#twra tha diabaso tin eikona kai tha thn balw se enan pinaka kai metatreopo tis times se double oste
#na mporeso parakato na kano tis diaireseis me megaliteri akribeia
image=Image.open(arxiki_eikona)
img=np.array(image)
img=double(img)

#Twra tha brw tis grammes kai tis stiles tou pinaka kai tha dw tin diastasi tou
#Auto tha to kanw me tin entoli shape
diastasi=len(img.shape)
lines,columns=img.shape

#An i eikona einai eghromi(3 diastaseis) tha prepei na tin metatrepso.
new_image=np.zeros([lines,columns])
if(diastasi==3):
    for i in range (0,lines-1):
        for j in range (0,columns-1):
            new_image[i][j]=(img[i][j][0]+img[i][j][1]+img[i][j][2])/3 #mesos oros twn RGB
elif(diastasi==2):
    new_image=img[:]
else:
    print("Something goes wrong!!!")

#Telos tha ypologiso thn katofliwmeni eikona kai tha thn emfaniso

theshold_image=np.zeros([lines,columns])
for i in range (0,lines):
    for j in range (0,columns):
        if(new_image[i][j]>theshold):
            theshold_image[i,j]=255 #kanto aspro
        else:
            theshold_image[i][j]=0 #kanto mauro
teliko=Image.fromarray(theshold_image.astype(np.uint8))
teliko.save(katwfliwmeni_eikona)