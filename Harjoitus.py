class Hissi:
    def __init__(self, alin, ylin):
        self.kerros_alin = alin
        self.kerros_ylin = ylin
        self.kerros_nyt = alin  # Hissi aloittaa alimmasta kerroksesta

    def siirry_kerrokseen(self, kohde):
        if kohde > self.kerros_ylin or kohde < self.kerros_alin:
            print('Kerrosta ei ole')
            return

        while kohde > self.kerros_nyt:
            self.kerros_ylos()

        while kohde < self.kerros_nyt:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros_nyt < self.kerros_ylin:
            self.kerros_nyt += 1
            print(f'Nykyinen kerros: {self.kerros_nyt}')

    def kerros_alas(self):
        if self.kerros_nyt > self.kerros_alin:
            self.kerros_nyt -= 1
            print(f'Nykyinen kerros: {self.kerros_nyt}')
