class Masina:
    def __init__(self, culoare: str, firma: str, cp: int):
        self.culoare == culoare

    @property
    def culoare(self):
        return self.__culoare

    @property.setter
    def culoare (self, value: str):
        if type(value) == str:
            self.__culoare = value
        else:
            print("error")

