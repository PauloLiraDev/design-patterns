# Monostate é um padrão de projeto que garante que todas as instâncias de uma classe compartilhem o mesmo estado.
# Mesmo que você crie várias instâncias, todas elas compartilharão o mesmo estado.


class Monostate:

    __estado = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj


m1 = Monostate()
print('M1 ID: ', id(m1))
print(m1.__dict__)

m2 = Monostate()
print('M2 ID: ', id(m2))
print(m2.__dict__)

m1.nome = "Felicity"
print('M1: ', m1.__dict__)
print('M2: ', m2.__dict__)
