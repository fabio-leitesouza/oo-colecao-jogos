from modelos.jogo import Jogo

jogo_zelda = Jogo('Zelda', 'RPG')
jogo_megaman = Jogo('MegaMan', 'plataforma')
jogo_metroid = Jogo('Metroid', 'plataforma')
jogo_sonic = Jogo('soni', 'plataforma')

jogo_metroid.alterar_status()

jogo_metroid.recebe_nota('Souza', 10)
jogo_metroid.recebe_nota('Eduarda', 8)
jogo_metroid.recebe_nota('Pedro', 7)

def main():
    Jogo.listar_jogos()

if __name__ == '__main__':
    main()