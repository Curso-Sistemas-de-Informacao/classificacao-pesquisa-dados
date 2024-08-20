
def bubble_sort(lista):

    for j in range(len(lista)):
        for i in range(j+1, len(lista)):
            if lista[i] < lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    
    print(lista)

#lista = [1, 2, 3, 4, 5] # lista ordenada
lista = [5, 4, 3, 2, 1] # lista inversa
#lista = [5, 5, 4, 3, 2, 2, 1] # lista com itens duplicados
#lista = [2, 6, 1, 9, 0] # lista com itens aleatorios sem repetição

bubble_sort(lista)