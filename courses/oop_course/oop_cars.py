class Car:
    def __init__(self, model: str, brand: str, price: int):
        self.model = model
        self.brand = brand
        self.price = price

    def start_engine(self):
        print("start")


vw = Car("golf", "volwsvagen", 30000)


class Volwsvagen(Car):
    def __init__(self, model: str, price: int):
        super().__init__(model, "volwsvagen", price)


class VolwsvagenGolf(Volwsvagen):
    def __init__(self):
        super().__init__("golf", 30000)


vw2 = VolwsvagenGolf()
print(vw2.start_engine())