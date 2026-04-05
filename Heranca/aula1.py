class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo")

class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: au au")

meu_cachorrinho = Cachorro("Goku")

meu_cachorrinho.comer()
meu_cachorrinho.latir()

#animal = Animal("Cachorro")
#animal.comer()