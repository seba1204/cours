def figure(n):
    plt.xlabel("Allongement relatif $\epsilon$")
    plt.ylabel("Contrainte $\sigma$ (Mpa)")
    plt.title("Essais de traction")

    for n in range(1, n+1):
        A = ConvertDataFromCSV('ressources/essai_' + str(n) + '.csv')
        plt.plot(A[2], A[1], label=A[0])

    plt.legend(loc='center right')
    plt.show()
