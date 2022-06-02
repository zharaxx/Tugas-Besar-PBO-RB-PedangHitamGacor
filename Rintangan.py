import pygame
class RINTANGAN(pygame.sprite.Sprite):
    def __init__(self, ukuran, posisi):
        super(RINTANGAN, self).__init__()
        self.surf = pygame.Surface(ukuran)
        self.surf.fill((100, 100, 100))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = posisi
    def update(self, Layar):
        Layar.blit(self.surf, self.rect)