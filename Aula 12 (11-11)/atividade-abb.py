class Node:
    def __init__(self, valor, nome, descricao, preco):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

class arvore_binaria:

    def __init__(self):
        self.raiz = None

    def insert(self, valor, nome, descricao, preco):
        if self.raiz is None:
            self.raiz = Node(valor, nome, descricao, preco)
        else:
            atual = self.raiz
            while True:
                if valor < atual.valor:
                    if atual.esquerda is None:
                        atual.esquerda = Node(valor, nome, descricao, preco)
                        break
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = Node(valor, nome, descricao, preco)
                        break
                    atual = atual.direita

    def remove(self, valor):
        self.raiz = self._remove(self.raiz, valor)

    def _remove(self, node, valor):
        if node is None:
            return node

        if valor < node.valor:
            node.esquerda = self._remove(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._remove(node.direita, valor)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda

            temp = node.esquerda
            while temp.direita:
                temp = temp.direita
            node.valor = temp.valor
            node.esquerda = self._remove(node.esquerda, temp.valor)
        
        return node
    
    def search(self, valor):
        atual = self.raiz
        while atual:
            if valor == atual.valor:
                return atual
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def ordem_simetrica(self, node):
        if node:
            self.ordem_simetrica(node.esquerda)
            print(f"Valor: {node.valor}, Nome: {node.nome}, Descrição: {node.descricao}, Preço: {node.preco}")
            self.ordem_simetrica(node.direita)


arvore = arvore_binaria()
arvore.insert(30, "produto x", "descricao do produto x", 80)
arvore.insert(20, "produto y", "descricao do produto y", 120)
arvore.insert(40, "produto z", "descricao do produto z", 50)

achar_numero = arvore.search(30)

if achar_numero: 
    print("encontrou")
else:
    print("não encontrou")


print("Produtos em ordem crescente:")
arvore.ordem_simetrica(arvore.raiz)

arvore.remove(40)