import numpy as np
n = int(input("#of equations and unknowns: "))
A = eval(input("enter enrties in A by row: "))
a = np.zeros((n,n))
b = eval(input("enter entries in vector b: "))
X0 = eval(input("enter initial vector X0 for Ax = b: "))
l = 0
while(l < n*n):
    for i in range(n):
        for m in range(n):
            a[i][m] = A[l+m]
        l += n
iteration = 1000
error_Tol = 10e-3
N = 0
X = []
fl = 0
while(N <= iteration):
    for i in range(n):
        s = 0
        for m in range(n):
            if(m != i):
                s += a[i][m]*X0[m]
        X.append((1/a[i][i])*(-s + b[i])) 
    ll = []
    for i in range(n):
        ll.append(abs(X[i] - X0[i]))
    if(max(ll) < error_Tol):
        print(X,end = " ")
        break
        fl = 1
    else: 
        N = N + 1
        X0 = X
        X = []
if(N == iteration and fl != 1):
    print("didnt find an answer")
        