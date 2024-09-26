import numpy as np

A3 = np.array([[1, 1.7, 1],
               [67.5, 1.99, 1.92],
               [67.6, 2.01, 1.93]])
B=np.array([[2,
             4,
             6]])
# Calcular el determinante
det_A3 = np.linalg.det(A3)
print("Determinante de A3:", det_A3)
# Calcular la inversa de A
a_inv = np.linalg.inv(A3)
# Multiplicar A por su inversa
result = np.dot(A3, a_inv)
# Mostrar el resultado
print("Inversa: ")
print(result)

# Calcular el número de condición usando la norma 2
cond_A3 = np.linalg.cond(A3)

# Mostrar el número de condición
print("Número de condición de A3:")
print(cond_A3)