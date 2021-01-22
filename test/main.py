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



def descripteur():

    for fichier in os.listdir('/home/jrmr/Bureau/pyMachinLearning/Label') :
        #print(str(fichier[:( len(str(fichier))- 4 ) ] ))
        name = str(fichier[:( len(str(fichier))- 4 ) ] )

        with open('/home/jrmr/Bureau/pyMachinLearning/Label/'+str(fichier)) as f:
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

            startR  = 0
            flag_r  = 0
            for h in range(len(tab)) :
                if (tab[h] == '.') :
                    flag = 1
                
                if (tab[h] == ' ') :
                    flag = 0

                if (flag == 0):
                    tab2 += tab[h]

                
            print('\n\n'+tab2+'\n'+'\n\n'+jj)
            #print('FILE '+str(item)+'\n')
            #print(tab)


im  = cv2.imread('/home/jrmr/Bureau/pyMachinLearning/test/n_08df83ae4d1def24.jpg')
im_o = cv2.imread('/home/jrmr/Bureau/pyMachinLearning/test/o_08df83ae4d1def24.jpg')


# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

#    L, H
#o = 683, 1024      (size 167, 747)
#n = 640, 430       (size 167-43 (124), 747-594 (153) BAD)

#    43, 594
# Create a Rectangle patch
print(str(im_o.shape[1] ))

rect = patches.Rectangle((0 / (im_o.shape[1] / im.shape[1]), 413 / (im_o.shape[0] / im.shape[0])),
(167 - (im_o.shape[1] - im.shape[1])),
(747 - (im_o.shape[0] - im.shape[0])), linewidth=1,edgecolor='r',facecolor='none')

rect2 = patches.Rectangle((130 / (im_o.shape[1] / im.shape[1]), 256 / (im_o.shape[0] / im.shape[0])),
(417 - (im_o.shape[1] - im.shape[1])),#
(901 - (im_o.shape[0] - im.shape[0])), linewidth=1,edgecolor='r',facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)
ax.add_patch(rect2)

print(str((im_o.shape[0] - im.shape[0])))
#plt.show()

descripteur()

#/home/jrmr/Bureau/pyMachinLearning/

