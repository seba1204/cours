import numpy as np
import matplotlib.pylab as plt

def tri_debut(A, i):
    V = A[i]
    k=i-1
    while plusGrandQue(A[k], V) and k>=0:
        A[k+1] = A[k]
        k-=1
    A[k+1] = V

def tri_insertion(A):
    for i in range(1, len(A)):
        tri_debut(A, i)

def plusGrandQue(a, b):
    if type(a) == list:
        return a[0] > b[0] or (a[0] == b[0] and a[1] > b[1])
    else:
        return a > b



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
A = ellipse(100)
A = combine(A[0], A[1])

tri_insertion(A)
C = decombine(A)

plt.plot(C[0], C[1])
plt.show()