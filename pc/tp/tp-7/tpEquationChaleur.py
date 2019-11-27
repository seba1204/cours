import numpy as np

N = 11


def initTab(dim):
    temp = np.array([[0 for k in range(dim)] for l in range(dim)])
    for i in range(0, dim):
        temp[i][0] = 10 * i
        temp[i][dim-1] = -10 * i
        temp[dim-1][i] = 100 - 20 * i
    return temp


def oneLoop(temp, precision, loopMax):
    dim = np.shape(temp)[0]-1
    newTemp = np.array(temp)
    delta = precision + 1
    loopNb = 0
    while (delta > precision and loopNb < loopMax):
        if (delta > precision):
            loopNb += 1
            print('on tourne dans le vide')
        elif loopNb > 0:
            loopNb = 0
        delta = 0
        for line in range(1, dim):
            for row in range(1, dim):
                oldValue = newTemp[line][row]
                newValue = temp[line-1][row] + \
                    temp[line+1][row] + \
                    temp[line][row - 1] + \
                    temp[line][row + 1]
                newValue /= 4
                newTemp[line][row] = newValue
                delta += abs(oldValue - newValue)
        delta /= (dim - 1)**2
    return newTemp


print(oneLoop(initTab(N), 10**(-5), 10))
