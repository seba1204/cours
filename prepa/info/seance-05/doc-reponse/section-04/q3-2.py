# On calcule les coordonnees
G, H = angle(0.1, degTorad(118.2), 1000)

# On cherche le maximum pour le comparer aux valeurs exp.
i = H.index(max(H))

# On trace tout ca
plt.plot(G, H)
plt.xlabel("$\\theta_m$")
plt.ylabel('$\dot{\\theta}_v$')
plt.plot(G[i], H[i], 'rx', label=f'({G[i]:.3f}, {H[i]:.3f})')
plt.legend()
plt.show()
