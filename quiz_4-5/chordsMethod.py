a = 1.0
b = 2.0
tol = 0.0001
max_iter = 20

x0 = a

for i in range(max_iter):
    f_x0 = x0**3 - x0 - 2
    f_b = b**3 - b - 2

    x1 = x0 - f_x0 * (b - a) / (f_b - f_x0)

    print("Iteration", i+1, ": x =", x1)

    if abs(x1 - x0) < tol:
        print("Approximate root:", x1)
        break

    x0 = x1
else:
    print("Method did not converge in", max_iter, "iterations")
