import numpy as np
import matplotlib.pyplot as plt


def init(x):
    if (x < 0):
        return-(init(-x))
    elif (x <= 7):
        return x/7
    return -(x-10)/3


def omega(x):
    k = np.floor((x+10)/20)
    return init(x-k*20)


def Trace(T):
    x = np.linspace(-10*T, 10*T, 1200)
    y = [omega(k) for k in x]
    plt.plot(x, y)
    plt.show()

# Trace(5)


def vibrante(k):
    x = np.linspace(0, 10, 1000)
    z = [omega(val) for val in x]
    zz = [omega(val-10) for val in x]
    c = 2
    t = np.floor(k*100)/100
    plt.figure()
    plt.axis([0, 10, -1, 1])
    y = [(omega(val+c*t)+omega(val-c*t))/2 for val in x]
    plt.plot(x, y, "-", color=(0, 0, 0), linewidth=2.5, label="t="+str(t))
    plt.plot(x, zz, ":", color=(1, 0, 0), linewidth=2, label="t=5")
    plt.plot(x, z, ":", color=(1, 0, 0), linewidth=2, label="t=0")
    plt.legend()
    plt.show()


for k in range(1, 5):
    vibrante(k)
