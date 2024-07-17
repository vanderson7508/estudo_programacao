class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True


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



livro1 = Livro('cabana', 'john', 1988)
livro2 = Livro('habitos', 'jack', 2013)


print(livro1)
print(livro2)

livro1.emprestar('cabana')
livro1.emprestar('cabana')
