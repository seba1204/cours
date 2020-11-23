import pylab as pl
import numpy as np

borneDomaineInf=-20
borneDomaineSup=20
PrecisionCourbe=100

xlabel=""
ylabel=""

X=np.linspace(borneDomaineInf, borneDomaineSup, PrecisionCourbe)
Y=np.exp(-X/10)
Y2=np.cos(X-(np.pi/4))*Y
Y3=-Y
pl.xlabel(xlabel)
pl.ylabel(ylabel)
pl.xlim=(min(X) - 2, max(X)+2)
pl.ylim=(min(Y), max(Y))
pl.plot(X,Y,color="red", linewidth=2, label="cos")
pl.plot(X,Y2,color="blue", linewidth=2, label="exp")
pl.plot(X,Y3,color="red", linewidth=2, label="-cos")
pl.grid()
pl.legend()
pl.show()
pl.close()