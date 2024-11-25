class NoJogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, genero):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.genero = genero
        self.esquerda = None
        self.direita = None

class ArvoreJogos:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo_id, titulo, desenvolvedor, preco, genero):
        if self.raiz == None:
            self.raiz = NoJogo(jogo_id, titulo, desenvolvedor, preco, genero)
        else:
            atual = self.raiz
            while True:
                if preco < atual.preco: 
                    if atual.esquerda == None:
                        atual.esquerda = NoJogo(jogo_id, titulo, desenvolvedor, preco, genero)
                        break
                    atual = atual.esquerda
                else:
                    if atual.direita == None:
                        atual.direita = NoJogo(jogo_id, titulo, desenvolvedor, preco, genero)
                        break
                    atual = atual.direita


    def buscar_por_preco(self, preco):

        def encontrar_jogos_preco(node, preco, jogos):
            if node == None: 
                return

            if node.preco == preco:
                jogos.append(node)

            encontrar_jogos_preco(node.esquerda, preco, jogos)
            encontrar_jogos_preco(node.direita, preco, jogos)

        jogos_achados = []
        encontrar_jogos_preco(self.raiz, preco, jogos_achados)
        return jogos_achados

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):

        def achar_jogos_faixa(node, jogos):
            if node == None: # tive que colocar isso pq chegava em um ponto que o valor era nulo, aí dava erro
                return
            
            if preco_minimo <= node.preco <= preco_maximo:
                jogos.append(node)

            achar_jogos_faixa(node.esquerda, jogos)
            achar_jogos_faixa(node.direita, jogos)

        jogos_achados = []
        achar_jogos_faixa(self.raiz, jogos_achados)
        return jogos_achados
    

class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.genero: 
            genero_hash = hash(genero) 
            if genero_hash not in self.genero_para_jogos:
                self.genero_para_jogos[genero_hash] = []
            self.genero_para_jogos[genero_hash].append(jogo)

    def buscar_por_genero(self, genero):
        genero_hash = hash(genero) 
        return self.genero_para_jogos.get(genero_hash, [])

class MotorBuscaJogos:
    def __init__(self):
        self.arvore_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def inserir_jogo(self, jogo_id, titulo, desenvolvedor, preco, genero):
        novo_jogo = NoJogo(jogo_id, titulo, desenvolvedor, preco, genero)
        self.arvore_jogos.inserir(jogo_id, titulo, desenvolvedor, preco, genero)
        self.generos.adicionar_jogo(novo_jogo)

    def buscar_jogos_por_preco(self, preco):
        return self.arvore_jogos.buscar_por_preco(preco)

    def buscar_jogos_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self.arvore_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)
    
    def buscar_por_genero(self, genero):
        return self.generos.buscar_por_genero(genero)
    

loja_jogos = MotorBuscaJogos()
loja_jogos.inserir_jogo(1, "Red Dead Redemption 2", "Rockstar Games", 250, ["Aventura", "Ação"])
loja_jogos.inserir_jogo(2, "Call of Duty: Black Ops 2", "Activision", 250, ["Tiro", "Ação"])
loja_jogos.inserir_jogo(3, "Fifa", "EA games", 200, ["Esportes"])
loja_jogos.inserir_jogo(4, "BloodBorne", "From Software", 100, ["RPG", "Aventura"])
loja_jogos.inserir_jogo(5, "The Last of Us", "Naughty Dog", 180, ["Aventura", "Ação"])
loja_jogos.inserir_jogo(6, "Fallout: New Vegas", "Obsidian Entertainment", 170, ["RPG"])



print("Jogos com um preço específico: ")
procurar_jogo_preco = loja_jogos.buscar_jogos_por_preco(250)

for jogo in procurar_jogo_preco:
    print(f"jogo: {jogo.titulo} | preço: {jogo.preco}")


print("######################")

print("Jogos com uma faixa de preço: ")
jogos_faixa_preco = loja_jogos.buscar_jogos_por_faixa_preco(100, 200)

for jogo in jogos_faixa_preco: # como ali na linha 117 ele retona uma lista, aqui eu vou percorrer ela pra mostrar os jogos achados, a mesma coisa no buscar por preço e por gênero
    print(f"jogo: {jogo.titulo} | preço: {jogo.preco}")


print("######################")

print("Jogos por gênero: ")
jogos_genero = loja_jogos.buscar_por_genero("Aventura")

for jogo in jogos_genero:
    print(f"jogo: {jogo.titulo} | gênero: {jogo.genero}")


print("######################")

print("Jogos organizados por gênero (conteúdo do dicionário):")
for genero_hash, jogos in loja_jogos.generos.genero_para_jogos.items():
    print(f"Gênero Hash: {genero_hash}")
    for jogo in jogos:
        print(f"  - Jogo: {jogo.titulo} | Gêneros: {jogo.genero}")
