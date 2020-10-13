def varia(X):
    E2 = sum([i**2*X[i] for i in range(len(X))])
    E = espe(X) ** 2
    return (E2 - E)
