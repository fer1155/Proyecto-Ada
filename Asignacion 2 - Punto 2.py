def calcFormas(X, N, num=1):
  #Se valida si las restricciones se cumplen, en dado caso que no se retorna 0 
  if X < 0 or X > 1000 or N < 2 or N > 10:
      return 0
  #Si X es igual a 0, encontramos una combinación válida
  if X == 0:
      return 1
  #Si num^N es mayor que X, no hay necesidad de continuar
  if num ** N > X:
      return 0
  #Llamada recursiva 
  return calcFormas(X - num ** N, N, num + 1) + calcFormas(X, N, num + 1)

X = 13
N = 2
print("El número de formas es:", calcFormas(X, N))