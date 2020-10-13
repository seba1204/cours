def traceTemps(N):
    Y = []
    for n in N:
        Y.append(temps_rapide(n))
    plt.plot(N*np.log(N), Y, 'rx')
    plt.show()
