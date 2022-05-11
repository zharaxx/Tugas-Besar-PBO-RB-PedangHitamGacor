class Karakter :
    def __init__(self):
        pass
    def draw(self, screen):
        screen.blit(self.image,self.rect)
    def update(self):
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

class Male(Karakter) :
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        img=pygame.image.load("Man.png")
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

class Female(Karakter) :
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        img=pygame.image.load("Girl.png")
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img,((width*0.2),(height*0.2)))
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4