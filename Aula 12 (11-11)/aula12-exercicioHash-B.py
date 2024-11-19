class Node:
    def __init__(self, key, valor):
        self.key = key
        self.valor = valor
        self.proximo = None


class HashTable:
    def __init__(self, tam):
        self.tam = tam
        self.tabela = [None] * tam

    def funcao_hash(self, key):
        return key % self.tam

    def insert(self, key, valor):
        index = self.funcao_hash(key)
        novo_no = Node(key, valor)

        if self.tabela[index] is None:
            self.tabela[index] = novo_no
        else:
            atual = self.tabela[index]
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def imprimir(self):
        for i in range(self.tam):
            print(f"Index {i}: ", end="")
            atual = self.tabela[i]
            while atual is not None:
                print(f"({atual.key}, {atual.valor})", end=" -> ")
                atual = atual.proximo
            print("None")



hash_table = HashTable(5)
hash_table.insert(9, "Ronaldo")
hash_table.insert(10, "Pele")
hash_table.insert(10, "Messi")
hash_table.insert(7, "Cristiano Ronaldo")
hash_table.insert(11, "Romario")
hash_table.insert(11, "Neymar")

hash_table.imprimir()
