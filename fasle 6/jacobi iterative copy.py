# Parinaz Kanan
import numpy as np
n = 2
a = [[2,3],[3,4]]
b = [4,5]
X0 = [0,0]
l = 0
iteration = 5 #k
error_Tol = 10e-3
N = 0
X = []
fl = 0
'''
while N<iteration:
    for i = 1,...,n
    Xi = 1/aii ( - sum + bi)
    
    '''
while(N <= iteration):
    
    for i in range(n):
        s = 0
        for m in range(n):
            
            if(m != i):
                #only if m != i the sum will be updated
                
                s += a[i][m]*X0[m]
        X.append((1/a[i][i])*(-s + b[i])) 
    ll = []
    for i in range(n):
        ll.append(abs(X[i] - X0[i]))
    else: 
        N = N + 1
        X0 = X
        if (N > 0):
            print("iteration:" , N , "X:" , X)
        X = []
        if(max(ll) < error_Tol):
            print(X,end = " ")
            break
if(N == iteration and fl != 1):
    print("didnt find an answer")


        

