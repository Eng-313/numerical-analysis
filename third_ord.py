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
sumX, sumX2, sumX3, sumX4, sumX5, sumX6, sumY, sumXY, sumX2Y, sumX3Y = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for i in range(n):
    sumX = sumX + x[i]
    sumX2 = sumX2 + x[i] * x[i]
    sumX3 = sumX3 + x[i] * x[i] * x[i]
    sumX4 = sumX4 + x[i] * x[i] * x[i] * x[i]
    sumX5 = sumX5 + x[i] * x[i] * x[i] * x[i] * x[i]
    sumX6 = sumX6 + x[i] * x[i] * x[i] * x[i] * x[i] * x[i]

    sumY = sumY + y[i]
    sumXY = sumXY + x[i] * y[i]
    sumX2Y = sumX2Y + x[i] * x[i] * y[i]
    sumX3Y = sumX3Y + x[i] * x[i] * x[i] * y[i]

A = np.array([[n, sumX, sumX2, sumX3], [sumX, sumX2, sumX3, sumX4],
              [sumX2, sumX3, sumX4, sumX5], [sumX3, sumX4, sumX5, sumX6]])
b = np.array([sumY, sumXY, sumX2Y, sumX3Y])
z = np.linalg.solve(A, b)

# Finding coefficients a0 a1 a2 and a3
a3 = z[3]
a2 = z[2]
a1 = z[1]
a0 = z[0]

# Displaying coefficients a, b & equation
print("\nCoefficients are:")
print("a0 = ", a0)
print("a1 = ", a1)
print("a2 = ", a2)
print("a3 = ", a3)
print("And equation is: y = %0.8f + %0.8f x + %0.8f x^2 + %0.8f x^3" % (a0, a1, a2, a3))
