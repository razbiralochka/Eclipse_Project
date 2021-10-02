import tensorflow as tf

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image





white=np.ones([256,256,1])

mask=np.ones([256,256,1])

for i in range(255):
    for j in range(255):
        if (i-127)*(i-127)+(j-127)*(j-127)<pow(117,2):
            mask[i,j]=0



imgs=np.empty([15,256,256,3])

test_img=np.empty([15,256,256,1])

for i in range(15):
    imgs[i]=image.imread("TrainingBMP/"+str(i+1)+".bmp")
    test_img[i,:,:,0]=(imgs[i,:,:,0]+imgs[i,:,:,1]+imgs[i,:,:,2])/(255*3)
    test_img[i]=white-test_img[i]
    test_img[i]=test_img[i]-mask
    for n in range(255):
        for k in range(255):
            if  test_img[i,n,k]<0.4:
                test_img[i,n,k]=0


  
plt.figure()
plt.imshow(test_img[14])
plt.colorbar()
plt.grid(False)
plt.show()

    




WolfNN = tf.keras.models.load_model('model.h5')
WolfNN.load_weights('weights.h5')

                   

WolfNumberNN=WolfNN.predict(test_img) 

a=np.array([0,  0, 22, 40, 58, 48, 58, 48, 33, 25, 28, 30, 51, 46, 46])

b=np.ones(15)

for i in range(15):
    b[i]=WolfNumberNN[[i]]

print(a)
print(b)

err=abs(a-b)/a
err=err*100
plt.plot(err)