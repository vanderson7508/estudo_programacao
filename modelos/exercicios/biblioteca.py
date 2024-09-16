from livro import Livro

livro1 = Livro('vanderson', 'Drummont', 1988)
livro2 = Livro('ludmilla', 'lopes', 1990)
livro3 = Livro('wesley', 'macedo', 1990)
livro4 = Livro('thiago', 'santos', 1998)

#livro1.emprestar('vanderson')
#print(livro1._disponivel)

Livro.livros = [livro1, livro2, livro3, livro4]
result = Livro.verificar_disponibilidade(1990)

for livro in result:
    print(livro)



