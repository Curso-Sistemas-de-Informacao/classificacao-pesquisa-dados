# professor, aqui eu tentei me basear no pdf da aula, mas não deu certo, então tive q recorrer a chatgpt, mas mais pra ele corrigir o código do que
# para ele fazer tudo, no pdf por exemplo não mostrava a parte de recursividade, aí foi uma das coisas q o chatgpt sugeriu

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class arvore_binaria:

    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            atual = self.raiz
            while True:
                if valor < atual.valor:
                    if atual.esquerda is None:
                        atual.esquerda = Node(valor)
                        break
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = Node(valor)
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

    
    def pre_ordem(self, node):
        if node:
            print(node.valor, end=" ")
            self.pre_ordem(node.esquerda)
            self.pre_ordem(node.direita)

    def pos_ordem(self, node):
        if node:
            self.pos_ordem(node.esquerda)
            self.pos_ordem(node.direita)
            print(node.valor, end=" ")

    def ordem_simetrica(self, node):
        if node:
            self.ordem_simetrica(node.esquerda)
            print(node.valor, end=" ")
            self.ordem_simetrica(node.direita)



arvore = arvore_binaria()
arvore.insert(9)
arvore.insert(2)
arvore.insert(5)
arvore.insert(6)
arvore.insert(7)
arvore.insert(1)
arvore.insert(8)

arvore.remove(9)

achar_numero = arvore.search(5)

if achar_numero:  # aqui eu coloquei uma mini lógica para retornar uma mensagem se o valor foi encontrado ou não
    print("encontrou")
else:
    print("não encontrou")

print("pos ordem: ")
arvore.pos_ordem(arvore.raiz)

print("\npos ordem: ")
arvore.pre_ordem(arvore.raiz)


print("\nordem simetrica: ") 
arvore.ordem_simetrica(arvore.raiz)




