import numpy as np
import matplotlib.pylab as plt
import time as t

phi = (1 + np.sqrt(5)) / 2

def firec(n):
    if (n == 0 or n == -1):
        return 1
    return firec(n-1) + firec(n-2)

def firecTime(n):
    T = []
    X = []
    for i in range(1, n+1):
        t1 = t.time()
        firec(i)
        T.append(t.time() - t1)
        X.append(i)
    return (X, T)

def traceTimeFirect(n):
    values = firecTime(n)
    plt.plot(values[0], values[1])
    plt.show()

def getAlpah(n):
    A = firecTime(n)
    B = [A[1][k] / phi ** A[0][k] for k in range(n)]
    return (A[0], B)

def traceAlpha(n):
    values = getAlpah(n)
    plt.plot(values[0], values[1])
    plt.show()

def fibo(n):
    a, b = 1, 1
    for i in range(n):
        c = a + b
        b = a
        a = c
    return c
        
def firecrapB(n):
    if (n == 1):
        return ([1,1])
    l = firecrap(n-1)
    return [l[1], sum(l)]

def firecrap(n):
    A = firecrapB(n)
    return (A[0] + A[1])

print(firecrap(30))
