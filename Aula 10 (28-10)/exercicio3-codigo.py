import math

def busca_binaria_contador(arr, alvo):
    inicio, fim = 0, len(arr) - 1
    comparacoes = 0
    
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if arr[meio] == alvo:
            return comparacoes 
        elif arr[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return comparacoes 

def pesquisa_por_salto_contador(arr, alvo):
    n = len(arr)
    bloco = int(math.sqrt(n))
    atual = 0
    comparacoes = 0

    while atual < n and arr[min(atual, n - 1)] < alvo:
        comparacoes += 1
        atual += bloco

    for i in range(max(0, atual - bloco), min(n, atual)):
        comparacoes += 1
        if arr[i] == alvo:
            return comparacoes 
    
    return comparacoes
