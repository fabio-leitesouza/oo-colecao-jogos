from modelos.usuario.user import User

class UserPremium(User):
    """
    Classe UserPremium que herda da classe User.    
    Esta classe representa um usuário premium com funcionalidades adicionais.
    """    
    def __init__(self, username, email, premium_since, credito):
        
        super().__init__(username, email, credito)
        self._premium_since = premium_since
        self._benefits = []
    
    def add_benefit(self, benefit):
        """
        Adiciona um benefício à lista de benefícios do usuário premium.
        
        Args:
            benefit (str): O benefício a ser adicionado.
        """
        self.benefits.append(benefit)
    
    def list_benefits(self):
        """
        Lista todos os benefícios do usuário premium.
        
        Returns:
            list: Lista de benefícios.
        """
        return self.benefits
    
    def __str__(self):
        """
        Retorna uma representação em string do usuário premium.
        
        Returns:
            str: Representação do usuário premium.
        """
        return f"{self.username} (Premium since: {self.premium_since})"
