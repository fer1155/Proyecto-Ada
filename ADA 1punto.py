import timeit
import matplotlib.pyplot as plt

# Definir array con los valores asociados de n
n = [3, 5, 7, 10]

# Definir funcion recursiva de fibonacci
def fibRecursivo(n):
    if n <= 1:
        return n
    else:
        return fibRecursivo(n-1) + fibRecursivo(n-2)

# Definir funcion iterativa de fibonacci
def fibList(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

# Definir arrays donde se guardaran los tiempos de ejecucion de cada funcion
tiemposFibRecursivo = []
tiemposFibList= []

print("Ejecutandose la funcion recursiva...")
for i in n:
    tiempoTranscurridoFibRecursivo = timeit.timeit(lambda:fibRecursivo(i), number=10)
    tiemposFibRecursivo.append(tiempoTranscurridoFibRecursivo)
    print("Cuando n toma valor de ", i)
    print("La función tarda", tiempoTranscurridoFibRecursivo, "segundos en ejecutarse.")

print(" ")
print("Ejecutandose la funcion iterativa...")
for i in n:
    tiempoTranscurridoFibList = timeit.timeit(lambda:fibList(i), number=10)
    tiemposFibList.append(tiempoTranscurridoFibList)
    print("Cuando n toma valor de ", i)
    print("La función tarda", tiempoTranscurridoFibList, "segundos en ejecutarse.")

# Tamaño específico de la grafica
plt.figure(figsize=(8, 6))

# Graficar los datos
plt.plot(n, tiemposFibRecursivo, label='Tiempos funcion - Recursiva -')
plt.plot(n, tiemposFibList, label='Tiempos funcion - Iterativa -')

# Añadir etiquetas de ejes y título
plt.xlabel('n')
plt.ylabel('T(n)')
plt.title('Tiempo de ejecucion Serie de Fibonacci')

# Añadir leyenda
plt.legend()

# Mostrar gráfico
plt.show()