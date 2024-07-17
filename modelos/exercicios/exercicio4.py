class Cliente:
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.cpf = cpf


    def __str__(self):
        return f'{self.nome} | {self.cpf}'


cliente_vanderson = Cliente('vanderson', 2338268156)

print(cliente_vanderson)
