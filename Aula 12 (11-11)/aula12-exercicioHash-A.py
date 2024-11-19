
class HashTable:

    def __init__(self, tam):
        self.tam = tam
        self.tabela = [None] * tam

    def funcao_hash(self, key):
        return key % self.tam
    
    def insert(self, key, valor):
        index = self.funcao_hash(key)
        self.tabela[index].append(valor) 
    
    def imprimir(self):

        for key, valores in self.tabela.items():
            print(f"Index {key}: {valores}")


hash_table = HashTable(5)
hash_table.insert(9, "Ronaldo")
hash_table.insert(10, "Pele")
hash_table.insert(10, "Messi")
hash_table.insert(7, "Cristiano Ronaldo")
hash_table.insert(11, "Romario")
hash_table.insert(11, "Neymar")

hash_table.imprimir()

