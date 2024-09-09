# tentei implementar o código do vídeo do classroom, mas não tava funcionando

def counting_sort(lista):
    n = len(lista)
    maximo = max(lista)

    contagem = [0] * (maximo + 1) 

    for i in range(0, n):
        contagem[lista[i]] += 1

    index = 0
    for i in range(0, maximo + 1):
        while contagem[i] > 0:
            lista[index] = i
            index += 1
            contagem[i] -= 1

lista = [10, 8, 8, 75, 2, 6, 4, 4, 2]
counting_sort(lista)
print(lista)
