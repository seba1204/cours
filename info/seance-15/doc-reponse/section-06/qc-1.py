class Ellipse():
    def GetAire(self, t):
        A = []
        aire = 0
        R = np.array([
            [np.cos(t), -np.sin(t)],
            [np.sin(t), np.cos(t)]
        ])
        for i in range(len(self.X)):
            u = np.array([self.X[i], self.Y[i]])
            v = np.dot(R, u)
            if(v[0] > 0 and v[1] > 0):
                A.append(v)

        for i in range(len(A)-1):
            aire += A[i+1][1] * abs(A[i+1][0] - A[i][0])
        return aire * 4
