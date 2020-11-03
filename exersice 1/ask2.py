import sys
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image

#Arxika tha paro se metablites ta orismata pou moy dinei
arxiki_eikona = sys.argv[1]
metasximatismeni_eikona = sys.argv[2]
a1 = float(sys.argv[3])
a2 = float(sys.argv[4])
a3 = float(sys.argv[5])
a4 = float(sys.argv[6])
a5 = float(sys.argv[7])
a6 = float(sys.argv[8])

#twra tha diabaso tin eikona kai tha thn balw se enan pinaka
image=Image.open(arxiki_eikona)
img=np.array(image)

#Twra tha brw tis grammes kai tis stiles tou pinaka
#Auto tha to kanw me tin entoli shape
lines,columns=img.shape
#parakato ilopoio ton afiniako metasximatismo pou den einai tipota allo para enas
#grammikos metasximatismos sinodeuomenos apo mia metatopisi
#episis ilopoio tin paremboli kontinoterou geitona. Se ahtin tin paremboli kathe fora
#pou dimiourgeitai ena neo deigma, epilegoume to kontinotero deigma to opoio exoume stin
#diathesi mas apo thn arxiki eikona eisodou. Auto to kanw me tin sinartisi round
changed_image=np.zeros((lines,columns))
for i in range (0,lines-1):
    for j in range (0,columns-1):
        x=i-lines/2 #edo apla allazoume to sistima sintetagmenon gia na min to strefei apo pano aristera alla apo tin mesi tis eikonas
        y=j-columns/2 #edo apla allazoume to sistima sintetagmenon gia na min to strefei apo pano aristera alla apo tin mesi tis eikonas
        af_x=a1*x+a4*y+a3 #edo ginetai o afinikos metasximatismos
        af_y=a2*x+a5*y+a6 #edo ginetai o afinikos metasximatismos
        new_x=af_x+lines/2 #epanafero tis sintenagmenes
        new_y=af_y+columns/2 #epanafero tis sintenagmenes
        paremboli_x=round(new_x) #edo ginetai h paremboli kontinoterou geitona
        paremboli_y=round(new_y) #edo ginetai h paremboli kontinoterou geitona
        #parakato elegxo an i oi kainouries times den bgainoun ekso apo ta oria tis eikonas eisodou
        if(paremboli_x>=0 and paremboli_y>=0 and paremboli_x<lines and paremboli_y<columns):
            changed_image[i][j]=img[paremboli_x][paremboli_y]

#Telos tha ypologiso thn metasximatismeni eikona kai tha thn emfaniso
teliko=Image.fromarray(changed_image.astype(np.uint8))
teliko.save(metasximatismeni_eikona)