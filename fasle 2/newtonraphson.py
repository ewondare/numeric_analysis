# parinaz kanan
def f(x):
    return x**3 - 5*x - 9

def g(x):
    #define g(x) to be the derivative of f(x)
    return 3*x**2 - 5


def newtonRaphson(x0,e,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('g(x) = 0 , cannot divide by zero')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


x0 = input('x0: ')
e = input('Tol: ')
N = input('N0: ')

x0 = float(x0)
e = float(e)
N = int(N)
newtonRaphson(x0,e,N)