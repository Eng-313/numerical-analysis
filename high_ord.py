#
import numpy
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter order of list square regression = "))
d = int(input("How many data points? "))

x = np.zeros(d)
y = np.zeros(d)

print("Enter data:")
for i in range(d):
    x[i] = float(input("x[" + str(i) + "]= "))
    y[i] = float(input("y[" + str(i) + "]= "))


# fit up to deg = n
z = np.polyfit(x, y, n)

# Displaying coefficients a, b & equation
print("\nCoefficients are:")
print(z)

# Plot Data
strt = x[0]
stp = x[len(x) - 1]

mymodel = numpy.poly1d(numpy.polyfit(x, y, n))

myline = numpy.linspace(start=strt,
                        stop=stp,
                        num=50,
                        endpoint=True,
                        retstep=False,
                        dtype=None)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()