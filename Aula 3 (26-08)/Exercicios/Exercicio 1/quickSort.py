

def particiona(lista, inicio, final):
    aux = 0
    esquerda = inicio
    direita = final
    pivo = lista[final]

    while(esquerda < direita):
        while(esquerda <= final and lista[esquerda] <= pivo):
            esquerda += 1
        
        while(direita >= 0 and lista[direita] > pivo):
            direita -= 1
        
        if esquerda < direita:
            aux = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = aux

    lista[inicio] = lista[direita]
    lista[direita] = pivo
    return direita


def quickSort(lista, inicio, fim):
    pivo = 0
    if fim > inicio:
        pivo = particiona(lista, inicio, fim)
        quickSort(lista, inicio, pivo - 1)
        quickSort(lista, pivo + 1, fim)


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20, 34]
quickSort(lista, 0, len(lista) - 1)
print("Lista ordenada: ", lista)