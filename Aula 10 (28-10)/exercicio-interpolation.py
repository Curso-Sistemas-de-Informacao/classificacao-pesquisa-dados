

def pesquisa_interpolation(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    n = len(lista)

    while inicio <= fim:
        meio = inicio + int((fim - inicio) * (chave - lista[inicio]) / (lista[fim] - lista[inicio]))

        if lista[meio] < chave:
            inicio = meio + 1

        elif lista[meio] > chave:
            fim = meio - 1

        else:
            print("achou a chave")
            break

    print("Não achou a chave")



lista = [2, 4, 6, 8, 10, 12, 14, 16]
chave = 4


