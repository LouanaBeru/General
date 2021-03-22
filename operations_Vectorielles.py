#MODULES
import numpy as np

#Fonction : scal
#Parametres : x : list, y : list
#Retourne : < x ; y >
def scal(x, y):
    print('lenx = ', len(x))
    print('leny = ', len(y))
    if len(x) == len(y):
        scal = 0
        x = np.asarray(x)
        y = np.asarray(y)
        for i in len(x):
            scal += x[i] * y[i]
        scal = float(scal)
        print('scal =' ,scal)
        return scal
    else:
        print('ERREUR <scal> : Les vecteurs ne sont pas de mêmes dimensions')
