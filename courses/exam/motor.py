class Motor:
    def __init__(self, nr_cilindri: int, nr_supape: int, max_putere: int, tip_carburant: int,
                 tip_injectie: int, catalizator: str, sisteme_alimentare: str):
        self.set_nr_cilindri(nr_cilindri)
        self.__nr_supape = nr_supape
        self.set_max_putere(max_putere)
        self.__tip_carburant = tip_carburant
        self.__tip_injectie = tip_injectie
        self.set_catalizator(catalizator)
        self.__sisteme_alimentare = sisteme_alimentare

    def get_nr_cilindri(self) ->int:
        return self.__nr_cilindtri

    def set_nr_cilindri(self, value: int):
        self.__nr_cilindtri = value

    def get_max_putere(self) -> int:
        return self.__max_putere

    def set_max_putere(self, value: int):
        self.__max_putere = value

    def get_catalizator(self) -> str:
        return self.__catalizator

    def set_catalizator(self, value: str):
        self.__catalizator = value

