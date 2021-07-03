
# Euler method python program
import numpy as np
import matplotlib.pyplot as plt


# function to be solved
def f(x, y):
    return x ** 2 + y ** 2


# or
# f = lambda x: x+y

# Euler method
def euler(x0, y0, xn, n):
    # Calculating step size
    h = (xn - x0) / n

    print('\n-----------SOLUTION-----------')
    print('------------------------------')
    print('x0\ty0\tslope\tyn')
    print('------------------------------')
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.8f\t%.8f\t%0.8f\t%.8f' % (x0, y0, slope, yn))
        print('------------------------------')
        y0 = yn
        x0 = x0 + h

    print('\nAt x=%.8f, y=%.8f' % (xn, yn))


# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# Euler method call
euler(x0, y0, xn, step)
