import numpy as np

def dicho(f, a, b,eps):
    if( abs(a-b) < 2*eps ):
        return((a+b)/2)
    m = (a+b)/2
    if(f(a)*f(m)<0):
        return (dicho(f, a, m, eps))
    return (dicho(f, m, b, eps))
f = lambda x : x**3 - 3 * x - 1

def getRooth(eps):
    a, b = -2, -1
    alpha = dicho(f, a, b, eps)
    a, b = -1, 1
    beta = dicho(f, a, b, eps)
    a, b = 1, 2
    gammmmma = dicho(f, a, b, eps)

    return(alpha, beta, gammmmma)

def puissance(R, Rb, n):
    return (np.linalg.matrix_power(R, n), np.linalg.matrix_power(R, n))

R = np.array([[0,0,1], [1,0,3], [0, 1, 0]])

racines = getRooth(0.0000001)
D = np.array([
    [racines[0],0,0],
    [0, racines[1], 0],
    [0, 0, racines[2]]
    ])
P = np.array([[1, 1, 1],
             [racines[0]**2, racines[1]**2,racines[2]**2],
             [racines[0], racines[1],racines[2]]])

P1 = np.linalg.inv(P)
Rb = np.dot(np.dot(P, D), P1)

print(puissance(R, Rb, 10)[0])
