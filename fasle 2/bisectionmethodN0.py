# parinaz kanan
def f(x):
    return x**3-5*x-9

# Implementing Bisection Method
def bisection(x0,x1,e):
    step = 1
    condition = True
    
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        if (step > e):
            condition = False

    print('\nRequired Root is : %0.8f' % x2)



x0 = input('a: ')
x1 = input('b: ')
N = input('N0: ')


x0 = float(x0)
x1 = float(x1)
e = int(N)



if f(x0) * f(x1) > 0.0:
    print('f(a)*f(b) already > 0')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)