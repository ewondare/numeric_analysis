# Parinaz Kanan
import numpy as np
import math

def f(x):
    x = math.sin(x)
    return x


a = float(input("a: "))
b = float(input("b: "))

n = 6
R = np.zeros((n,n))
h = [b -a ,]
# T(h)
R[0][0] = (h[0] / 2) * (f(a) + f(b))

for i in range(1,n):
    # calculate T(h/i) by trapezoidal method
    fs = 0  
    h.append(h[i-1]/2)
    for m in range(1,pow(2,i-1)):
        fs += f(a + (2*m - 1)*h[i])
    R[i][0] = 1/2*(R[i-1][0] + h[i - 1]*fs)
h = b - a   

'''
t(0,0)  t(1,0) ...... t(n,0)
t(0,1)  t(1,1)
.
.
.      t(1,n-1)
t(0,n)
'''

'''
I =1/i^4 * T(m)(i-1) - T(m-1)(i-1)
'''
for i in range(1,n):
    for m in range(i,n):
        R[m][i] = R[m][i - 1] + (1/(pow(4,i) - 1)) * (R[m][i-1] - R[m - 1][i - 1])    
         
for i in range(n):
    print("\n")
    for m in range(n):
        if(R[i][m] != 0):
            print(R[i][m] , end = " ")
