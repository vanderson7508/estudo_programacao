from modelos.restaurante import Restaurante


restaurante_praca = Restaurante('praca', 'Goumert')
restaurante_praca.receber_avaliacao('carlos', 10)
restaurante_praca.receber_avaliacao('lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

