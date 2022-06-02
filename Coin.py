import random,Path
from Maps import Maps
from Item import pygame,Item
class coin(Item) :
    def __init__(self) :
        super(Item, self).__init__()
        img=pygame.image.load("Assets/Gambar/coin.png")
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
    def draw(self,screen,player,item):
        screen.blit(self.image, self.rect)
        kena_player=self.rect.colliderect(player.rect)
        if kena_player :
            item.add(coin())
            self.kill()
            print(player.score)
            Path.coin_sound.play()