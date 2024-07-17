class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao


    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'


    def aniversario(self):
        self._idade += 1


    @property
    def saudacao(self):
        return print(f'Olá {self._profissao} seja bem vindo!!!')


pessoa_vanderson = Pessoa('vanderson', 35, 'policial')

pessoa_vanderson.aniversario()
pessoa_vanderson.aniversario()

print(pessoa_vanderson)

pessoa_vanderson.saudacao
