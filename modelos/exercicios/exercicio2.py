class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'


fusca = Carro('fiat', 'branco', 1999)

print(fusca)
