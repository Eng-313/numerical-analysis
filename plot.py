#
import numpy
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]

strt = x[0]
stp = x[len(x) - 1]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(start=strt,
                        stop=stp,
                        num=10,
                        endpoint=True,
                        retstep=False,
                        dtype=None)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
