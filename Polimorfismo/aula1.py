class Animal:
    def falar(self):
        pass

class Cachorro:
    def falar(self):
        return "Au Au"
    
class Gato:
    def falar(self):
        return "Miau Miau"
    
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())