def graphe():
    x = np.array([300, 700, 800, 1000, 1500, 2000, 3000])
    y = [temps(n)*np.log(n)/n for n in x]
    plt.plot(x, y, 'x')  # donne la constante C
    plt.show()
