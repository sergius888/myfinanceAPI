# clasa Vehicul care are următoarele atribute:
# număr roţi (int), număr uşi (int), număr locuri (int);
# capacitate rezervor (int) /portbagaj (int) u.m. : litru;
# dimensiuni: lungime (int) / lăţime(int); înălţime(int)  u.m.:  mm;
# consum: urban/extraurban/mixt (int) u.m.:litri/100km

class Vehicul:
    def __init__(self, nr_roti: int, nr_usi: int, nr_locuri: int, capacitate_rezervor: int,
                 capacitate_portbagaj: int, lungime: int, latime: int, inaltime: int,
                 consum_urban: int, consum_extraurban: int, consum_mixt: int):
        self.set_nr_roti(nr_roti)
        self.__nr_usi = nr_usi
        self.__nr_locuri = nr_locuri
        self.set_capacitate_rezervor(capacitate_rezervor)
        self.__capacitate_portbagaj = capacitate_portbagaj
        self.__lungime = lungime
        self.__latime = latime
        self.__inaltime = inaltime
        self.set_consum_urban(consum_urban)
        self.__consum_extraurban = consum_extraurban
        self.__consum_mixt = consum_mixt

    def get_nr_roti(self) -> int:
        return self.__nr_roti

    def set_nr_roti(self, value: int):
        self.__nr_roti = value

    def get_capacitate_rezervor(self) -> int:
        return self.__capacitate_rezervor

    def set_capacitate_rezervor(self, value: int):
        self.__capacitate_rezervor = value

    def get_consum_urban(self) -> int:
        return self.__consum_urban

    def set_consum_urban(self, value: int):
        self.__consum_urban = value

