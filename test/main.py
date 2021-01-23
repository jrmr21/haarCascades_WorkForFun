#importation de librairie nécessaires 
import urllib.request
import cv2 as cv
import numpy as np
import array as arr
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import cv2

path = '/home/jrmr/Bureau/pyMachinLearning/haarCascades_WorkForFun/'

#out_RIO
def create_img(tab, name):
    im      = cv2.imread(path+'img_resize/'+ str(name) +'.jpg')      #resize picture
    im_o    = cv2.imread(path+'img1/'+ str(name) +'.jpg')    #origin picture

    print("\n name1 :"+str(name)+' '+ str(len(tab)-1) +"\n")
    # Create figure and axes
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)

    rX = (im_o.shape[1] / im.shape[1])
    rY = (im_o.shape[0] / im.shape[0])

    with open(path + 'NewLabel/'+ str(name)+'.txt','a') as g:
        for i in range(1, len(tab)) :
            tab_tmp = tab[i]
            #print("\n\n pppp: "+str(tab_tmp)+' i : '+ str(i) +'\n')
            
            pointA = (int(tab_tmp[0]) / rX)
            pointB = (int(tab_tmp[1]) / rY)

            rect = patches.Rectangle((pointA, pointB),
            ((int(tab_tmp[2]) / rX) - pointA),
            ((int(tab_tmp[3]) / rY) - pointB), linewidth=1, edgecolor='r', facecolor='none')

            ax.add_patch(rect)

            g.write('Penguin '+str(pointA) +'.0 '+
                str(pointB) +'.0 '+ 
                str((int(tab_tmp[2]) / rX) - pointA) +'.0 '+ 
                str((int(tab_tmp[3]) / rY) - pointB) +'.0 '+'\n')

    #plt.show()
    plt.savefig(path+'/out_RIO/'+ str(name) +'.jpg')
    
    
        
        

def descripteur():

    for fichier in os.listdir(path+'Label') :
        #print(str(fichier[:( len(str(fichier))- 4 ) ] ))
        name = str(fichier[:( len(str(fichier))- 4 ) ] )

        with open(path+'Label/'+str(fichier)) as f:
            content = f.readlines()
            
            tab     = ''
            item    = 0
            jj      = 0
            
            for line in content:
                item    += 1
                tab     += line[8:(len(line)-1)]
                tab     += '   '

            tab2        = ''
            flag        = 0
            h           = 0
            for h in range(len(tab)) :
                if (tab[h] == '.') :
                    flag = 1
                
                if (tab[h] == ' ') :
                    flag = 0

                if (flag == 0):
                    tab2 += tab[h]

            h           = 0
            str_num     = ''
            tab_num     = [0,0,0,0]
            count_tab   = 0 
            tab_line    = [[0,0,0,0],]

            for h in range(len(tab2)) :

                if (tab2[h] == ' ' and count_tab != 4) :
                    #print('\n\n'+tab2+'\n'+'\n\n')
                    #print("\n before : "+str_num+"\n")
                    tab_num[count_tab] = int(str_num, base=10)
                    count_tab   += 1
                    str_num     = ''

                    if (count_tab == 4) :
                        tab_line.append(tab_num)
                        #print('\n---\n'+tab2+'\n')
                        #print("\n"+str(tab_num)+'\n')
                        tab_num     = [0,0,0,0]
                    

                if (tab2[h] != ' ') :
                    if (count_tab  == 4) :
                        count_tab   = 0
                    str_num += tab2[h]

            #print("\n len :"+str(len(tab_line))+"// "+str(tab_line[len(tab_line)-1][0]) +"\n")
            #print('\n\n'+tab2+'\n'+'\n\n')
            #print('FILE '+str(item)+'\n')
            #print(tab)
            create_img(tab_line, str(fichier[:-4]))



descripteur()

#/home/jrmr/Bureau/pyMachinLearning/


def create_img2(tab, name):
    i       = 0
    im      = cv2.imread(path+'img_resize/'+ str(name) +'.jpg')      #resize picture
    im_o    = cv2.imread(path+'img1/'+ str(name) +'.jpg')    #origin picture

    print("\n name1 :"+str(name)+' '+ str(len(tab)) +"\n")
    # Create figure and axes
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im_o)

    rX = 1#(im_o.shape[1] / im.shape[1])
    rY = 1#(im_o.shape[0] / im.shape[0])

    print("\n rx "+str(tab[0][0])+" ry "+str(tab[0][1])+"\n")


    for i in range(len(tab)) :
        tab_tmp = tab[i]
            
        rect = patches.Rectangle((int(tab_tmp[0]) , int(tab_tmp[1]) ),
        (int(tab_tmp[2]) - int(tab_tmp[0])),
        (int(tab_tmp[3]) - int(tab_tmp[1])), linewidth=1, edgecolor='r', facecolor='none')

        ax.add_patch(rect)


    plt.show()

#create_img2([[238.683136, 120.173883, 464.013312, 612.5528429999999]],'00c438ec42b0f143')