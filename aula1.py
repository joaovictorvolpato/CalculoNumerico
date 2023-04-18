#Código aula 1

from math import exp, factorial

def sum1(x,y):
    soma = 0
    for i in range(y):
        soma = soma + pow(x,i)/factorial(i)
    return soma

def sum2(x):
    soma = 0
    tolerance = 0.000001
    terms = 0
    error = 1
    absv = exp(x)
    while (error > tolerance):
        soma = soma + pow(x,terms)/factorial(terms)
        terms = terms + 1    
        error = absv - soma
    return soma, terms

res, t = sum2(2)

print(res)
print(t)

