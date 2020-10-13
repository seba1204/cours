def lignes(n, k0, k1):
    pas = 0.01
    k = k0
    while(k <= k1):
        def g(x):
            return f([x, x]) - k
        c = racine(g, -10, 10)
        if (c != None):
            plt.plot(c, c, 'b.')
            traceLigne(points(n, pas, c, c))
        k += 1

lignes(3000, 1, 8)
plt.show()
