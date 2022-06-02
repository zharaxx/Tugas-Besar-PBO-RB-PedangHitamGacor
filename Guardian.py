import pygame,random
class Guardian(pygame.sprite.Sprite) :
    def __init__(self,x,y) :
        super(Guardian, self).__init__()
        img=pygame.image.load("Assets/Gambar/Guardian.png")
        width=img.get_width()
        height=img.get_height()
        self.image=pygame.transform.scale(img,((width*0.5),(height*0.5)))
        self.rect = self.image.get_rect(center = (x, y))
        self.a, self.b = x, y
        self.speed = 3
        self.arah = 'x'
        self.acak = random.choice([-1, 1])
        self.kejar = False
        self.freeze = False
    def draw(self, screen) :
        screen.blit(self.image,self.rect)
    def update(self, rintangan, karakter) :
        kena = False
        if self.freeze :
            self.rect.x, self.rect.y = self.a, self.b
        else :
            if self.rect.x <= 50 :
                self.rect.x = 50
                kena = True
            if self.rect.x >= 924 :
                self.rect.x = 924
                kena = True
            if self.rect.y <=40 :
                self.rect.y = 40
                kena = True
            if self.rect.y >= 535 :
                self.rect.y = 535
                kena = True
            kena_rintangan = pygame.sprite.spritecollideany(self, rintangan)
            if self.kejar and not kena_rintangan:
                arah_x = 1 if karakter.rect.x - self.rect.x > 0 else -1 if karakter.rect.x - self.rect.x < 0 else 0
                arah_y = 1 if karakter.rect.y - self.rect.y > 0 else -1 if karakter.rect.y - self.rect.y < 0 else 0
                self.rect.x = self.rect.x + (arah_x * self.speed)
                self.rect.y = self.rect.y + (arah_y * self.speed)
            if abs(self.rect.x - karakter.rect.x) <= 100 and abs(self.rect.y - karakter.rect.y) <= 100 :
                self.kejar=True
            else :
                self.kejar=False
            if kena_rintangan or kena:
                self.rect.x, self.rect.y = self.a, self.b
                if not self.kejar :
                    self.arah = random.choice(["x", "y"])
                    self.acak = random.choice([-1, 1])
            else:
                self.a, self.b = self.rect[:2]
            if not self.kejar :
                if self.arah == 'x':
                    self.rect.x = self.rect.x + (self.acak * self.speed)
                elif self.arah == 'y':
                    self.rect.y = self.rect.y + (self.acak * self.speed)
