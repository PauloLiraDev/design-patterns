from typing import List, Tuple


class Curso:

    def __init__(self, curso: str = "Curso Padrão", carga_horaria: int = 45) -> None:
        self.__curso = curso
        self.__carga_horaria = carga_horaria


# Polimorfismo
curso1: Curso = Curso()
curso2: Curso = Curso("Padrões de Projeto em Python")
curso3: Curso = Curso("Python para Data Science", 40)

# print(curso1.__dict__)
# print(curso2.__dict__)
# print(curso3.__dict__)

nome: str = "Geek University"
tupla: Tuple = (1, 3, 5, 7, 9)
lista: List = [2, 4, 6, 8, 10]

# print(nome[:4], tupla[:4], lista[:4])


class Pessoa:

    def __init__(self: object, nome: str) -> None:
        self.__nome = nome

    def andar(self: object) -> str:
        print(f"{self.__nome} está andando")


class Aluno(Pessoa):

    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula


felicity = Aluno('Felicity Jones', '1234')
# felicity.andar()


# Abstração
def gerar_fibonacci(qtd: int) -> None:
    if qtd <= 0:
        print("Quantidade deve ser maior que 0")
    else:
        print(f'A sequência de Fibonacci para {qtd} termo(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1, end=', ')
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1


# gerar_fibonacci(10)


# Composição
class Motor:

    def ligar(self) -> None:
        print("Motor está ligado")


class Pneu:

    def encher(self: object) -> None:
        print("Pneu está cheio")


class Carro:

    def __init__(self: object) -> None:
        self.__motor = Motor()
        self.__pneu = Pneu()
