import numpy as np

def gaussMethod(matrix, ans):
    result = np.linalg.solve(matrix, ans)
    return  result

matrix = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]]
])

ans = np.array([8, -11, -3])

print(gaussMethod(matrix, ans))
