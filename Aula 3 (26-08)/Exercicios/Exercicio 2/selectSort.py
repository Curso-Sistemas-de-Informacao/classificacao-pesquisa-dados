import time

def select_sort(lista):
    tempo_inicio = time.perf_counter()
    for i in range(len(lista)-1):
        menor_id = i
        menor = lista[i]
        for j in range(i+1, len(lista)):
            if(lista[j] < menor):
                menor = lista[j]
                menor_id = j
            
        troca = lista[i]
        lista[i] = lista[menor_id]
        lista[menor_id] = troca

    tempo_fim = time.perf_counter()
    print(f"Tempo de execução do select sort: {tempo_fim - tempo_inicio:.10f} segundos")
    print("Lista ordenada com select_sort", lista)
    print("_____________________")       


lista = [1, 2, 3, 4, 5] # lista ordenada
# lista = [5, 4, 3, 2, 1] # lista inversa
# lista = [2, 2, 4, 5, 1, 1, 3] # lista com itens duplicados
#lista = [3, 2, 1, 4, 5] # lista com itens aleatórios sem repetição
select_sort(lista)