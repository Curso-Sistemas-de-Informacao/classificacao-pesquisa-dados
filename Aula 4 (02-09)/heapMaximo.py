
def maxHeapfy(lista, i, n):
    maior = i
    l = 2*i+1
    r = 2*i+2
    if l < n and lista[l] > lista[i]:
        maior = l
        
    if r < n and lista[r] > lista[maior]:
        maior = r

    if maior != i:
        temp = lista[i]
        lista[i] = lista[maior]
        lista[maior] = temp
        maxHeapfy(lista, maior, n)

def heapSort(lista):
    for k in range(len(lista)//2-1, -1, -1):
        maxHeapfy(lista, k, len(lista))

    for n in range(len(lista)-1, 0, -1):
        temp = lista[0]
        lista[0] = lista[n]
        lista[n] = temp
        maxHeapfy(lista, 0, n)


lista = [7, 10, 4, 3, 20, 15]

heapSort(lista)

print(lista)