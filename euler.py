import numpy as np

# Reading value of n
n = int(input("How many data points? "))

# Creating numpy array x & y to store n data points
x = np.zeros(n)
y = np.zeros(n)

# Reading data
print("Enter data:")
for i in range(n):
    x[i] = float(input("x[" + str(i) + "]= "))
    y[i] = float(input("y[" + str(i) + "]= "))

# Finding required sum for least square methods
sumX, sumX2, sumY, sumXY = 0, 0, 0, 0
for i in range(n):
    sumX = sumX + x[i]
    sumX2 = sumX2 + x[i] * x[i]
    sumY = sumY + y[i]
    sumXY = sumXY + x[i] * y[i]

A = np.array([[n, sumX], [sumX, sumX2]])
b = np.array([sumY, sumXY])
z = np.linalg.solve(A, b)

# Finding coefficients a and b
a1 = z[1]
a0 = z[0]

# Displaying coefficients a, b & equation
print("\nCoefficients are:")
print("a0: ", a0)
print("a1: ", a1)
print("And equation is: y = %0.8f + %0.8f x" % (a0, a1))
