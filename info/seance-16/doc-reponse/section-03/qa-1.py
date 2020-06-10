def traceLigne(A):
    A = np.array(A)
    X, Y = A[:, 0], A[:, 1]
    plt.plot(X, Y)
    plt.show()


A = points(3000, 0.1, 1, 0)
traceLigne(A)
