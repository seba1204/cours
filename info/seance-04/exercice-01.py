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
from Ressources.data  import *

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
    materialName = '' # Name of the tested material
    epsilon = [] # Movemennt of the test piece
    sigma = [] # Force applied on the test piece
    starting = True
    
    if (os.path.exists(path)):
        try:
          file = open(path, 'r')
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
                  print ('error !')
        finally:
                  file.close()
        return (materialName, sigma, epsilon)
    else:
        raise ('File ({}) doesn\'t exists'.format(path))

def Trace(materialName, sigma, epsilon):
    plt.plot(epsilon, sigma, label=materialName)

A = ConvertDataFromCSV('Ressources/essai_1.csv')
Trace(A[0], A[1], A[2])



plt.show()