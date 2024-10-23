class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinennopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = tämänhetkinennopeus
        self.matka = matka

auto1 = Auto('ABC-123', '142km/h')

print(f'Rekisteritunnus: {auto1.rekisteritunnus}, Huippunopeus: {auto1.huippunopeus}, Tämän hetkinen nopeus: {auto1.tämänhetkinennopeus}, Kuljettu matka: {auto1.matka}')