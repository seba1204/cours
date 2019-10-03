import matplotlib.pyplot as plt
import numpy as np
import sys

print ('Argument List:', str(sys.argv))

def extractData(path):
    X, Y=[], []
    try:
        file = open(path, "r")
        for row in file.readlines():
            try:
                X.append(float(row.split(';')[0].replace(',','.')))
                Y.append(float(row.split(';')[1].replace(',','.')))
            except:
                pass
    finally:
        file.close()
    return (X, Y)

# A = extractData('data.csv')

# s = A[0]
# t = A[1]

# plt.magnitude_spectrum(s, scale='dB',color='C1')
# plt.show()