def traceTimeFirect(n):
    X, T = firecTime(n)
    Xp = [phi ** k for k in X]
    plt.plot(Xp, T)
    plt.show()
