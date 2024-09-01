import time

def bubble_sort(lista):
    tempo_inicio = time.perf_counter()

    for j in range(len(lista)):
        for i in range(j+1, len(lista)):
            if lista[i] < lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    
    tempo_fim = time.perf_counter()
    print(f"Tempo de execução do bubble sort: {tempo_fim - tempo_inicio:.10f} segundos")
    print("Lista ordenada com bubble sort", lista)
    print("_____________________")

[19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

#lista = [1, 2, 3, 4, 5] # lista ordenada
lista = [5, 4, 3, 2, 1] # lista inversa
#lista = [5, 5, 4, 3, 2, 2, 1] # lista com itens duplicados
#lista = [2, 6, 1, 9, 0] # lista com itens aleatorios sem repetição

bubble_sort(lista)