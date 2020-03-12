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
    
    
x, y = ellipse(1000)


plt.plot(x, y)
plt.show()