#pivot de gauss
# -> determinant

import numpy as np 

################################################
##DIMENSION DES MATRICES

def dim(A):
    taille = np.shape(A)
    return taille

#TEST def
# b = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# n = dim(b)[0]
# m = dim(b)[1]
# print(n, m)

################################################
##PRODUIT MATRICIEL

def produitMat(A, B):
    if dim(A)[1] == dim(B)[0]:
        multiple = np.dot(A,B)
        return multiple

    else:
        return 'ERREUR : Les matrices n ont pas les bonnes dimensions'

# #TEST produitMat
# a = np.array([[2, 2],
#                 [2, 2]])
# b = np.array([[1, 1],
#                 [1, 1]])
# c = np.array([[1, 1],
#                 [1, 1],
#                 [1, 1]])

# ab = produitMat(a, b)
# ac = produitMat(a, c)
# print(ab, ac)

################################################
##TRANSPOSITION

def transpose(A):
    transposee = A.T
    return transposee

# #TEST transpose

# a = np.array([[2, 2, 3]])
# t = transpose(a)
# print(t)

################################################
##DETERMINANT

def det(A):
    determinant = np.linalg.det(A)
    return determinant

# #TEST det

# a = np.array([[2, 2],
#             [0, 2]])
# b = np.array([[2, 2],
#             [2, 2]])
# c = np.array([[2, 2, 3],
#             [0, 2, 3],
#             [0, 0, 3]])

# d1 = det(a)
# d2 = det(b)
# d3 = det(c)
# print(d1, d2, d3)

################################################
##INVERSE

def inverse(A):
    if det(A) != 0:
        inversee = np.linalg.inv(A)
        return inversee
    else:
        return 'ERREUR : La matrice n est pas inversible'

# #TEST inverse

# a = np.array([[2, 2],
#             [0, 2]])
# b = np.array([[2, 2],
#             [2, 2]])

# invA = inverse(a)
# invB = inverse(b)
# print(invA, invB)