#importation de librairie nécessaires 
import urllib.request
import cv2 as cv
import numpy as np
import array as arr
import os

path = '/home/jrmr/Bureau/pyMachinLearning/haarCascades_WorkForFun/'

# fonction qui crée le fichier de description pour nos images négatives                
def descripteur():

    for fichier in os.listdir(path+'Label') :
        #print(str(fichier[:( len(str(fichier))- 4 ) ] ))
        name = str(fichier[:( len(str(fichier))- 4 ) ] )

        with open(path+'NewLabel/'+str(fichier)) as f:
            content = f.readlines()
            
            tab     = ''
            item    = 0
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

            #print('\n\n'+tab2+'\n'+tab+'\n\n')
            #print('FILE '+str(item)+'\n')
            #print(tab)

            with open(path+'info.txt','a') as g:
                g.write(name +'.jpg'+' '+ str(item) + ' '+ tab2 + "\n")

        
def resie():        
    for fichier in os.listdir(path+'img1') :
        print(str(fichier))
        if (str(fichier) != 'nv') :
            img = cv.imread(path+'img1/'+str(fichier), 0)
            resized_image = cv.resize(img, (640,480), 0)
            cv.imwrite(path+"img_resize/"+str(fichier), resized_image)


def neg_descripteur():
    for fichier in os.listdir(path+'neg') :
        line = 'neg/'+fichier+'\n'

        with open(path+'bg.txt','a') as f:
            f.write(line)

#neg_descripteur()
#descripteur()
resie()