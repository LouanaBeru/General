##MODULES
import numpy as np 

################################################
##DIMENSION DES MATRICES

def dim(A):
    A = np.asarray(A)
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
    print(type(B))
    print(dim(B))
    if dim(A)[1] == dim(B)[0]:
        A = np.asarray(A)
        B = np.asarray(B)
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
# d = np.array([[1, 1, 1],
#             [1, 1, 1]])
# e = np.array([[1, 0],
#             [0, 1],
#             [2, 0]])

# ab = produitMat(a, b)
# ac = produitMat(a, c)
# de = produitMat(d, e)
# print(ab,ac, de)

################################################
##TRANSPOSITION

def transpose(A):
    A = np.asarray(A)
    transposee = A.transpose()
    return transposee

# #TEST transpose

# a = np.array([[2, 2, 3]])
# t = transpose(a)
# print(t)

################################################
##DETERMINANT

def det(A):
    A = np.asarray(A)
    if dim(A)[0] == dim(A)[1]:
        determinant = np.linalg.det(A)
        return determinant
    else:
        return 0

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
    if dim(A)[0] == dim(A)[1] and det(A) != 0 :
        A = np.asarray(A)
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

################################################
##PRODUIT NOMBRE MATRICE

def produitMatNbr(nbr, A):
    A = np.asarray(A)
    n = dim(A)[0]
    m = dim(A)[1]
    for i in range(n):
        for j in range(m):
            A[i][j] = nbr * A[i][j] 
    return A

# #TEST produitMatNbr

# A = [[1, 0],
#     [1, 2]]

# B = [[1, 2, 3]]
# a = 3
# b = -2

# aA = produitMatNbr(a, A)
# bA = produitMatNbr(b, A)
# aB = produitMatNbr(a, B)
# bB = produitMatNbr(b, B)


# print(aA) 
# print(bA)
# print(aB) 
# print(bB)