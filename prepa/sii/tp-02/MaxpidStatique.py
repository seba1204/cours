import numpy as np
import pylab as pl


a=69.5
b=82
l=80
L=290
p=4
m=0.65
g=9.81

n=1000
maxAngle=np.pi/2


theta=[-k * maxAngle / n for k in range(n)]


curves = [theta]

print(max(theta))
print(len(theta))

def traceCurve(f):
    curve = []
    for t in theta:
        curve.append(f(t))
    curves.append(curve)
    
def drawCurve():
    for i in range(1, len(curves)):
        pl.plot(curves[0], curves[i])
    pl.show()
    
def geo(t):
    return np.arctan((l * np.cos(t) + a) / (l * np.sin(t) - b))
    
def statique(t):
    return p * m * g * L * l * np.cos(t) / (2 * np.pi * np.sin(geo(t)))
    
traceCurve(statique)
drawCurve()