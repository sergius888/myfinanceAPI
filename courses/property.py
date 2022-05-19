class Masina:
    def __init__(self, culoare: str):
        self.culoare = culoare

    @property
    def culoare(self):
        return self.__culoare

    @culoare.setter
    def culoare(self, value: str):
        if type(value) == str:
            self.__culoare = value
        else:
            print("error")



new_car = Masina("blue")
print(new_car.culoare)
new_car.culoare = 2
print(new_car.culoare)
