
def select_sort(lista):
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

    print(lista)
            


# lista = [1, 2, 3, 4, 5] # lista ordenada
# lista = [5, 4, 3, 2, 1] # lista inversa
# lista = [2, 2, 4, 5, 1, 1, 3] # lista com itens duplicados
lista = [3, 2, 1, 4, 5] # lista com itens aleatórios sem repetição
select_sort(lista)