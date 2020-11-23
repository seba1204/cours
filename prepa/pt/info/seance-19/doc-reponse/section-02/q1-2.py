def f(x):
    return np.sin(x)

def TraceDerivk(f, a, b, n, k):
    X = np.linspace(a, b, n+1)
    yk = deriveekieme(f(X), X, k)
    c = 'g' if k % 2 == 0 else 'r'
    plt.plot(X[:-k], np.abs(yk), color=c, label=f'k={k}')

def TraceDeriv(f, a, b, n):
    for k in range(1, 7):
        TraceDerivk(f, a, b, n, k)
    plt.legend()
    plt.show()
