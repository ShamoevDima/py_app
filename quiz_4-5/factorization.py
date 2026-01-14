A = [
    [2, 3, 1],
    [4, 7, 7],
    [6, 18, 22]
]

n = len(A)

L = [[0]*n for _ in range(n)]
U = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j:
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        else:
            L[i][j] = A[i][j]
            for k in range(j):
                L[i][j] -= L[i][k] * U[k][j]
            L[i][j] /= U[j][j]
    L[i][i] = 1

print("L matrix:")
for row in L:
    print(row)

print("\nU matrix:")
for row in U:
    print(row)
