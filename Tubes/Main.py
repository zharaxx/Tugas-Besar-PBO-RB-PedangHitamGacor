from tkinter import Menu
from turtle import width
import pygame,sys
from pygame import mixer

# class Halangan(pygame.sprite.Sprite) :
#     def __init__(self) -> None:
#         super(Halangan, self).__init__()
#     pass
class RINTANGAN(pygame.sprite.Sprite):
	def __init__(self, ukuran, posisi):
		super(RINTANGAN, self).__init__()
		self.surf = pygame.Surface(ukuran)
		self.surf.fill((100, 100, 100))
		self.rect = self.surf.get_rect()
		self.rect.x, self.rect.y = posisi
	def update(self, Layar):
		Layar.blit(self.surf, self.rect)
        
class Maps():
    def __init__(self):
        self.kotak = pygame.sprite.Group()
        self.kotak1 = RINTANGAN((125, 60), (115, 95))
        self.kotak2 = RINTANGAN((125,60), (115, 451))
        self.kotak3 = RINTANGAN((125, 60), (760, 85))
        self.kotak4 = RINTANGAN((125, 60), (757, 438))
        self.kotak5 = RINTANGAN((65, 40),(146, 155))
        self.kotak6 = RINTANGAN((65, 40),(146, 420))
        self.kotak7 = RINTANGAN((65, 40),(791, 141))
        self.kotak8 = RINTANGAN((65, 40),(789, 409))
        self.kotak9 = RINTANGAN((61, 347), (310, 129))
        self.kotak10 = RINTANGAN((61, 347), (630, 115))
        self.kotak11 = RINTANGAN((65, 120),(469,38))
        self.kotak12 = RINTANGAN((65, 120),(469,449))
        self.kotak13 = RINTANGAN((125, 65), (438, 155))
        self.kotak14 = RINTANGAN((125, 65), (438, 390))
        self.kotak.add(self.kotak1, self.kotak2, self.kotak3, self.kotak4, self.kotak5,
        self.kotak6, self.kotak7, self.kotak8, self.kotak9, self.kotak10, self.kotak11, self.kotak12,
        self.kotak13, self.kotak14)
    def tampil(self, screen):
        self.kotak.update(screen)

class Guardian(pygame.sprite.Sprite) :
    def __init__(self,x,y) :
        super(Guardian, self).__init__()
        self.x=int(x)
        self.y=int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        img=pygame.image.load("Assets\Gambar\Guardian.png")
        width=img.get_width()
        height=img.get_height()
        self.image=pygame.transform.scale(img,((width*0.5),(height*0.5)))
        self.a, self.b = self.x, self.y
    def draw(self, screen) :
        screen.blit(self.image,self.rect)
    def update(self, rintangan) :
        kena_rintangan = pygame.sprite.spritecollideany(self, rintangan)
        if kena_rintangan:
            self.x, self.y = self.a, self.b
        else:
            self.a, self.b = self.rect[:2]

    

class Karakter(pygame.sprite.Sprite) :
    def __init__(self):
        super(Karakter, self).__init_()
        pass
    def draw(self, screen):
        screen.blit(self.image,self.rect)
    def update(self, rintangan, musuh):
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
        if kena_rintangan:
            self.x, self.y = self.a, self.b
        else:
            self.a, self.b = self.rect[:2]
        if kena_musuh:
            main()
            

class Male(Karakter) :
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        img=pygame.image.load("Assets\Gambar\Man.png")
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

class Female(Karakter) :
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        img=pygame.image.load("Assets\Gambar\Girl.png")
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

class Button :
    def __init__(self,x,y,img,scale) :
        self.pos_x=x
        self.pos_y=y
        width = img.get_width()
        height = img.get_height()
        self.img= pygame.transform.scale(img, ((width*scale),(height*scale)))
        self.img_rect=self.img.get_rect(center=(self.pos_x,self.pos_y))
        self.clicked=False

    def draw (self) :
        pos = pygame.mouse.get_pos()
        if self.img_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                return True
        if not pygame.mouse.get_pressed()[0] and self.clicked:
            self.clicked = False
        return False
    def show(self, screen):
        screen.blit(self.img,self.img_rect) 
    def update_image(self, img):
        self.image = pygame.transform.scale(img,self.scale)

pygame.init()
Screen_WIDTH = 1000
Screen_HEIGHT = 650
WIN = pygame.display.set_mode((Screen_WIDTH,Screen_HEIGHT))
pygame.display.set_caption("Hunter and Guardian")
BG_main = pygame.image.load("Assets\Gambar\Background.png")
BG_main = pygame.transform.scale(BG_main, (1000, 650))
BG_karakter = pygame.image.load("Assets\Gambar\Bg_Karakter.png")
BG_karakter = pygame.transform.scale(BG_karakter,(1000, 650))
BG_info = pygame.image.load("Assets\Gambar\Bg_info.png")
BG_info = pygame.transform.scale(BG_info,(1000,650))
BG_map = pygame.image.load('Assets\Gambar\maps.png')
BG_map = pygame.transform.scale(BG_map, (1000,650))
karakter_pilihan=1
music = pygame.mixer.music.load('Assets\Audio\Sound Gameplay.mp3')
pygame.mixer.music.play(-1)
button_sound = mixer.Sound('Assets\Audio\Sound Button.wav')

icon = pygame.image.load("Assets\Gambar\Man.png")
pygame.display.set_icon(icon)

def karakter() :
    global karakter_pilihan
    male_button=Button(((Screen_WIDTH/2)-200),((Screen_HEIGHT/2)+100),img=pygame.image.load("Assets\Gambar\Hunter_Man.png"),scale=(0.5))
    female_button=Button(((Screen_WIDTH/2)+200),((Screen_HEIGHT/2)+100),img=pygame.image.load("Assets\Gambar\Hunter_Girl.png"),scale=(0.5))
    run = True
    while run :
        WIN.blit(BG_karakter, (0,0))
        male_button.show(WIN)
        female_button.show(WIN)
        if male_button.draw() :
            karakter_pilihan=1
            main()
        if female_button.draw() :
            karakter_pilihan=2
            main()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                sys.exit()
        pygame.display.update()

def info() :
    back_button=Button((90),(50),img=pygame.image.load("Assets\Gambar\Back.png"),scale=0.4)
    run = True
    while run :
        WIN.blit(BG_info, (0,0))
        back_button.show(WIN)
        if back_button.draw() :
            button_sound.play()
            main()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                sys.exit()
        pygame.display.update()

def pause():

    def message_to_screen(message, colour, size, pos):
        font = pygame.font.Font('freesansbold.ttf',size)
        text = font.render(message, True, colour)
        WIN.blit(text, (text.get_rect(center = pos)))

    paused = True
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        if paused:
            WIN.fill("orange")
            message_to_screen("Paused", (0, 0, 0), 30, (500, 325))
            message_to_screen("Press C to continue or Q to quit.", (0, 0, 0), 10, (500, 500))
            pygame.display.update()
            continue
        else:
            return 
        pygame.display.update()
        clock.tick(5)

def main() :
    run=True
    music = True
    start_button=Button(((Screen_WIDTH/2)-300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Assets\Gambar\Mulai.png"),scale=0.6)
    karakter_button=Button((Screen_WIDTH/2),((Screen_HEIGHT/2)+200),img=pygame.image.load("Assets\Gambar\Karakter.png"), scale=0.6)
    exit_button=Button(((Screen_WIDTH/2)+300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Assets\Gambar\Exit.png"), scale=0.6)
    info_button=Button((Screen_WIDTH-50),(Screen_HEIGHT-50),img=pygame.image.load("Assets\Gambar\Info.png"), scale=0.5)
    on_button=Button(50,(Screen_HEIGHT-50),img=pygame.image.load("Assets\Gambar\Audio.png"), scale=0.5)
    off_button=Button(50,(Screen_HEIGHT-50),img=pygame.image.load("Assets\Gambar\off.png"), scale=0.15)
    while run :
        WIN.blit(BG_main,(0,0))
        start_button.show(WIN)
        karakter_button.show(WIN)
        exit_button.show(WIN)
        info_button.show(WIN)
        if music:
            on_button.show(WIN)
        else:
            off_button.show(WIN)
        if start_button.draw() :
            button_sound.play()
            play()
        if karakter_button.draw() :
            button_sound.play()
            karakter()
        if exit_button.draw() :
            button_sound.play()
            run=False
        if info_button.draw() :
            button_sound.play()
            info()
        if music:
            if on_button.draw():
                music = False
        else:
            if off_button.draw():
                music = True
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        pygame.display.update()
    pygame.quit()

def play() :
    halangan=Maps()
    musuh=pygame.sprite.Group()
    musuh.add(Guardian(905,56),Guardian(891,517),Guardian(57,53),Guardian(73,516))
    clock=pygame.time.Clock()
    if (karakter_pilihan==1) :
        player = Male((Screen_WIDTH/2),(Screen_HEIGHT/2))
    elif (karakter_pilihan==2) :
        player = Female((Screen_WIDTH/2),(Screen_HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0] == 1:
                print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = True
                if event.key == pygame.K_UP:
                    player.up_pressed = True
                if event.key == pygame.K_DOWN:
                    player.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = False
                if event.key == pygame.K_UP:
                    player.up_pressed = False
                if event.key == pygame.K_DOWN:
                    player.down_pressed = False
                if event.key == pygame.K_p:
                    pause()
        WIN.blit(BG_map,(0,0))
        player.draw(WIN)
        player.update(halangan.kotak,musuh)
        for i in musuh :
            i.draw(WIN)
        pygame.display.flip()
        clock.tick(30)

main()