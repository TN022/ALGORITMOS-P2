numeros = [7, 2, 4, 1, 8, 5, 3]

print("Lista original:", numeros)

tamanho = len(numeros)
for i in range(tamanho - 1):
    indice_minimo = i
    for j in range(i + 1, tamanho):
        if numeros[j] < numeros[indice_minimo]:
            indice_minimo = j
    numeros[i], numeros[indice_minimo] = numeros[indice_minimo], numeros[i]

print("Lista ordenada com Selection Sort:", numeros)
