numeroEntero = int(input("Ingrese el numero entero: "))

def superDigito(numeroEntero):
    if numeroEntero < 10:
        return numeroEntero
    else:
        digitos = [int(digito) for digito in str(numeroEntero)]
        sumaDigitos = sum(digitos)
        return superDigito(sumaDigitos)

print("El super digito del numero", numeroEntero, "es:", superDigito(numeroEntero))