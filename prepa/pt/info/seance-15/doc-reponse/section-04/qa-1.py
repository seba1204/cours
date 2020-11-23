class Liste(list):
    def trier(self):
        for i in range(1, len(self.A)):
            self._triDebut(i)

    def time(self, n, show=False):
        X, T = [], []
        for i in range(1, n):
            self.generateRadomList(i)
            start = time.time()
            self.trier()
            end = time.time()

            X.append(i)
            T.append(np.sqrt(end - start))
        if (show):
            plt.plot(X, T, label='$\sqrt{t}$')
            plt.show()
