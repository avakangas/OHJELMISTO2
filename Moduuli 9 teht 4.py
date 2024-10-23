import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinennopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
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
        kuljettu_matka = self.tämänhetkinennopeus * tuntimäärä
        self.matka += kuljettu_matka

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i}"
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_kaynnissa = False

print(f"{'Rekisteritunnus':<12} {'Huippunopeus (km/h)':<20} {'Tämän hetkinen nopeus (km/h)':<30} {'Kuljettu matka (km)':<20}")
print("="*100)
for auto in autot:
    print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<20} {auto.tämänhetkinennopeus:<30} {auto.matka:<20}")
