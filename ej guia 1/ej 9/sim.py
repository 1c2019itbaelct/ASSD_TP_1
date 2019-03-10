import matplotlib.pyplot as plt
import numpy as np
import array as arr


def f(t):
    'A damped exponential'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    return s1 * e1

def myDelta(n):
    return(n==0)

def myU(n):
    return(n>=0)


def mySistem(n , x,a,b):
    solution=arr.array('f')
    for i in n:
        ypree=0
        ypre=0
        preb=i-1
        prebb=i-2
        if preb>=0:
            ypre=solution[preb]
        if prebb>=0:
            ypree = solution[prebb]
        d=0.5*x(i-2)
        solution.append(d+(a*ypre)+(b*ypree))



    return solution



t1 = np.arange(30)
y1=mySistem(t1,myU,(5/4),-(25/32))

l = plt.plot(t1, y1, 'ro')
plt.xlabel('Time')
plt.ylabel('Y(nT)')
plt.title('Respuesta al escalon')
plt.setp(l, markersize=10)
plt.setp(l, markerfacecolor='C0')
plt.show()