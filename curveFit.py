#Código para fazer ajuste de curvas em python usando o método dos minimos quadrados

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Definindo os pontos
# n -> número de pontos
# m -> grau do polinômio de ajuste
x = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y = np.array([3.16, 2.38, 1.75, 1.34, 1, 0.74, 0.56])

m = 1
n = len(x)

def polynomial_curve_fit(x, y, m):
    A = [[0 for i in range(m + 1)] for j in range(m + 1)]
    b = [0 for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(m + 1):
            A[i][j] = sum([x[k]**(i + j) for k in range(n)])
        b[i] = sum([y[k] * x[k]**i for k in range(n)])

    #gives the coefficients of the polynomial
    return np.linalg.solve(A, b)

#Exponential curve fit general form: y = Ae^(bx), we linearize it by taking the natural log of both sides to get: ln(y) = ln(A) + Bx. ln(y) = z, ln(A) = c0
#So we end up solving for z = c0 + bx, that means we only have a 2x2 matrix to solve for
def exponential_curve_fit(x, y):
    A = [[0, 0], [0, 0]]
    b = [0, 0]

    A[0][0] = n
    A[0][1] = sum([x[i] for i in range(n)])
    A[1][0] = sum([x[i] for i in range(n)])
    A[1][1] = sum([x[i]**2 for i in range(n)])

    b[0] = sum([np.log(y[i]) for i in range(n)])
    b[1] = sum([x[i] * np.log(y[i]) for i in range(n)])

    #gives the coefficients of function but we need to convert it back to the exponential form
    ret =  np.linalg.solve(A, b)
    print(np.exp(ret[0]), ret[1])
    return np.exp(ret[0]), ret[1]


def plot_curve_and_scatter(x, y, m):
    plt.scatter(x, y)
    a = polynomial_curve_fit(x, y, m)
    x_values = np.linspace(min(x) - 1, max(x) + 1, 200)
    y_values = np.array([sum([a[i] * x_values[j]**i for i in range(m + 1)]) for j in range(200)])
    plt.plot(x_values, y_values, 'r')
    plt.scatter(x, y)
    plt.show()

def plot_curve_and_scatter_exponential(x, y):
    plt.scatter(x, y)
    a, b = exponential_curve_fit(x, y)
    x_values = np.linspace(min(x) - 1, max(x) + 1, 200)
    y_values = np.array([a * np.exp(b * x_values[j]) for j in range(200)])
    plt.plot(x_values, y_values, 'r')
    plt.scatter(x, y)
    plt.show()

def main():
    #plot_curve_and_scatter(x, y, m)
    plot_curve_and_scatter_exponential(x, y)

if __name__ == '__main__':
    main()

