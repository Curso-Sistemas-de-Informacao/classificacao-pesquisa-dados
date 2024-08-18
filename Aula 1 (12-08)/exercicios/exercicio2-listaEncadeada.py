
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class lista_encadeada:
    def __init__(self):
        self.primeiro = None
    
    def adicionar(self, valor):
        novo_node = Node(valor)
        if self.primeiro is None:
            self.primeiro = novo_node
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_node
    
    def ordenar(self):
        inicio = self.primeiro # aqui a ideia é que "inicio" seja o valor no topo da lista, não achei nome melhor de variável 
        while inicio is not None:
            menor_valor = inicio
            atual = inicio.proximo
            while atual is not None:
                if atual.valor < menor_valor.valor:
                    menor_valor = atual
                atual = atual.proximo

            aux = inicio.valor
            inicio.valor = menor_valor.valor
            menor_valor.valor = aux

            inicio = inicio.proximo
    
    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


lista = lista_encadeada()


# Tirar os comentários do teste que quer fazer

# Lista ordenada

# lista.adicionar(1)
# lista.adicionar(2)
# lista.adicionar(3)
# lista.adicionar(4)
# lista.adicionar(5)

# -----------------------

# Lista inversa

# lista.adicionar(5)
# lista.adicionar(4)
# lista.adicionar(3)
# lista.adicionar(2)
# lista.adicionar(1)

# -----------------------

# Lista com itens duplicados

lista.adicionar(3)
lista.adicionar(3)
lista.adicionar(1)
lista.adicionar(5)
lista.adicionar(2)
lista.adicionar(4)
lista.adicionar(4)

# -----------------------

# lista com itens aleatorios sem repetição

# lista.adicionar(2)
# lista.adicionar(5)
# lista.adicionar(3)
# lista.adicionar(4)
# lista.adicionar(1)

lista.ordenar()
lista.imprimir()
