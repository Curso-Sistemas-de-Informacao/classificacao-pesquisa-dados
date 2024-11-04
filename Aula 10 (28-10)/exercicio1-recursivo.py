def busca_binaria_recursiva(lista, chave, inicio=0, fim=None):
    if fim == None:
        fim = len(lista) - 1

    if inicio > fim:
        return print("não achou a chave") 

    meio = (inicio + fim) // 2

    if lista[meio] == chave:
        return print("achou a chave") 
    
    elif lista[meio] < chave:
        return busca_binaria_recursiva(lista, chave, meio + 1, fim) 
    else:
        return busca_binaria_recursiva(lista, chave, inicio, meio - 1) 
    
lista = [0, 1, 2, 4, 5, 6, 7, 8, 9]
chave = 7

busca_binaria_recursiva(lista, chave)