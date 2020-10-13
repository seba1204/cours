import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

# from src.constants import maxi
# from src.magnetic_field import f


'''constants of exercise number 5 : toroidal solenoid'''

# ------------- torus dimmensions ------------- #
a = 0.08  # side of the section                    #
b = 0.10  # internal radius                        #
def maxi(per): return b + a + (per * (b + a))   #
# --------------------------------------------- #


# -------------- coil parameters -------------- #
mu_0 = 4 * pi * 10 ** -7  # Vacuum permeability  #
N = 1000     # number of turns                     #
I = 4     # current intensity                   #
# --------------------------------------------- #


def rInInterval(r): return r > b and r < b+a


def zInInterval(z): return z > 0 and z < a


def magneticField(r): return (mu_0 * N * I) / (2 * pi * r)


def f(r, z):
    result = []
    for i in range(0, 1000):
        if(rInInterval(r[i])):
            result.append(magneticField(r[i]))
        else:
            result.append(0.)
    return result


fig = plt.figure()
ax = fig.gca(projection='3d')

maxV = maxi(0.2)

r = np.linspace(0, maxV, 1000)
z = np.linspace(0, maxV, 1000)

B = f(r, z)

ax.plot(r, z, B)
ax.legend()

plt.show()
