class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Utilizando property")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Utilizando setter")
        self.__nome = nome
