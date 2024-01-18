import random

def ordenar_pares(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    numeros_pares_ordenados = sorted(numeros_pares)
    return numeros_pares_ordenados

lista_desordenada = random.sample(range(1, 100), 30)

print("Lista original desordenada:", lista_desordenada)

numeros_pares_ordenados = ordenar_pares(lista_desordenada)
print("Números pares ordenados:", numeros_pares_ordenados)
