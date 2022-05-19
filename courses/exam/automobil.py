# Cumpărătorul  mai  este  interesat  de  culoarea  maşinii (string), firma producătoare (string) şi de alte dotări:
#
# -vopsea metalizată (boolean)
# -aer condiţionat (boolean)
# -sistem de frânare (string)
# -airbag şofer (boolean)
# -faruri dublu optice (boolean)

from motor import Motor
from vehicul import Vehicul


class Automobil(Vehicul):
    def __init__(self, motor: Motor, culoare: str, firma: str, vopsea_metalizata: bool, aer_conditionat: bool,
                 sistem_de_franare: str, airbag_sofer: bool, faruri_dublu_optice: bool, nr_roti: int, nr_usi: int,
                 nr_locuri: int, capacitate_rezervor: int, capacitate_portbagaj: int, lungime: int, latime: int,
                 inaltime: int, consum_urban: int, consum_extraurban: int, consum_mixt: int):
        super().__init__(nr_roti, nr_usi, nr_locuri, capacitate_rezervor, capacitate_portbagaj, lungime, latime,
                         inaltime, consum_urban, consum_extraurban, consum_mixt)
        self.set_motor(motor)
        self.set_culoare(culoare)
        self.__firma = firma
        self.set_vopsea_metalizata(vopsea_metalizata)
        self.__aer_conditionat = aer_conditionat
        self.__sistem_de_franare = sistem_de_franare
        self.__airbag_sofer = airbag_sofer
        self.__faruri_dublu_optice = faruri_dublu_optice

    def get_motor(self) -> Motor:
        return self.__motor

    def set_motor(self, value: Motor):
        self.__motor = value

    def get_culoare(self) -> str:
        return self.__culoare

    def set_culoare(self, value: str):
        self.__culoare = value

    def get_vopsea_metalizata(self) -> bool:
        return self.__vopsea_metalizata

    def set_vopsea_metalizata(self, value: bool):
        self.__vopsea_metalizata = value

    def print_caracteristici(self):
        print(f"Caracteristici:\n"
              f"    Motorul are {str(self.__motor.get_nr_cilindiri())} cilindri, "
              f"puterea maxima este {str(self.__motor.get_max_putere())} "
              f"si are catalizatorul {self.__motor.get_catalizator()}.\n"
              f"    Masina are {str(self.get_nr_roti())} roti, "
              f"capacitatea rezervorului este de {str(self.get_capacitate_rezervor())},"
              f"si are consumul urban de {str(self.get_consum_urban())}."
              f"    Este de culoare {self.get_culoare()}. "
              f"{'Are' if self.get_vopsea_metalizata() else 'Nu are'} vopsea metalizata.")



