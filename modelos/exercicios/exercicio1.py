class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao  


    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'


musica1 = Musica('onda', 'lulu', 50)
print(musica1)

