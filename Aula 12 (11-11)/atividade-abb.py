class Node:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.esquerda = None
        self.direita = None
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

class arvore_binaria:

    def __init__(self):
        self.raiz = None

    def insert(self, id, nome, descricao, preco):
        if self.raiz is None:
            self.raiz = Node(id, nome, descricao, preco)
        else:
            atual = self.raiz
            while True:
                if id < atual.id:
                    if atual.esquerda is None:
                        atual.esquerda = Node(id, nome, descricao, preco)
                        break
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = Node(id, nome, descricao, preco)
                        break
                    atual = atual.direita

    def remove(self, id):
        self.raiz = self._remove(self.raiz, id)

    def _remove(self, node, id):
        if node is None:
            return node

        if id < node.id:
            node.esquerda = self._remove(node.esquerda, id)
        elif id > node.id:
            node.direita = self._remove(node.direita, id)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda

            temp = node.esquerda
            while temp.direita:
                temp = temp.direita
            node.id = temp.id
            node.esquerda = self._remove(node.esquerda, temp.id)
        
        return node
    
    def search(self, id):
        atual = self.raiz
        while atual:
            if id == atual.id:
                return atual
            elif id < atual.id:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def ordem_simetrica(self, node):
        if node:
            self.ordem_simetrica(node.esquerda)
            print(f"id: {node.id}, Nome: {node.nome}, Descrição: {node.descricao}, Preço: {node.preco}")
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