from PIL import Image

import numpy as np

img1 = Image.open("152830.png")

img2 = Image.open("302514.png")

img3 = Image.open("303104.png")

arr = np.array(img1)

for i in range(6):

    if arr[14][17+i*33][0] == 0:                 #проверка 1
        if arr[25][17+i*33][0] == 0:             #проверка 2
            if arr[33][17+i*33][0] == 0:         #проверка 3
                print(3)
            else:
                print(6)
        else:
            if arr[33][17+i*33][0] == 0:         #проверка 3
                if arr[43][17+i*33][0] == 0:     #проверка 4
                    print(9)
                else:
                   if arr[25][27+i*33][0] == 0:  #проверка 5
                       print(8)
                   else:
                       print(5)
            else:
                if arr[43][17+i*33][0] == 0:     #проверка 4
                    print(2)
                else:
                    print(0)
        
    else:    
        if arr[25][17+i*33][0] == 0:             #проверка 2
            if arr[33][17+i*33][0] == 0:         #проверка 3
                print(6)
            else:
                print(1)
        else:
            print(4)    



    
