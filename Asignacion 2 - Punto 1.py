def comprobarValorIndice(vector, indice):
    if indice >= len(vector):
        return False
    elif vector[indice] == indice:
        return True
    else:
        return comprobarValorIndice(vector, indice+1)

vector = [6, 5, 4, 3]
indice = 0

print(comprobarValorIndice(vector, indice))