from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, email, credito):
        self._username = username
        self._email = email
        self._credito = credito
        self._ativo = False
        
    @abstractmethod
    def aplicar_credito(self, valor):
        pass
    
    @abstractmethod
    def aplicar_bonus(self):
        pass
    
        