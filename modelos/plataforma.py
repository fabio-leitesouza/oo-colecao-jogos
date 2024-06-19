from modelos.jogo import Jogo

class Plataforma:
    def __init__(self, nome, empresa):
        self._nome = nome
        self._empresa = empresa
        self._jogos = [] 
        
    def __str__(self):
        return self._nome
    
    def adicionar_jogo(self, jogo):
        self._jogos.append(jogo)
        
    def exibir_jogos(self):
        print(f'Os jogos da plataforma {self._nome}')
        for i, jogo in enumerate(self._jogos, start=1):
            if hasattr(jogo, 'categoria'):
                mensagem = f'{i} | Nome: {jogo._nome} | Categoria: {jogo._categoria} | Preço: {jogo._preco}'
                print(mensagem)
            else:
                mensagem = f'{i} | Nome: {jogo._nome} | Categoria: {jogo._categoria} | Preço: {jogo._preco}'
                print(mensagem)