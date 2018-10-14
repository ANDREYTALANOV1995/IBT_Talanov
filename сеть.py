from pybrain.tools.shortcuts import buildNetwork
from PIL import Image
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import RPropMinusTrainer
import numpy as np
import os

files = os.listdir("img/")

ds = SupervisedDataSet(200*60*3, 1)


for i in range(len(files)):
    img = Image.open("img/"+files[i])
    data = np.array(img)
    data = data.reshape(-1)
    ds.addSample((data), (files[i][0:6]))

img1 = Image.open("660022.png")

data1 = np.array(img)
data1 = data1.reshape(-1)

net = buildNetwork(200*60*3, 1)
 
trainer = RPropMinusTrainer(net)
trainer.setData(ds)

trainer.trainEpochs(100)

print(net.activate(data1))
