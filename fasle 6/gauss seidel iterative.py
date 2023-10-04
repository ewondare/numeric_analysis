import numpy as np
n = int(input("Enter n: "))
A = eval(input("enter enrties in A in a single row in [...]: "))
a = np.zeros((n,n))
b = eval(input("enter entries in vector b: "))
X0 = eval(input("enter initial vector X0 for Ax = b: "))
l = 0
while(l < n*n):
    for i in range(n):
        for m in range(n):
            a[i][m] = A[l+m]
        l += n
iteration = 7 #k
error_Tol = 10e-3
N = 0
X = []
fl = 0
while(N <= iteration):
    for i in range(n):
        s = 0 # sum for second sigma
        ss = 0 # sum fot first sigma
        for m in range(i):
                ss += a[i][m]*X[m]
        for m in range(i+1,n):
                s += a[i][m]*X0[m]
        X.append((1/a[i][i])*(-s -ss + b[i])) 
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
        if (N > 0):
            print("iteration:" , N , "X:" , X)
        X = []
if(N == iteration and fl != 1):
    print("didnt find an answer")