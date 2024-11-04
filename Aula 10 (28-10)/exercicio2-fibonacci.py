def pesquisa_fibonacci(lista, chave):
    n = len(lista)

    fib_m2 = 0 
    fib_m1 = 1 
    fib_m = fib_m2 + fib_m1 

    while fib_m < n:
        fib_m2, fib_m1 = fib_m1, fib_m
        fib_m = fib_m2 + fib_m

    offset = -1 

    while fib_m > 1:

        i = min(offset + fib_m2, n - 1)

        if lista[i] < chave:
            fib_m, fib_m1, fib_m2 = fib_m1, fib_m2, fib_m - fib_m1
            offset = i
        elif lista[i] > chave:
            fib_m, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m - fib_m1
        else:
            return i 

    if fib_m1 and lista[offset + 1] == chave:
        return offset + 1
    return -1  

lista = [0, 1, 2, 4, 5, 6, 7, 8, 9]
chave = 7

pesquisa_fibonacci(lista, chave)
