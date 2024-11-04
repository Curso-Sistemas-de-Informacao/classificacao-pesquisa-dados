import random
# from exercicio3-codigo import busca_binaria_contador, pesquisa_por_salto_contador

# Lista ordenada de 10.000 elementos
arr = list(range(10000))

valores_teste = [10, 5000, 9990, 10001]
resultados_binaria = []
resultados_salto = []

# Executando o teste de comparações para cada valor
for valor in valores_teste:
    comparacoes_binaria = busca_binaria_contador(arr, valor)
    comparacoes_salto = pesquisa_por_salto_contador(arr, valor)
    
    resultados_binaria.append(comparacoes_binaria)
    resultados_salto.append(comparacoes_salto)

print("Resultados da Busca Binária (comparações):", resultados_binaria)
print("Resultados da Pesquisa por Salto (comparações):", resultados_salto)
