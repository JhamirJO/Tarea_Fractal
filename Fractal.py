import matplotlib.pyplot as plt
import numpy as np

#define una función llamada "mandelbrot" que toma un número complejo c como entrada.
def mandelbrot(c):
    z = 0 #inicializa una variable z a cero.
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

#Se crea un arreglo numpy de 500 puntos igualmente espaciados en el rango [-2, 2] para los valores x e y.
x = y = np.linspace(-2, 2, 500)

#utiliza la función meshgrid para crear matrices X e Y para los valores de x e y respectivamente.
X, Y = np.meshgrid(x, y)
#crea un conjunto de números complejos Z utilizando las matrices X e Y y la constante compleja 1j.
Z = X + Y*1j
img = plt.imshow([[mandelbrot(c) for c in row] for row in Z], cmap='Blues', extent=[-2, 2, -2, 2])
plt.show()
