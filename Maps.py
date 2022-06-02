import pygame, Rintangan
class Maps():
    def __init__(self):
        self.kotak = pygame.sprite.Group()
        self.kotak1 = Rintangan.RINTANGAN((61, 347), (309, 129))
        self.kotak2 = Rintangan.RINTANGAN((61, 350), (630, 129))
        self.kotak3 = Rintangan.RINTANGAN((61,116),(148,127))
        self.kotak4 = Rintangan.RINTANGAN((61,116),(148,360))
        self.kotak5 = Rintangan.RINTANGAN((61,116),(793,126))
        self.kotak6 = Rintangan.RINTANGAN((61,116),(793,360))
        self.kotak7 = Rintangan.RINTANGAN((62,175),(469,40))
        self.kotak8 = Rintangan.RINTANGAN((62,175),(470,392))
        self.kotak.add(self.kotak1, self.kotak2,self.kotak3,self.kotak4,self.kotak5,self.kotak6,self.kotak7,self.kotak8)
    def tampil(self, screen):
        self.kotak.update(screen)