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
sumX, sumX2, sumX3, sumX4, sumY, sumXY, sumX2Y = 0, 0, 0, 0, 0, 0, 0
for i in range(n):
    sumX = sumX + x[i]
    sumX2 = sumX2 + x[i] * x[i]
    sumX3 = sumX3 + x[i] * x[i] * x[i]
    sumX4 = sumX4 + x[i] * x[i] * x[i] * x[i]
    sumY = sumY + y[i]
    sumXY = sumXY + x[i] * y[i]
    sumX2Y = sumX2Y + x[i] * x[i] * y[i]

A = np.array([[n, sumX, sumX2], [sumX, sumX2, sumX3], [sumX2, sumX3, sumX4]])
b = np.array([sumY, sumXY, sumX2Y])
z = np.linalg.solve(A, b)

# Finding coefficients a and b
a2 = z[2]
a1 = z[1]
a0 = z[0]

# Displaying coefficients a, b & equation
print("\nCoefficients are:")
print("a0 = ", a0)
print("a1 = ", a1)
print("a2 = ", a2)
print("And equation is: y = %0.8f + %0.8f x + %0.8f x^2" % (a0, a1, a2))
