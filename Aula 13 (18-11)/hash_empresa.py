class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __str__(self):
        return f"Nome: {self.nome}, Caminho: {self.caminho}, Tamanho: {self.tamanho} KB"


class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        
        return sum(ord(c) for c in chave) % self.tamanho

    def adicionar(self, arquivo):
        indice = self._funcao_hash(arquivo.nome)
        for item in self.tabela[indice]:
            if item.nome == arquivo.nome:
                print(f"Erro: O arquivo '{arquivo.nome}' já existe.")
                return
        self.tabela[indice].append(arquivo)
        print(f"Arquivo '{arquivo.nome}' adicionado com sucesso.")

    def buscar(self, nome):
        indice = self._funcao_hash(nome)
        for arquivo in self.tabela[indice]:
            if arquivo.nome == nome:
                return arquivo
        print(f"Arquivo '{nome}' não encontrado.")
        return None

    def remover(self, nome):
        indice = self._funcao_hash(nome)
        for i, arquivo in enumerate(self.tabela[indice]):
            if arquivo.nome == nome:
                del self.tabela[indice][i]
                print(f"Arquivo '{nome}' removido com sucesso.")
                return
        print(f"Arquivo '{nome}' não encontrado para remoção.")

    def listar(self):
        print("Arquivos armazenados:")
        for i, lista in enumerate(self.tabela):
            if lista:
                print(f"Índice {i}:")
                for arquivo in lista:
                    print(f"  {arquivo}")
        print("Fim da lista.")


tabela = TabelaHash()

tabela.adicionar(Arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 1024))
tabela.adicionar(Arquivo("foto.jpg", "/imagens/foto.jpg", 2048))
tabela.adicionar(Arquivo("dados.csv", "/planilhas/dados.csv", 512))
tabela.adicionar(Arquivo("backup.zip", "/backup/backup.zip", 4096))

arquivo = tabela.buscar("dados.csv")
if arquivo:
    print("Arquivo encontrado:", arquivo)

tabela.remover("foto.jpg")

tabela.listar()
