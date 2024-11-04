
def busca_iterativa(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] < chave:
            inicio = meio + 1

        elif lista[meio] > chave:
            fim = meio - 1

        else:
            print("achou a chave")
            break

    print("Não achou a chave")


lista = [0, 1, 2, 4, 5, 6, 7, 8, 9]
chave = 4

busca_iterativa(lista, chave)