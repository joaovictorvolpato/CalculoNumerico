#Here we implement the scrip corresponding to the false position method

import numpy as np
import math
import matplotlib.pyplot as plt

def functionToBeAnalysed(x):
    return np.multiply(np.exp(x),-2 *np.cos(x))

def iterativeFalsePosition(a,b,precision):
    error = 1
    ite = 0
    while(abs(error) > precision):
        
        ite += 1
        #findd (a, f(a)) and (b, f(b)) points
        fa = functionToBeAnalysed(a)
        fb = functionToBeAnalysed(b)
        print(f'fa {fa}, fb {fb}')
        #define xk and where it is
        xk = (np.divide(a * fb - b * fa, (fb - fa)))
        Fxk = functionToBeAnalysed(xk)
        #check the interval where the root is
        if (isValidInterval(a,xk)):
            b = xk
        else:
            a = xk
        #define the error
        error = Fxk - 0
        #print(f'ite {ite}, xk {xk}, a: {a} , b: {b}')
    return xk, ite


def iterativeModifiedFalsePosition(a,b,precision):
    error = 1
    ite = 0
    fa = functionToBeAnalysed(a)        
    fb = functionToBeAnalysed(b)
    while(abs(error) > precision):
        ite += 1
        #define xk and where it is
        xk = (np.divide(a * fb - b * fa, (fb - fa)))
        Fxk = functionToBeAnalysed(xk)
        #check the interval where the root is
        if (isValidInterval(a,xk)):
            b = xk
            pa = np.divide(fb,fb + Fxk)
            fb = Fxk
            fa = np.multiply(pa, fa)
            print(f'iterac {ite}, fa {fa}, fb {fb}')
        else:
            a = xk
            pb = np.divide(fa,fa + Fxk)
            fa = Fxk
            fb = np.multiply(pb, fb) 
            print(f'iterac {ite}, fa {fa}, fb {fb}')
        #define the error
        error = Fxk
        #print(f'ite {ite}, xk {xk}, a: {a} , b: {b}')
    return xk, ite

def isValidInterval(a,b):
    if (np.multiply(functionToBeAnalysed(a),functionToBeAnalysed(b)) < 0):
        return True
    else:
        return False

def plotFunction():
    x = np.linspace(0,2,50)
    y = functionToBeAnalysed(x)
    plt.plot(x,y)
    plt.show()


#xm, res = iterativeFalsePosition(0,2,0.0000001)
xm, res = iterativeModifiedFalsePosition(0,2,0.0000001)
print(res)
print(xm)
plotFunction()

