#This file implements the code for polynomial Interpolation

#First we have to provide a set o x and f(x) points

x = [-1, 0, 1]
fx = [4, 1, -1]
order = len(x)

#Then we need to create the matrix

A = [[]]

for i in range(order):
    for j in range(order):
        A[i][j] = x[i]**j

#Then we need to solve the matrix, A, fx=b, solve for [a1,a2,a3]

from gaussElimination import partial_pivot

x, o, y, b = partial_pivot(A, fx)

#the [a1,a2,a3] values are in the x vector, a1,a2,a3 being the coefficient of the polynomial P(x) = a1x⁰ + a2x¹ + a3x²  

print(f'P(x) = {x[1]} {x[2]}x {x[3]}x² ')

# To calculate P of i

for i in range(order):
    pi =  sum(A[j] * x[i]**j for j in range(order))



