class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.cnpj = None
        self.endereco = None
        self.ativo = False


    def __str__(self):
        return f'Nome = {''.ljust(4)} {self.nome}\nCategoria = {self.categoria}'


restaurante_italian = Restaurante(nome='italian', categoria='italiano')

print(restaurante_italian)
