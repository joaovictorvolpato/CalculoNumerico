import numpy as np
#import matplotlib as plt
from math import exp, sin, cos


def funcx(x):
    return exp(x)+4*(x**2)
    #return np.divide(27895,9.1 - np.power(x,2))

#Recusive aproach to implementing the bipart method
def recursiveBipartMethod(a,b,precision,ite):
    Xm = np.divide(a+b,2)
    Fxm = functionToBeAnalysed(Xm)
    error = Fxm - 0
    #Stop condition for the recursion
    if (abs(error) < precision):
        #print(type(Xm))
        #print(type(ite))
        return Xm, ite
    ite = ite + 1
    #Given an [a,b] interval, we check where the root of the function is
    if (isValidInterval(a,Xm)):
        bipartMethod(a,Xm, precision, ite)
    else:
        bipartMethod(Xm,b, precision, ite)
    
#Iterative aproach to implementing the bipart method
def iterativeBipartMethod(a,b,precision):
    error = 1
    ite = 0
    #Xm = 0
    #while our error is no less than the precision we set, the method contiues
    while(abs(error) > precision):
        #print("entrou")
        ite = ite + 1
        Xm = (a + b)/2
        Fxm = functionToBeAnalysed(Xm)
        
        #check where the the root of the function is
        if (isValidInterval(a,Xm)):
            b = Xm
        else:
            a = Xm
        error = Fxm - 0 

    return Xm, ite

#Bolzanos Theorem
def isValidInterval(a,b):
    if (functionToBeAnalysed(a)*functionToBeAnalysed(b) < 0):
        return True
    else:
        return False

def functionToBeAnalysed(x):
    return exp(x)-4*(x**2)
    


#Find sin(3x),with 10e-6

#xm, result = bipartMethod(0,1,0.0000000001,0)
xm, res = iterativeBipartMethod(0,2,10e-6)
print(xm)
print(res)

#first = funcx(3)
#snc = funcx(3.000001)
#print(first)
#print(snc)


