# Parinaz Kanan
def f(x):
    return 1/(1 + x**2)

def simpson(x0,xn,n):
    h = (xn - x0) / n

    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    
    # Finding final integration value
    integration = integration *  h / 3
    
    return integration
    
# Input section
a = float(input("Enter a: "))
b = float(input("Enter b: "))
n = int(input("Enter n: "))

# Call trapezoidal() method and get result
result = simpson(a, b, n)
print("Integration result by Simpson's 3/8 method is: %0.6f" % (result) )