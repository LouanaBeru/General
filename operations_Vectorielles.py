#MODULES

#Fonction : scal
#Parametres : x : list, y : list
#Retourne : < x ; y >
def scal(x, y):
    if len(x) == len(y):
        scal = 0
        for i in len(x):
            scal += x[i] * y[i]
        return scal
    else:
        print('Les vecteurs ne sont pas de mêmes dimensions')
