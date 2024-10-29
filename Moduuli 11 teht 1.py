class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


if __name__ == "__main__":
    julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
    julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    print("Julkaisu 1 tiedot:")
    julkaisu1.tulosta_tiedot()
    print("\nJulkaisu 2 tiedot:")
    julkaisu2.tulosta_tiedot()
