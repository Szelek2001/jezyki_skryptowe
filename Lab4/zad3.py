class student:
    def __init__(self, imie, ocena_z_analizy, aktywnosc):
        self.set_imie(imie)
        self.set_ocena(ocena_z_analizy)
        self.set_aktywnosc(aktywnosc)
        self.imie = imie
        self.__ocena_z_analizy = ocena_z_analizy
        self._aktywnosc = aktywnosc

    def set_imie(self,imie):
        if isinstance(imie,str):
            self.imie = imie
        else:
            raise TypeError

    def set_ocena(self, ocena):
        if isinstance(ocena, (int,float)):
            self.__ocena_z_analizy = ocena
        else:
            raise TypeError

    def set_aktywnosc(self, akty):
        if isinstance(akty, (int, float)):
            self._aktywnosc = akty
        else:
            raise TypeError

    def get_aktywnosc(self):
        return self._aktywnosc

    def get_imie(self):
        return self.imie

    def get_ocena(self):
        return self.__ocena_z_analizy

    def del_akty(self):
        del self._aktywnosc

    def del_ocena(self):
        del self.__ocena_z_analizy

    def del_imie(self):
        del self.imie

    def print_ocen(self):
        print(self.__ocena_z_analizy)

    def przywitaj_studenta(self):
        print("Witaj studencie o imieniu: ", self.imie)

    def _czy_dodac(self, ile_na_wyzsza_ocene):
        if self._aktywnosc > ile_na_wyzsza_ocene:
            return True
        return False

    def ocena_po_kolokwium(self, kolos):
        if self._czy_dodac(11):
            self.__ocena_z_analizy = kolos + 1
        else:
            self.__ocena_z_analizy = kolos

        if self.__ocena_z_analizy > 5:
            raise ValueError


myClassObjects = []
myClassObjects.append(student("Rafal", 5, 20))
myClassObjects.append(student("Jan", 2, 0))
myClassObjects.append(student("Adam", 2, 20))
myClassObjects.append(student("Oman", 6, 22))

myClassObjects[0].przywitaj_studenta()
myClassObjects[1].print_ocen()
myClassObjects[1].ocena_po_kolokwium(2)
myClassObjects[1].print_ocen()
myClassObjects[2].ocena_po_kolokwium(2)
myClassObjects[2].print_ocen()
