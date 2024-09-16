class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self.livros = []



    def __str__(self):
        return f'Titulo: {self._titulo} | Autor: {self._autor} | Ano de publicacao: {self._ano_publicacao}'


    @property
    def titulo(self):
        return self._titulo


    @property
    def autor(self):
        return self._autor


    @property
    def ano_publicacao(self):
        return self._ano_publicacao



    def emprestar(self, titulo):
        if self._disponivel == True:
            print('Livro esta disponivel')
        else:
            print('Livro indisponivel')

        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis


livro1 = Livro('cabana', 'john', 1988)
livro2 = Livro('habitos', 'jack', 1990)

Livro.livros = [livro1, livro2]
resultado = Livro.verificar_disponibilidade(1988)

for livro in resultado:
    print(livro)

