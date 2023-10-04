# Parinaz Kanan
def f(x):
    return 1/(1 + x**2)


def trapezoidal(x0,xn,n):
    h = (xn - x0) / n
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    

    integration = integration * h/2
    
    return integration

a = float(input("enter a in [a,b]:"))
b = float(input("Enter b in [a,b]: "))
n = int(input("Enter n: "))

# Call trapezoidal() method and get result
result = trapezoidal(a, b, n)
print("Integration result: %0.6f" % (result) )


import numpy as np

def integral(f, a, b):
    desired_error = 0.05
    n = 1
    previous_integration = 0
    current_integration = (f(a) + f(b)) * (b - a) / 2
    
    while abs(current_integration - previous_integration) > desired_error:
        n *= 2
        h = (b - a) / n
        x = np.linspace(a, b, n+1)
        y = f(x)
        previous_integration = current_integration
        current_integration = (h/2) * ((2*np.sum(y)) - y[0] - y[-1])
        

    return current_integration