# Imports ------------------------------------------------------------------
from helpers.help import around
from test.exceptedOutput import pointsOuput

# Calculs des points -------------------------------------------------------
A = points(10, 0.5, 1, 0)
print(around(A) == pointsOuput)
