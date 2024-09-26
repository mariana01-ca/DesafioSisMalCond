import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x1
x1 = np.linspace(-1, 3, 100)

# Fijar x3 = 1
x3 = 1

# Primera ecuación: 1*x1 + 1.7*x2 + 1*x3 = b1
b1 = 2  # Supongamos b1 = 2
x2_1 = (b1 - 1*x1 - 1*x3) / 1.7

# Segunda ecuación: 67.5*x1 + 1.99*x2 + 1.92*x3 = b2
b2 = 4  # Supongamos b2 = 4
x2_2 = (b2 - 67.5*x1 - 1.92*x3) / 1.99

# Tercera ecuación: 67.6*x1 + 2.01*x2 + 1.93*x3 = b3
b3 = 6  # Supongamos b3 = 6
x2_3 = (b3 - 67.6*x1 - 1.93*x3) / 2.01

# Graficar las tres rectas
plt.plot(x1, x2_1, label='Ecuación 1: 1*x1 + 1.7*x2 + 1*x3 = 2')
plt.plot(x1, x2_2, label='Ecuación 2: 67.5*x1 + 1.99*x2 + 1.92*x3 = 4')
plt.plot(x1, x2_3, label='Ecuación 3: 67.6*x1 + 2.01*x2 + 1.93*x3 = 6')

# Añadir etiquetas y leyenda
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.grid(True)
plt.title('Gráfico del sistema de ecuaciones')

# Mostrar la gráfica
plt.show()
