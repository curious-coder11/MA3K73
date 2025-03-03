from math import gcd

def addFrac(a,b):
    x,y = a
    p,q = b
    g = x*q+y*p
    h = y*q
    n = gcd(g,h)
    return [int(g/n),int(h/n)]

n = 23
a = [1,1]
b = [1,2]
values =[a,b]
for i in range (n):
    x = [a[0],a[1]*2]
    y = [b[0],b[1]*2]
    values.append(addFrac(x,y))
    a = values[-2]
    b = values[-1]

x = values[-1]
y = x[0]/x[1]
print(x,y)
