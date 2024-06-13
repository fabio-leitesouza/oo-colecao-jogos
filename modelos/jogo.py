#metodo especial construtor __ini__
#metodo especial __srt__ para mostar um objeto em forma de texto

class Jogo:
    jogos = []
    
    def __init__(self, nome, categoria):        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Jogo.jogos.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    def listar_jogos():
        print(f"{'Nome do jogo'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}")
        for jogo in Jogo.jogos:
            print(f'{jogo._nome.ljust(20)} | {jogo._categoria.ljust(20)} | {jogo.ativo}')    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
     
    
    
jogo_zelda = Jogo('zelda', 'RPG')
jogo_metroid = Jogo('Metroid', 'Plataforma')

Jogo.listar_jogos()

