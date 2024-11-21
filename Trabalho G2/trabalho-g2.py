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
        atual = self.raiz
        while atual:
            if atual.preco == preco:
                return atual
            elif atual.preco < preco:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):

        def achar_jogos_faixa(node, jogos):
            if node == None:
                return
            
            if preco_minimo <= node.preco <= preco_maximo:
                jogos.append(node)

            achar_jogos_faixa(node.esquerda, jogos)
            achar_jogos_faixa(node.direita, jogos)

        jogos_achados = []
        achar_jogos_faixa(self.raiz, jogos_achados)
        return jogos_achados
    

arvore_jogos = ArvoreJogos()
arvore_jogos.inserir(1, "Red Dead Redemption 2", "Rockstar Games", 250, "Aventura")
arvore_jogos.inserir(2, "Call of Duty: Black Ops 2", "Activision", 350, "Tiro")
arvore_jogos.inserir(3, "Gta V", "Rockstar Games", 200, "Ação")
arvore_jogos.inserir(4, "BloodBorne", "From Software", 100, "RPG")


procurar_jogo_preco = arvore_jogos.buscar_por_preco(250)

if procurar_jogo_preco:
    print(f"Jogo encontrado: {procurar_jogo_preco.titulo}")
else:
    print("Jogo não encontrado.")

print("######################")

jogos_faixa_preco = arvore_jogos.busca_por_faixa_preco(100, 200)

for jogo in jogos_faixa_preco:
    print(f"Jogo: {jogo.titulo} | Preço: {jogo.preco}")

    



