# Molde do Pokemon

# Vamos ter vários atributos

# A classe é o molde que vamos criar para poder conseguirmos construir coisas

class MoldePokemon:
    def __init__(self, nome, altura, peso, hp, ataque, tipo):
        self.nome = nome
        self.altura = float(altura)
        self.peso = peso
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo
   
    def mostrar_nome_pokemon(self):
        print(f"O nome do meu pokemon é: {self.nome}")
    
    def mostrar_altura_pokemon(self):
        if self.altura >= 100:
            altura_em_metros = self.altura / 100
            print(f"A altura do meu pokemon é: {altura_em_metros}m")
        else:
            print(f"A altura do meu pokemon é: {self.altura}cm")

    def mostrar_peso_pokemon(self):
        print(f"O peso do meu pokemon é {self.peso}")

# Chegou a hora de pegar a classe e de fato construir essas coisas
# Por enquanto, a gente ainda tem apenas o molde
# Construir dentro da Orientação a Objetos significa criar um Objeto

pikachu = MoldePokemon("Pikachu", 200, 150, 400, "Choque do trovão", "Eletrico")
pikachu.mostrar_nome_pokemon()
pikachu.mostrar_altura_pokemon()
pikachu.mostrar_peso_pokemon()