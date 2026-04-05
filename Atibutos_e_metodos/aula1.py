# Uma classe é um Molde.
# Vamos usar esse Molde para construir coisas que queremos que tem um mesmo padrão

# - HP
# - Tipo do meu Pokemon (Terra, Elétrico, Fogo, etc)
# - Quais seus ataques (Choque do trovão)
# - Altura
# - Peso
# - Nome

# Nome -> Pikachu
# Hp -> 300
# Tipo -> Eletrico
# Ataque -> Choque do trovão
# Altura -> 50cm
# Peso -> 15kg

# nome -> Charizard
# Hp -> 450
# Tipo -> Fogo
# Ataque -> Lança Chama
# Altura -> 2m
# Peso -> 1500kg

class MoldePokemon:
   # Metodo == Função
   # Metodo construtor
   # Self tem a responsabilidade de armazenar e manipular essas informações dos atributos
   def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

   def mostrar_nome_pokemon(self):
       print(f"O nome do meu pokemon é: {self.nome}")
   
   def mostrar_altura_pokemon(self):
       pass
   
   def mostrar_hp_pokemon(self):
       pass
   
   def mostrar_tipo_pokemon(self):
       pass
   
   def mostrar_ataque_pokemon(self):
       pass
   
   def mostrar_peso_pokemon(self):
       pass