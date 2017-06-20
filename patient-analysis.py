import numpy
import matplotlib.pyplot as plt

data =np.loadtxt(fname='data/inflimmation1.csv', delimiter=',')

print(data)

image-1=plt.plot(data)

plt.show(image-1)
