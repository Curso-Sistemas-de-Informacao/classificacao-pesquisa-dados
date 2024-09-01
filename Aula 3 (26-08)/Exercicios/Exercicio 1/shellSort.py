def gapInsertionSort(lista,start,gap):
    for i in range(start+gap,len(lista),gap):
        currentvalue = lista[i] #
        position = i 

        while position>=gap and lista[position-gap]>currentvalue:
            lista[position]=lista[position-gap]
            position = position-gap

        lista[position] = currentvalue

def shellSort(lista):
    sublistcount = len(lista)//2
    while sublistcount > 0:
    
        for startposition in range(sublistcount):
            gapInsertionSort(lista,startposition,sublistcount)
        print("After increments of size" ,sublistcount, "The list is" ,lista)
        
        sublistcount = sublistcount // 2


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20, 34]
shellSort(lista)