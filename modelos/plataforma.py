from modelos.jogo import Jogo

class Plataforma:
    def __init__(self, nome, empresa):
        self._nome = nome
        self._empresa = empresa
        self._jogos = [] 
    
    def adicionar_jogo(self, nome, categoria, preco):
        jogo = Jogo(nome, categoria, preco)
        self._jogos.append(jogo)
    
    def encontrar_jogo(self, nome):
        for jogo in self._jogos:
            if jogo._nome == nome.title():
                return jogo
        return None
    
    def alterar_status_jogo(self, nome):
        jogo = self.encontrar_jogo(nome)
        if jogo:
            jogo.alterar_status()
            print(f"Status do jogo '{jogo._nome}' foi alterado para {jogo.ativo}.")
        else:
            print(f"Jogo '{nome}' não encontrado.")
    
    def recebe_nota_jogo(self, nome, usuario, nota):
        jogo = self.encontrar_jogo(nome)
        if jogo:
            jogo.recebe_nota(usuario, nota)
            print(f"Nota {nota} recebida para o jogo '{jogo._nome}' do usuário '{usuario}'.")
        else:
            print(f"Jogo '{nome}' não encontrado.")