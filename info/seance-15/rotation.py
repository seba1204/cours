import numpy as np
import matplotlib.pylab as plt

def ellipse(N):
    t = np.linspace(0, 2*np.pi, N)
    h = 2*np.pi/N
    x=[1]
    y=[2]
    
    for i in range(N):
        x.append(x[i] + h * (2*x[i]-5*y[i]))
        y.append(y[i] + h * (x[i]-2*y[i]))
    return(x, y)
    
def combine(A, B):    
    C = []
    for i in range(len(A)):
        C.append([A[i], B[i]])
    return C

def decombine(C):    
    A, B = [], []
    for i in C:
        A.append(i[0])
        B.append(i[1])
    return A, B
A = ellipse(1000)

X = np.array(A[0])
Y = np.array(A[1])
plt.plot(X, Y)
a = max(np.sqrt(X**2 + Y**2))

rmax = 0
for i in range(len(X)):
    r =  np.sqrt(X[i]**2 + Y[i]**2)
    if r > rmax:
        rmax=r
        pointMax = [X[i], Y[i]]

u = np.array(pointMax)
v = np.array([1, 0])
print(u)
def norme(u):
    return np.sqrt(u[0]**2 + u[1]**2)
def pScalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]
theta = np.arccos(pScalaire(u, v) / (norme(u) * norme(v)))

def rotation(X, Y, theta):
    B = []
    R = np.array([[np.cos(theta), (-1) *np.sin(theta)], [ np.sin(theta), np.cos(theta)]])
    for i in range(len(X)):
        u = np.array([X[i], Y[i]])
        B.append(np.dot(u, R))
    return B
b = rotation(X, Y, theta)
plt.plot(b[0], b[1])
plt.show()
print(theta)

