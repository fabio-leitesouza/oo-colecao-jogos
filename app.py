from modelos.jogo import Jogo
from modelos.plataforma import Plataforma

super_nintendo = Plataforma('Nintendo', 'Nintendo')
master_system = Plataforma('Master System', 'Sega')
steam = Plataforma("Steam", "Valve")

super_nintendo.adicionar_jogo("Zelda", "RPG", 99.99)
super_nintendo.adicionar_jogo('MegaMan', 'Plataforma', 100)
master_system.adicionar_jogo('sonic', 'plataforma', 0)
steam.adicionar_jogo("Cyberpunk 2077", "RPG", 0)
steam.adicionar_jogo("The Witcher 3", "RPG", 0)

# Alterando o status do jogo "Cyberpunk 2077"
steam.alterar_status_jogo("Cyberpunk 2077")
super_nintendo.alterar_status_jogo("MegaMan")

super_nintendo.recebe_nota_jogo('Zelda', 'Souza', 10)


def main():
    Jogo.listar_jogos()

if __name__ == '__main__':
    main()