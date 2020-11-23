class Liste(list):
    def separate(self):
        X, Y = [], []
        for a in self.A:
            X.append(a[0])
            Y.append(a[1])
        return (X, Y)
