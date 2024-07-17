class ClienteBanco:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self._saldo = 500


    def __str__(self):
        return f'Nome: {self.nome} | CPF: {self.cpf}'


    @property
    def saldo(self):
        return self._saldo


    def sacar(self, valor):
        self._saldo -= valor




cliente_1 = ClienteBanco('vanderson', 298478748, 4985955)
cliente_2 = ClienteBanco('vani', 674765875, 6199934784)
cliente_3 = ClienteBanco('graca', 298478748, 4985955)

print(cliente_1)
print(cliente_2)
print(cliente_3)

cliente_1.sacar(50)

print(cliente_1._saldo)
