class Restaurante:
    nome = ''
    categoria = ''
    estado = False


restaurante_01 = Restaurante

restaurante_01.nome = 'Bistro'


print(restaurante_01.nome)

restaurante_pizza = Restaurante
restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.categoria)

if restaurante_pizza.categoria == 'Fast Food':
    print('É um fast')
else:
    print('Nao é fast')


print(restaurante_pizza.estado)
