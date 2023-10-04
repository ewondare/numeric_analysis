# Parinaz Kanan
def f(t,y):
    return t*y + t**3


a =  input("a in [a,b]:")
b = input("b in [a,b]:")
n = input("enter n: ")
x = input("f(x0): ")

a = float(a)
b = float(b)
n  = int(n)
x = float(x)


h = (b - a) / n
t = a
y = x

# Yi+1 = Yi + F(xi,yi)h
# where F is derivative of y
# we also have y(x0)


#print x0 , Y(x0):
print(f"({t} , {y})")
#calculate Y(xi) for i = x0+ 1h , x0+ 2h, .... , y+nh
for i in range(1,n+1):
    y = y + h * f(t , y)
    t = a + i * h
    print(f"({t} , {y})")
