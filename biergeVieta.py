import numpy as np
#import matplotlib.pyplot as plt
import math


#We represent the polynomial as a lista of its coefficients
#the first element of the list is the coefficient of the highest degree
#when the coeficient is 0, it means the polynomial doesnt have that degree
#example: x^3 + 2x^2 - x + 1 = [1,2,-1,1]
#So polynomial[0] has the coefficient of the highest degree, so the highest degree is len(polynomial) - 1


#Here we calculate the polynomial for a given x
def calculatePolynomial(polynomial:list, x:float):
    result = 0
    for i in range(len(polynomial)):
        result += polynomial[i] * np.power(x, len(polynomial) - 1 - i)
    return result

def calculateR(polynomial:list, x:float):
    resultb = [None] * len(polynomial)
    resultc = [None] * len(polynomial)
    resultb[0] = polynomial[0]
    resultc[0] = polynomial[0]
    for i in range(1,len(polynomial)):
        resultb[i] = polynomial[i] + np.multiply(x,resultb[i-1])
        #print(f'restulb{i}, : {resultb[i]}')
        resultc[i] = resultb[i] + np.multiply(x, resultc[i-1])
        #print(f'restulc{i}, : {resultc[i]}')
    #print(resultb[len(polynomial)-1], resultc[len(polynomial)-2])
    return resultb[len(polynomial)-1], resultc[len(polynomial)-2]

def BiergeVieta(polynomial:list, x0:float, precision:float):
    ite = 0
    error = calculatePolynomial(polynomial, x0)
    while(abs(error) > precision):
        R, R1 = calculateR(polynomial, x0)
        x0 = x0 - np.divide(R,R1)
        ite += 1
        error = calculatePolynomial(polynomial, x0)
        print(R)
    return x0, ite

def plotPolynomial(polynomial:list, x0:float):
    x = np.linspace(-10,10,100)
    y = [None] * len(x)
    for i in range(len(x)):
        y[i] = calculatePolynomial(polynomial, x[i])
    plt.plot(x,y)
    plt.plot(x0, calculatePolynomial(polynomial, x0), 'ro')
    plt.show()

polynomial = [1,-9,27,-31,12]
x0 = 6
precision = 10e-8
x, ite = BiergeVieta(polynomial, x0, precision)
#plotPolynomial(polynomial, x)
print(f'x: {x}, ite: {ite}')
