# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:26:22 2019

@author: PONT Sébastien
"""
# Importation of external modules
import numpy as np
import os.path
import matplotlib.pylab as plt

# Importation of constant data
from ressources.donnees import *

# Transform function that return epsilon and sigma


def Transform(m, f):
    return (m/l0, f/S)


def isNumeric(inputList):
    """Return true if all elements in a list are numeric (int or float)"""
    for element in inputList:
        try:
            float(element)
        except:
            return False
    return True


def clearEmptyCells(inputList):
    """
        @inputs  : list
        @returns : same list without empty cells
    """
    return [k for k in inputList if k != '']


def ConvertDataFromCSV(path):
    """Read data from the csv given and return an numpy array filled with this data"""
    materialName = ''  # Name of the tested material
    epsilon = []  # Movemennt of the test piece
    sigma = []  # Force applied on the test piece
    starting = True

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)

    if (os.path.exists(filename)):
        try:
            file = open(filename, 'r')
            for row in file.readlines():
                try:
                    line = clearEmptyCells(row.replace('\n', '').split(';'))
                    if (starting):
                        starting = not starting
                        materialName = line[0]
                    elif (isNumeric(line)):
                        # Data reading from the CSV file
                        movement = float(line[0])
                        force = float(line[1])

                        # Formating of data
                        tranformedData = Transform(movement, force)

                        # Adding data to result that will be returned
                        epsilon.append(tranformedData[0])
                        sigma.append(tranformedData[1])
                except:
                    print('error !')
        finally:
            file.close()
        return (materialName, sigma, epsilon)
    else:
        raise ValueError("File ({}) doesn\'t exists".format(path))


def figure(n):
    plt.xlabel("Allongement relatif $\epsilon$")
    plt.ylabel("Contrainte $\sigma$ (Mpa)")
    plt.title("Essais de traction")

    for n in range(1, n+1):
        A = ConvertDataFromCSV('ressources/essai_' + str(n) + '.csv')
        plt.plot(A[2], A[1], label=A[0])

    plt.legend(loc='center right')
    plt.show()


def rupture(sigma):
    return max(sigma)


def ind(L, e):
    i = 0
    while (L[i] < e and i < len(L)):
        i += 1
    return i


def select(sigma, epsilon):
    # C'est pas optimise... mais c'est pour se servir de la fonction rupture

    # Limite a la rupture
    Rm = rupture(sigma)

    # Index a partir duquel on le depasse
    i = sigma.index(Rm)

    # On coupe les listes
    sigma = sigma[:i]
    epsilon = epsilon[:i]

    # Maintenant on sélectionne les bonnes valeurs
    mini = ind(sigma, 0.08 * Rm)
    maxi = ind(sigma, 0.45 * Rm)

    # On coupe les listes
    sigma = sigma[mini:maxi]
    epsilon = epsilon[mini:maxi]

    return (sigma, epsilon)


def somme(sigma, epsilon):
    sigma = np.array(sigma)
    epsilon = np.array(epsilon)
    n = sigma.shape[0]
    Sxi = np.sum(epsilon)
    Syi = np.sum(sigma)
    Sxiyi = np.sum(epsilon * sigma)
    Sxi2 = np.sum(epsilon**2)
    return (Sxi, Syi, Sxiyi, Sxi2, n)


def young(sigma, epsilon):
    sigma, epsilon = select(sigma, epsilon)
    Sxi, Syi, Sxiyi, Sxi2, n = somme(sigma, epsilon)
    E = ((n * Sxiyi) - (Sxi * Syi)) / ((n * Sxi2) - (Sxi ** 2))
    sigm0 = (Syi - E * Sxi) / (n)

    return (E, sigm0)


def test(A, B, E, sigm0):
    for i in range(10):
        valTh = E * A[i] + sigm0
        valRel = B[i]
        if(valRel < 1.05 * valTh):
            return False
        return True


def lim_el(sigma, epsilon, E, sigm0):
    iMax = len(epsilon) - 1
    i = 0
    while (not test(sigma, epsilon,  E, sigm0) and i <= iMax - 10):
        i += 1
    if (i != 0):
        return(sigma[i])
    else:
        return (0)


A = ConvertDataFromCSV('ressources/essai_1.csv')
B = select(A[1], A[2])
E, sigm0 = young(A[1], A[2])
print(lim_el(B[0], B[1], E, sigm0))
