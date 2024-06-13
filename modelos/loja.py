# Classe Motocicleta
class Motocicleta:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Instanciando uma Motocicleta
motocicleta1 = Motocicleta("Honda CB500", "Vermelha", 2022)
print(f"Modelo: {motocicleta1.modelo}, Cor: {motocicleta1.cor}, Ano: {motocicleta1.ano}")

# Classe Loja
class Loja:
    def __init__(self, nome, categoria, endereco, telefone):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.telefone = telefone
        self.ativo = False

    # Método especial __str__
    def __str__(self):
        return f"Loja: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Telefone: {self.telefone}"

# Instanciando uma Loja
loja1 = Loja("Loja de Motos", "Motocicletas", "Rua das Motos, 123", "(11) 98765-4321")
print(loja1)

# Classe Cliente
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três Clientes
cliente1 = Cliente("João Silva", 30, "joao.silva@email.com", "(11) 91234-5678")
cliente2 = Cliente("Maria Souza", 25, "maria.souza@email.com", "(11) 92345-6789")
cliente3 = Cliente("Pedro Oliveira", 35, "pedro.oliveira@email.com", "(11) 93456-7890")

print(f"Cliente 1: Nome: {cliente1.nome}, Idade: {cliente1.idade}, Email: {cliente1.email}, Telefone: {cliente1.telefone}")
print(f"Cliente 2: Nome: {cliente2.nome}, Idade: {cliente2.idade}, Email: {cliente2.email}, Telefone: {cliente2.telefone}")
print(f"Cliente 3: Nome: {cliente3.nome}, Idade: {cliente3.idade}, Email: {cliente3.email}, Telefone: {cliente3.telefone}")


