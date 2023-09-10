
class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto {cls.instance}')
        return cls.instance

    def __init__(self, nome):
        self.nome = nome
        print(f'Inicializando o objeto {self.nome}')


s1 = Singleton('Angelina')
print(f'Instância de s1: {id(s1)}')

s2 = Singleton('João')
print(f'Instância de s2: {id(s2)}')