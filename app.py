from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praca', 'Goumert')
restaurante_praca.receber_avaliacao('carlos', 15)
restaurante_praca.receber_avaliacao('lais', 10)
restaurante_praca.receber_avaliacao('Emy', 4)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

