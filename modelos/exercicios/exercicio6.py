class Conta_bancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False


    def __str__(self):
        return f'Titular: {self._titular} | Saldo: {self._saldo}'


conta_lud = Conta_bancaria('Ludmilla', 500)
conta_vando = Conta_bancaria('vanderson', 500)

print(conta_lud)
print(conta_vando)


