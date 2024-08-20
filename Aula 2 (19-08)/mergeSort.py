
def merge_sort(lista, inicio, meio, fim):
    fim1 = 0
    fim2 = 0
    tamanho = fim - inicio + 1
    p1 = inicio
    p2 = meio + 1
    temp = []

    for i in range(tamanho):
        if not fim1 and not fim2:
            if lista[p1] < lista[p2]:
                temp.append(lista[p1])
                p1 += 1
            else:
                temp.append(lista[p2])
                p2 += 1

            if p1 > meio:
                fim1 = 1

            if p2 > fim:
                fim2 = 1
        else:
            if not fim1:
                temp.append(lista[p1])
                p1 += 1
            else:
                temp.append(lista[p2])
                p2 += 1

    for j in range(tamanho):
        lista[inicio + j] = temp[j]

    print(lista)


lista = [3, 5, 7, 8, 3, 4, 10, 15, 21]
merge_sort(lista, 0, 3, len(lista) - 1)