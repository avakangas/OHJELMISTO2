class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinennopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus.replace('km/h', '').strip())
        self.tämänhetkinennopeus = tämänhetkinennopeus
        self.matka = matka

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämänhetkinennopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinennopeus = 0
        else:
            self.tämänhetkinennopeus = uusi_nopeus

    def aja(self, tunteja):
        self.matka += self.tämänhetkinennopeus * tunteja


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print(f"Sähköauto - Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, "
              f"Tämänhetkinen nopeus: {self.tämänhetkinennopeus} km/h, Kuljettu matka: {self.matka} km, "
              f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def tulosta_tiedot(self):
        print(f"Polttomoottoriauto - Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, "
              f"Tämänhetkinen nopeus: {self.tämänhetkinennopeus} km/h, Kuljettu matka: {self.matka} km, "
              f"Bensatankin koko: {self.bensatankin_koko} l")


if __name__ == "__main__":
    sähköauto = Sähköauto("ABC-15", "180 km/h", 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", "165 km/h", 32.3)

    sähköauto.kiihdytä(100)
    polttomoottoriauto.kiihdytä(120)

    sähköauto.aja(3)
    polttomoottoriauto.aja(3)

    print("Autojen tiedot:")
    sähköauto.tulosta_tiedot()
    polttomoottoriauto.tulosta_tiedot()
