# Parinaz Kanan
def f(t,w):
    return w - t**2 + 1

a = input("a in [a,b]: ")
b = input("b in [a,b]: ")
n = input("enter n: ")
x = input("f(x0): ")
a = float(a)
b = float(b)
n  = int(n)
x  = float(x)


h = (b - a) / n
t = a
y = x

#Form of runge kutta (order 4):
#   Yi+1 = Yi + 1/6(k1 + k2 + k3 + k4)
# k1 can be calculated through normal procedure
# yet for spefically using order four, we can calculate them through:
# k1 = h * f(xi + yi)
# k2 = h * f(xi+h/2 + yi+k1/2)
# k3 = h * f(xi + h/2, yi +k2/2)
# k4 = hf(xi + h , yi +k3) 

# x0 and y0:
print(f"({t} , {y})")
for i in range(1,n):

    K1 = h*f(t,y)
    K2 = h*f(t + (h/2),y+(1/2)*K1)
    K3 = h*f(t + (h/2),y+(1/2)*K2)
    K4 = h*f(t + h,y + K3)
    y = y + (K1 + 2*K2 + 2*K3 + K4) / 6
    t = a + (i) * h # we update x to go forward one h
    print(f"({t} , {y})")