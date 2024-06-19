from modelos.jogo import Jogo
from modelos.plataforma import Plataforma
from modelos.usuario.basic import BasicUser

super_nintendo = Plataforma('Nintendo', 'Nintendo')
master_system = Plataforma('Master System', 'Sega')
steam = Plataforma("Steam", "Valve")

jogo_zelda = Jogo('Zelda', 'RPG', 199.99)
jogo_sonic = Jogo('MegaMan', 'Plataforma', 100)
jogo_cyberpunk2077 = Jogo("Cyberpunk 2077", "RPG", 0)

super_nintendo.adicionar_jogo(jogo_zelda)
master_system.adicionar_jogo(jogo_sonic)
steam.adicionar_jogo(jogo_cyberpunk2077)

# Alterando o status do jogo "Cyberpunk 2077"
jogo_cyberpunk2077.alterar_status()

jogo_zelda.recebe_nota('Souza', 10)

usuario_souza = BasicUser('Souza', 'souza@souza', 0)
usuario_souza.aplicar_credito(10)
usuario_souza.aplicar_bonus()


def main():
    Jogo.listar_jogos()
    steam.exibir_jogos()
    print(usuario_souza._credito)

if __name__ == '__main__':
    main()