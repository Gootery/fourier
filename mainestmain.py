import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as spi

def comprehend(enput):
    words = ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt']
    for word in words:
        if word in enput:
            enput = enput.replace(word, 'np.' + word)
    return enput

enput = comprehend(input("Give me a piecewise continuous function (make it valid in Python, ex: x**2 is the function x^2): "))
L = input("Input your bound (-L to L, input 'pi' for pi):")
n = input("How many terms do you wanna approximate it to(around 150ish and everything past it stops working): ")
if L == 'pi':
    L = np.pi
else:
    L = float(L)

f = lambda x: eval(enput, {'np': np, 'x': x})
def a_n(n):
    aofn = spi.quad(lambda x: f(x) * np.cos(n * np.pi * x / L), -L, L)
    return aofn[0] / L

def b_n(n):
    aofn = spi.quad(lambda x: f(x) * np.sin(n * np.pi * x / L), -L, L)
    return aofn[0] / L

def series(x, N):
    frst = a_n(0)
    for n in range(1, N + 1):
        frst += a_n(n) * np.cos(np.pi * n * x / L) + b_n(n) * np.sin(np.pi * n * x / L)
    return frst

values = np.linspace(-L, L, 10000)
plt.plot(values, f(values), label='Original Function')
plt.plot(values, series(values, int(n)), label=f'Fourier Series - {int(n)} terms')
plt.legend()
plt.show()
