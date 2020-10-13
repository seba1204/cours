def deriveekieme(Y, X, k):
    if k == 0:
        return Y
    else:
        Z = [(Y[i+1]-Y[i])/(X[i+1]-X[i]) for i in range(len(Y)-1)]
        return deriveekieme(Z, X, k-1)
