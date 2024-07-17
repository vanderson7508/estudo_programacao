class Casa:
    def __init__(self, tamanho):
        self._tamanho = tamanho  # Atributo privado

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, novo_tamanho):
        if novo_tamanho > 0:
            self._tamanho = novo_tamanho
        else:
            print("O tamanho da casa deve ser maior que zero.")

