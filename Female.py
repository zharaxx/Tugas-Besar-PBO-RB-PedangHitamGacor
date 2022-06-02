from Karakter import pygame,Karakter
class Female(Karakter) :
    def __init__(self, x, y):
        self.score=0
        self.invicible=False
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        img=pygame.image.load("Assets/Gambar/Girl.png")
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 5
        self.a, self.b = self.x, self.y
        self.efek=0