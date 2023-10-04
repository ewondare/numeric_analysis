
def f(x):
    return x**2-5*x-9

def falsePosition(x0,x1,e):
    step = 1
    condition = True

    while condition:
        x2 = x0 - (((x1-x0) * f(x0))/( f(x1) - f(x0) ))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


x0 = input('x0: ')
x1 = input('x1: ')
e = input('Tol: ')

x0 = float(x0)
x1 = float(x1)
e = float(e)

if f(x0) * f(x1) > 0.0:
    print('f(a) * f(b) already > 0.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)