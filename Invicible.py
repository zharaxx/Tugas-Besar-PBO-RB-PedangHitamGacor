import random,Path
from Item import pygame,Item
from Maps import Maps
class invicible(Item) :
    def __init__(self) :
        super(Item, self).__init__()
        img=pygame.image.load("Assets/Gambar/invicible.png")
        width=img.get_width()
        height=img.get_height()
        self.image=pygame.transform.scale(img,((width*0.5),(height*0.5)))
        self.rect = self.position_random(Maps())
    def position_random(self,halangan):
        rect = self.image.get_rect(center = (random.randint(60,940), random.randint(50,550)))
        for kotak in halangan.kotak:
            if rect.colliderect(kotak.rect):
                return self.position_random(Maps())
        return rect
    def draw(self,screen,player,musuh):
        screen.blit(self.image, self.rect)
        kena_player=self.rect.colliderect(player.rect)
        if kena_player :
            if Path.karakter_pilihan == 1 :
                img=pygame.image.load("Assets/Gambar/boy invicible.png")
                width = img.get_width()
                height = img.get_height()
                player.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
            else :
                img=pygame.image.load("Assets/Gambar/girl invicible.png")
                width = img.get_width()
                height = img.get_height()
                player.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
            player.invicible=True
            Path.invicible_sound.play()
            self.kill()