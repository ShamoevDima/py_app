
def factorization(matrix):
    A = np.array(matrix)
    L, U = lu_factor(A)

    print("L = " + L)
    print("U = " + U)


A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], float)

factorization(A)
