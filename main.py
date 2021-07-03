import numpy as np
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5]
Y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]

# Train Algorithm (Polynomial)
degree = 2
poly_fit = np.poly1d(np.polyfit(X, Y, degree))

# Plot data
xx = np.linspace(0, 26, 100)
plt.plot(xx, poly_fit(xx), c='r', linestyle='-')
plt.title('Polynomial')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([0, 25, 0, 100])
plt.grid(True)
plt.scatter(X, Y)
plt.show()

# Predict price
print(poly_fit(12))
