import numpy as np
import matplotlib.pyplot as plt
plt.axis([0, 1000, 0, 1])
w = 10  # fréquence
k = 2  # Nombre de période
X = np.linspace(0, k * 2 * np.pi, 1000)
phi = np.random.random()
Y = np.cos(phi + w * X)
for i in range(100):
    phi = np.random.random()
    Y += np.cos(phi + w * X) / (i + 1)
    plt.clf()
    plt.plot(X, Y)
    plt.pause(0.05)

plt.show()
