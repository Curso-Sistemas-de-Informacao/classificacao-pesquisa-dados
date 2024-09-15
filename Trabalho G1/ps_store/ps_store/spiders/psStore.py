import scrapy

class PsstoreSpider(scrapy.Spider):
    name = "psStore"
    allowed_domains = ["store.playstation.com"]
    start_urls = ["https://store.playstation.com/pt-br/category/8a31d28e-61a4-4794-9286-24f7944b7c5c/1"]

    def parse(self, response):
        jogos = response.css('span.psw-t-body::text').getall() 
        precos = response.css('span.psw-m-r-3::text').getall()

        jogos_precos = list(zip(jogos, precos))

        jogos_precos = self.bubble_sort(jogos_precos)

        for nome_jogo, preco_jogo in jogos_precos:
            yield {
                'nome_jogo': nome_jogo,
                'preco_jogo': preco_jogo,
            }

    def bubble_sort(self, jogos_precos):
        tamanho = len(jogos_precos)

        jogos_precos_formatados = []

        for nome, preco in jogos_precos:
            preco_formatado = float(preco.replace('R$', '').replace(',', '.').strip())
            jogos_precos_formatados.append((nome, preco_formatado)) 

        for i in range(tamanho):
            for j in range(0, tamanho-i-1):
                if jogos_precos_formatados[j][1] > jogos_precos_formatados[j+1][1]:
                    jogos_precos_formatados[j], jogos_precos_formatados[j+1] = jogos_precos_formatados[j+1], jogos_precos_formatados[j]

        return jogos_precos_formatados
