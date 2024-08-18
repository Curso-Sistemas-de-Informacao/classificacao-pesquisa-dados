class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
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

    def inserir_ordenado(self):
        lista_ordenada = None
        atual = self.primeiro

        while atual is not None:
            proximo_node = atual.proximo
            lista_ordenada = self.inserir_posicao(lista_ordenada, atual)
            atual = proximo_node
        self.primeiro = lista_ordenada

    def inserir_posicao(self, lista_ordenada, novo_node):
        if not lista_ordenada or lista_ordenada.valor >= novo_node.valor:
            novo_node.proximo = lista_ordenada
            lista_ordenada = novo_node
        else:
            atual = lista_ordenada
            while atual.proximo and atual.proximo.valor < novo_node.valor:
                atual = atual.proximo
            novo_node.proximo = atual.proximo
            atual.proximo = novo_node
        return lista_ordenada

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


lista = ListaEncadeada()

# Tirar os comentários do teste que quer fazer

# Lista ordenada

# lista.adicionar(1)
# lista.adicionar(2)
# lista.adicionar(3)
# lista.adicionar(4)
# lista.adicionar(5)

# ----------------------

# Lista inversa

lista.adicionar(5)
lista.adicionar(4)
lista.adicionar(3)
lista.adicionar(2)
lista.adicionar(1)

# ----------------------

# Lista com itens duplicados

# lista.adicionar(3)
# lista.adicionar(3)
# lista.adicionar(1)
# lista.adicionar(5)
# lista.adicionar(2)
# lista.adicionar(4)
# lista.adicionar(4)

# ----------------------

# lista com itens aleatorios sem repetição

# lista.adicionar(2)
# lista.adicionar(5)
# lista.adicionar(3)
# lista.adicionar(4)
# lista.adicionar(1)

lista.inserir_ordenado()
lista.imprimir()
