#importation de librairie nécessaires 
import urllib.request
import cv2 as cv
import numpy as np
import array as arr
import os

# fonction qui crée le fichier de description pour nos images négatives                
def descripteur():

    for fichier in os.listdir('/home/jrmr/Bureau/pyMachinLearning/Label') :
        #print(str(fichier[:( len(str(fichier))- 4 ) ] ))
        name = str(fichier[:( len(str(fichier))- 4 ) ] )

        with open('/home/jrmr/Bureau/pyMachinLearning/Label/'+str(fichier)) as f:
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

            with open('/home/jrmr/Bureau/pyMachinLearning/bg.txt','a') as g:
                g.write('img1/'+ name +'.jpg'+' '+ str(item) + ' '+ tab2 + "\n")

        
def resie():        
    for fichier in os.listdir('/home/jrmr/Bureau/pyMachinLearning/img1') :
        print(str(fichier))
        if (str(fichier) != 'nv') :
            img = cv.imread('/home/jrmr/Bureau/pyMachinLearning/img1/'+str(fichier), cv.IMREAD_COLOR)
            resized_image = cv.resize(img, (640,430))
            cv.imwrite("/home/jrmr/Bureau/pyMachinLearning/img1/nv/"+str(fichier), resized_image)




#descripteur()

resie()