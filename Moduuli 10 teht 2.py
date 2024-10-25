from Harjoitus import Hissi

class Talo:
    def __init__(self, alin,ylin, lkm):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.hissien_lkm = lkm
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(self.alin_kerros,self.ylin_kerros))

    def aja_hissia(self, numero, kohdekerros):
        if numero > self.hissien_lkm or numero < 1:
            print('Hissiä ei ole')
            return
        print(f'Hissin numero: {numero}')
        self.hissit[numero - 1].siirry_kerrokseen(kohdekerros)