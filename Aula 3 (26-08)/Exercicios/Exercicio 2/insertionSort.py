import time

def insertionSort(lista):
    tempo_inicio = time.perf_counter()
    for j in range(1, len(lista)):
        i = j-1
        tmp = lista[j]

        while((i>=0) and (tmp < lista[i])):
            lista[i+1] = lista[i]
            i-=1

        lista[i+1] = tmp
    
    tempo_fim = time.perf_counter()
    print(f"Tempo de execução do insertion sort: {tempo_fim - tempo_inicio:.10f} segundos")
    print("Lista ordenada com insertion sort", lista)
    print("_____________________")


lista = [1, 2, 3, 4, 5] # lista ordenada, no caso, não irá alterar nada
#lista = [5, 4, 3, 2, 1] # lista inversa
#lista = [5, 5, 4, 3, 2, 2, 1] # lista com itens duplicados
#lista = [2, 6, 1, 9, 0] # lista com itens aleatorios sem repetição

insertionSort(lista)