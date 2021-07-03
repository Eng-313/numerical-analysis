
##############################  Finite Divided Difference (FDD) Table #########################
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
import pandas as pd
import math


def get_diff_table(X, Y):
    """
         Get the market insert
    """
    n = len(X)
    A = np.zeros([n, n])

    for i in range(0, n):
        A[i][0] = Y[i]

    for j in range(1, n):
        for i in range(j, n):
            A[i][j] = (A[i][j - 1] - A[i - 1][j - 1]) / (X[i] - X[i - j])

    return A


def newton_interpolation(X, Y, x):
    """
         Calculate the interpolation of x points
    """
    sum = Y[0]
    temp = np.zeros((len(X), len(X)))
    #
    for i in range(0, len(X)):
        temp[i, 0] = Y[i]
    temp_sum = 1.0
    for i in range(1, len(X)):
        # x polynomial
        temp_sum = temp_sum * (x - X[i - 1])
        #
        for j in range(i, len(X)):
            temp[j, i] = (temp[j, i - 1] - temp[j - 1, i - 1]) / (X[j] - X[j - i])
        sum += temp_sum * temp[i, i]
    return sum


n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing
# to zero for storing x and y value along with differences of y
X = np.zeros(n)
Y = np.zeros(n)

# Reading data points
print('Enter data for X and Y: ')
for i in range(n):
    X[i] = float(input('X[' + str(i) + '] = '))
    Y[i] = float(input('Y[' + str(i) + '] = '))

'''
X = [4, 4.5, 5.5, 6]
Y = [0.6020600, 0.6532125, 0.7403627, 0.7781513]
'''
A = get_diff_table(X, Y)
df = pd.DataFrame(A)
print(df)

xs = np.linspace(np.min(X), np.max(X), 1000, endpoint=True)
ys = []
for x in xs:
    ys.append(newton_interpolation(X, Y, x))

plt.title("newton_interpolation")
plt.plot(X, Y, 's', label="original values")  # blue dot indicates the original value
plt.plot(xs, ys, 'r', label='interpolation values')  # Interpolation curve
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)  # specifies the position of the legend in the lower right corner
plt.show()