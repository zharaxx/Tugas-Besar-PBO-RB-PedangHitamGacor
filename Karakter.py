import pygame,random
from Main import dead
from Invicible import invicible
from Freeze import Freeze
import Path

class Karakter(pygame.sprite.Sprite) :
    def __init__(self):
        super(Karakter, self).__init_()
        pass
    def draw(self, screen):
        screen.blit(self.image,self.rect)
    def update(self, rintangan, musuh, koin, potion, waktu):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        self.x += self.velX
        self.y += self.velY
        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)
        if self.x <= 50 :
            self.x = 50
        if self.x >= 924 :
            self.x = 924
        if self.y <=40 :
            self.y = 40
        if self.y >= 535 :
            self.y = 535
        kena_rintangan = pygame.sprite.spritecollideany(self, rintangan)
        kena_musuh = pygame.sprite.spritecollideany(self, musuh)
        kena_koin = pygame.sprite.spritecollideany(self, koin)
        kena_item=pygame.sprite.spritecollideany(self,potion)
        if kena_rintangan:
            self.x, self.y = self.a, self.b
        else:
            self.a, self.b = self.rect[:2]
        if kena_musuh and not self.invicible :
            Path.skor = self.score
            dead()
        if kena_koin :
            self.score+=1
            if self.score%3==0 and self.score !=0 :
                tipe_item=random.randint(1,2)
                if tipe_item == 1 :
                    potion.add(invicible())
                else :
                    potion.add(Freeze())
        if kena_item :
            self.efek=waktu
        if waktu - self.efek == 10 and self !=0 :
            self.invicible = False
            if Path.karakter_pilihan == 1 :
                img=pygame.image.load("Assets/Gambar/Man.png")
                width = img.get_width()
                height = img.get_height()
                self.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
            else :
                img=pygame.image.load("Assets/Gambar/Girl.png")
                width = img.get_width()
                height = img.get_height()
                self.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
            for i in musuh :
                i.freeze = False
            self.efek=0