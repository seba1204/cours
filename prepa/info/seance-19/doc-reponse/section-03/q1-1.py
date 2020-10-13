def g(x):
    return np.exp(-x**2)*np.sin(x**3)

TraceDerivk(g, 0, 6, 1000, 4)
plt.show()
X = np.linspace(0, 6, 1001)
print(max(deriveekieme(g(X), X, 4)))