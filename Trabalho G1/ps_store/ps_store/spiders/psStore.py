import scrapy

class PsstoreSpider(scrapy.Spider):
    name = "psStore"
    allowed_domains = ["store.playstation.com"]
    start_urls = ["https://store.playstation.com/pt-br/category/8a31d28e-61a4-4794-9286-24f7944b7c5c/1"]

    def parse(self, response):
        jogos = response.css('span.psw-t-body::text').getall() 
        precos = response.css('span.psw-m-r-3::text').getall() 
        for jogos, precos in zip(jogos, precos):
                yield{
                'nome_jogo': jogos,
                'preco_jogo': precos,
                }