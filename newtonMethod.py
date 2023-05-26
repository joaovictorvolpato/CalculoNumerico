#Here we implement the scrip corresponding to the false position method

import numpy as np
from math import sin, cos, exp
#import matplotlib.pyplot as plt

def f(x):
    return exp(x)-4*(x**2)

def functionDerivative(x):
    return exp(x)-8*(x) 

def newtonMethod():
    error = 1
    precision = 10e-6
    ite = 0
    x0 = 1
    fx = f(x0)
    while(abs(error) > precision):
        ite += 1
        #define xk and where it is
        #check the interval where the root is
        x0 = x0 - fx/functionDerivative(x0)
        fx = f(x0)
        error = fx
        print(fx)
        #print(f'ite {ite}, xk {xk}, a: {a} , b: {b}')
    return x0, ite

#não funciona
def secantMethod():
    error = 1
    precision = 10e-10
    ite = 0
    x0 = 0 #first guess
    x1 = 1 #second guess
    fx = functionToBeAnalysed(x0)
    while(abs(error) > precision):
        ite += 1
        #define xk and where it is
        #check the interval where the root is
        fx0 = functionToBeAnalysed(x0)
        fx1 = functionToBeAnalysed(x1)
        xk = x0 - (fx * (x1-x0) / (fx1 - fx))
        x0 = x1
        x1 = xk
        fxk = functionToBeAnalysed(xk)
        print(f'ite {ite}, fxk {fxk}, xk {xk}')
    return xk, ite

def secant(x1, x2):
    E = 10e-10
    n = 0; xm = 0; x0 = 0; c = 0;
    #if (f(x1) * f(x2) < 0):
    while True:  
        # calculate the intermediate value
        x0 = ((x1 * f(x2) - x2 * f(x1)) /
                            (f(x2) - f(x1)));
 
        # check if x0 is root of
        # equation or not
        c = f(x1) * f(x0);
 
        # update the value of interval
        x1 = x2;
        x2 = x0;
 
        # update number of iteration
        n += 1;
 
        # if x0 is the root of equation
        # then break the loop
        if (c == 0):
            break;
        xm = ((x1 * f(x2) - x2 * f(x1)) /(f(x2) - f(x1)));
             
        if(abs(xm - x0) < E):
            return xm, n

#def plotFunction():
#    x = np.linspace(-1,2,50)
#    y = f(x)
#    plt.plot(x,y)
#    plt.show()


#xm, res = iterativeFalsePosition(0,2,0.0000001)
res,ite = newtonMethod()
print(res)
print(ite)
#plotFunction()
#print(res)
#print(xm)

