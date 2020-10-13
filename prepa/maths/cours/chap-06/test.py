import numpy as np
import matplotlib.pylab as plt


def question_7(n):
    X, Y, Y_2 = [k for k in range(2, n)], [], []
    S = 0
    for x in X:
        S += ((-1)**x)/x**2
        Y.append(S)
        # Y_2.append(1/np.log(x))
    plt.plot(X, Y)
    # plt.plot(X, Y_2)
    plt.show()


question_7(10000)
