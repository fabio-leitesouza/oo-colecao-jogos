from modelos.usuario.user import User

class BasicUser(User):    
    def __init__(self, username, email, credito):        
        super().__init__(username, email, credito)
        
    def aplicar_credito(self, valor):
        if valor > 0:
            self._credito += valor
            print(f"Crédito de {valor} adicionado. Novo saldo: {self._credito}")
        else:
            print("O valor do crédito deve ser positivo.")
    
    def aplicar_bonus(self):
        self._credito += (self._credito * 0.03)
    