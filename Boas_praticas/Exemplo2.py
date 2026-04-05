# Animal: Classe base que define um método falar que será sobrescrito pela subclasses.
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass
# Cachorro e Gato: Subclasses que herdam Animal e Implementam o método falar com comportamentos especificos
class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    
class Gato(Animal):
    def falar(self):
        return "Miau!"
    
# Criando Instãncias das classes
# Instâncias de Cachorro e Gato são criadas e seus métodos falar são chamados para exibir os sons especificos de cada animal 
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

#Exibindo os sons dos animais
print(cachorro.nome + " diz " + cachorro.falar())
print(gato.nome + " diz " + gato.falar())