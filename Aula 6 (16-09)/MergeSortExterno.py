import os
import heapq

BLOCOS_TAMANHO = 100

def dividir_arquivo(arquivo, tamanho_bloco):
    arquivos_temporarios = []
    with open(arquivo, 'r') as f:
        while True:
            linhas = f.readlines(tamanho_bloco)
            if not linhas:
                break
            linhas.sort() 
            arquivo_temp = f'temp_{len(arquivos_temporarios)}.txt'
            with open(arquivo_temp, 'w') as temp_file:
                temp_file.writelines(linhas)
            arquivos_temporarios.append(arquivo_temp)
    return arquivos_temporarios

def mesclar_arquivos(arquivos, arquivo_saida):
    heap = []
    arquivos_abertos = [open(arquivo, 'r') for arquivo in arquivos]
    
    for i, arquivo in enumerate(arquivos_abertos):
        linha = arquivo.readline()
        if linha:
            heapq.heappush(heap, (linha, i))
    
    with open(arquivo_saida, 'w') as f_out:
        while heap:
            menor, i = heapq.heappop(heap)
            f_out.write(menor)
            linha = arquivos_abertos[i].readline()
            if linha:
                heapq.heappush(heap, (linha, i))
    
    for arquivo in arquivos_abertos:
        arquivo.close()

def external_merge_sort(arquivo, arquivo_saida):
    arquivos_temporarios = dividir_arquivo(arquivo, BLOCOS_TAMANHO)
    
    mesclar_arquivos(arquivos_temporarios, arquivo_saida)

    for arquivo_temp in arquivos_temporarios:
        os.remove(arquivo_temp)

arquivo_entrada = 'teste.txt'
arquivo_saida = 'arquivo_teste_ordenado.txt'
external_merge_sort(arquivo_entrada, arquivo_saida)
