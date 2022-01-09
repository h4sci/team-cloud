import numpy
import matplotlib
import matplotlib.pyplot as plt

print('Neda')
sampl = numpy.random.uniform(low=0.5, high=13.3, size=(5,))
x = numpy.array([1, 2, 3, 4, 5])
#matplotlib.pyplot.plot(x,sampl)
#matplotlib.pyplot.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(100))

fig.savefig('graph.png')
