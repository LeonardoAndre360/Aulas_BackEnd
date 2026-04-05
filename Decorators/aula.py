def meu_decorator(func):
    def wrapper():
        print("Antes da execução da minha função!")
        func()
        print("Depois da execução da minha função!")
    return wrapper
    


@meu_decorator
def despedida():
    print("Tchau!")

def cheguei():
    print("Oiii")


cheguei()
despedida()
