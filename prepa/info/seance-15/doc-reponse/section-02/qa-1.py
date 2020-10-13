class Liste(list):
    # ...
    def trier(self):
        for i in range(1, len(self.A)):
            self._triDebut(i)
