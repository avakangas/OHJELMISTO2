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

    def kulje(self, tuntimäärä):
        # Lasketaan kuljettu matka ja päivitetään matka-ominaisuus
        kuljettu_matka = self.tämänhetkinennopeus * tuntimäärä
        self.matka += kuljettu_matka

auto1 = Auto('ABC-123', '142km/h')

print(f'Rekisteritunnus: {auto1.rekisteritunnus}, Huippunopeus: {auto1.huippunopeus}, Tämän hetkinen nopeus: {auto1.tämänhetkinennopeus}, Kuljettu matka: {auto1.matka}')

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f'Nopeus kiihdytyksen jälkeen: {auto1.tämänhetkinennopeus} km/h')

auto1.kulje(1.5)
print(f'Kuljettu matka 1.5 tunnin jälkeen: {auto1.matka} km')

auto1.kiihdytä(-200)
print(f'Nopeus hätäjarrutuksen jälkeen: {auto1.tämänhetkinennopeus} km/h')

auto1.kulje(1)
print(f'Kuljettu matka 1 tunnin jälkeen: {auto1.matka} km')