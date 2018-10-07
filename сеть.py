from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import RPropMinusTrainer
 
#тут создаем структуру для обучения и набор данных для обучения
ds = SupervisedDataSet(5, 1)

ds.addSample((0, 1, 0, 0, 1), (1,))     # правило для цифры 1
ds.addSample((1, 0, 0, 1, 1), (2,))     # правило для цифры 2
ds.addSample((1, 1, 1, 1, 0), (3,))     # правило для цифры 3  
ds.addSample((0, 0, 1, 0, 1), (4,))     # правило для цифры 4
ds.addSample((1, 0, 1, 0, 0), (5,))     # правило для цифры 5
ds.addSample((0, 1, 1, 0, 0), (6,))     # правило для цифры 6
ds.addSample((1, 1, 0, 0, 0), (7,))     # правило для цифры 7
ds.addSample((1, 0, 1, 0, 1), (8,))     # правило для цифры 8
ds.addSample((1, 0, 1, 1, 1), (9,))     # правило для числа 9

# создаем нейросеть с 5 входами, 9 скрытых слоя и 1 выход
net = buildNetwork(5, 9, 1,)
 
# указываем какую сеть и какими данными обучать
trainer = RPropMinusTrainer(net)
trainer.setData(ds)
 
# обучаем сеть
trainer.trainEpochs(100)
 
# подаем на вход контрольные точки цифры 9
print(net.activate([1,0,1,1,1]))
