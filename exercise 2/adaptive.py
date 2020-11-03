import sys
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image

#Arxika tha paro se metablites ta orismata pou moy dinei
arxiki_eikona = sys.argv[1]
katwfliwmeni_eikona = sys.argv[2]
windows_size = int(sys.argv[3])

#twra tha diabaso tin eikona kai tha thn balw se enan pinaka kai metatrepo tis times se double oste
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
    exit(1)

def ypologise_antikeimeniki_otsu(A, k):
    pixels_tmima1 = A[A < k]
    pixels_tmima1 = pixels_tmima1[pixels_tmima1>=0] #pairno oles tis thetikes times. Giati ta arinitika einai ayta poy einai ektos orion. Etsi o pinakas exei mono ta simeia pou einai entos ton orion
    pixels_tmima2 = A[A >=k]
    mu1 = np.mean(pixels_tmima1)
    mu2 = np.mean(pixels_tmima2)
    mu_synoliko = np.mean(A.flatten())
    pi1 = len(pixels_tmima1) / (len(pixels_tmima1) + len(pixels_tmima2))
    pi2 = len(pixels_tmima2) / (len(pixels_tmima1) + len(pixels_tmima2))
    antikeimeniki_synartisi = pi1 * (mu1 - mu_synoliko)**2 + pi2 * (mu2 - mu_synoliko)**2
    return(antikeimeniki_synartisi)

#--------SEIMIOSI--------
#Gia tin geitonia pairno apo to pixel pou briskomai toses stiles oso to windows_size-1 apo ta deksia
#Gia tin geitonia pairno apo to pixel pou briskomai toses grammes oso to windows_size -1 pros ta kato
#--------TELOS SEIMIOSIS--------

#Telos tha ypologiso thn katofliwmeni eikona kai tha thn emfaniso
pinakas=np.zeros((lines,columns)) #enas pinakas pou exei ta katwflia gia kathe pixel
img_new=np.zeros((windows_size,windows_size)) #einai h geitonai pou psaxnoume na gia na broume to katwfli
for i in range (0,lines):
    for j in range (0,columns):
    	kalytero_katwfli=0
    	kalyterh_timi=0
        #dimiourgo tin geitonia
    	for k in range(0,windows_size):
    		for l in range(0,windows_size):
    			if (i+k>lines-1) or (j+l>columns-1): #elegxo an einai ektos orion
    				img_new[k][l]=-4 #an einai bazo tin timi sto -4 oste na min tin simperilabo ston ypologismo tou kalyterou katwfliou
    			else:
    				img_new[k][l]=new_image[i+k][j+l]
        #telos dimiourgias geitonias
    	for m in range(1,256,10): #to pairno ana 10 giati den trexei ana ena. Kanei poli ora den katafera na to trekso
    		obj_otsu=ypologise_antikeimeniki_otsu(img_new,m)
    		if(obj_otsu>kalyterh_timi):
    			kalytero_katwfli=m
    			kalyterh_timi=obj_otsu
    	pinakas[i][j]=kalytero_katwfli #bazo to katwfli sto katallilo pixel

for i in range (0,lines):
    for j in range (0,columns):
        if(img[i][j]>pinakas[i][j]):
            img[i,j]=255 #kanto aspro
        else:
            img[i][j]=0 #kanto mauro

teliko=Image.fromarray(img.astype(np.uint8))
teliko.save(katwfliwmeni_eikona)