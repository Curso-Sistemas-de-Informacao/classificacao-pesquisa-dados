import math

def pesquisa_por_salto(lista, chave):
    n = len(lista)
    bloco = int(math.sqrt(n)) 
    atual = 0

    while atual < n and lista[atual] < chave:
        atual += bloco

    for i in range(max(0, atual - bloco), min(n, atual)):
        if lista[i] == chave:
            return i  
    return print("não achou a chave")

lista = [0, 1, 2, 4, 5, 6, 7, 8, 9]
chave = 7

print(pesquisa_por_salto(lista, chave))