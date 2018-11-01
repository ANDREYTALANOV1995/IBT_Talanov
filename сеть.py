
from pybrain.tools.shortcuts import buildNetwork
from PIL import Image
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import RPropMinusTrainer
import numpy as np
import os


files = os.listdir("img/")
files1 = os.listdir("test_img/")
ds = SupervisedDataSet(200*60*3, 1)

for i in range(len(files)):
    img = Image.open("img/"+files[i])
    data = np.array(img)
    data = data.reshape(-1)
    ds.addSample((data), (files[i][0:6]))




img1 = Image.open("test_img/152830.png")

data1 = np.array(img1)
data1 = data1.reshape(-1)

net = buildNetwork(200*60*3, 1)

trainer = RPropMinusTrainer(net)
trainer.setData(ds)

trainer.trainEpochs(100)


def calculation(a,b):
    i=0
    if((int(a) // 100000)%10 == (int(b) // 100000)%10):
        i=i+1
    if ((int(a) // 10000) % 10 == (int(b) // 10000) % 10):
        i = i + 1
    if((int(a) // 1000)%10 == (int(b) // 1000)%10):
        i=i+1
    if((int(a) // 100)%10 == (int(b) // 100)%10):
        i=i+1
    if((int(a) // 10)%10 == (int(b) // 10)%10):
        i=i+1
    if((int(a) // 1)%10 == (int(b) // 1)%10):
        i=i+1
    return i/6*100
sum = 0
for fname in files1:
    img3 = Image.open("test_img/%s" % fname)
    data6 = np.array(img3)
    data6 = data6.reshape(-1)
    print(fname, "Результат распознования равен", np.round(net.activate(data6)))
    sum += calculation(np.round(net.activate(data6)), fname.split('.')[0])

print('%s' % (sum / 3))





