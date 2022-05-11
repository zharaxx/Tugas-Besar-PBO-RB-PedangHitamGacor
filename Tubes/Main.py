import pygame,sys
from pygame import mixer

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

class Button :
    def __init__(self,x,y,img,scale) :
        self.pos_x=x
        self.pos_y=y
        width = img.get_width()
        height = img.get_height()
        self.img= pygame.transform.scale(img, ((width*scale),(height*scale)))
        self.img_rect=self.img.get_rect(center=(self.pos_x,self.pos_y))
        self.clicked=False

    def draw (self,screen) :
        action=False
        pos = pygame.mouse.get_pos()
        if self.img_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.img,self.img_rect) 
        return action
    
    def update_image(self, img):
        self.image = pygame.transform.scale(img,self.scale)

pygame.init()
Screen_WIDTH = 1000
Screen_HEIGHT = 650
WIN = pygame.display.set_mode((Screen_WIDTH,Screen_HEIGHT))
pygame.display.set_caption("Hunter and Guardian")
BG_main = pygame.image.load("Background.png")
BG_main = pygame.transform.scale(BG_main, (1000, 650))
BG_karakter = pygame.image.load("Bg_Karakter.png")
BG_karakter = pygame.transform.scale(BG_karakter,(1000, 650))
BG_info = pygame.image.load("Bg_info.png")
BG_info = pygame.transform.scale(BG_info,(1000,650))
karakter_pilihan=1
music = pygame.mixer.music.load('Sound Gameplay.mp3')
pygame.mixer.music.play(-1)
button_sound = mixer.Sound('Sound Button.wav')

icon = pygame.image.load("sword.png")
pygame.display.set_icon(icon)

#on = pygame.image.load("on.png")
#off = pygame.image.load("off.png")
#sound_btn=Button(50,(Screen_HEIGHT-50), scale=0.15)

#sound_on = True

#running = True
#while running:
    #if sound_btn.draw(WIN):
        #sound_on = not sound_on
        #if sound_on:
            #sound_btn.update_image(on)
        #else:
            #sound_btn.update_image(off)

def karakter() :
    global karakter_pilihan
    run = True
    while run :
        WIN.blit(BG_karakter, (0,0))
        male_button=Button(((Screen_WIDTH/2)-200),((Screen_HEIGHT/2)+100),img=pygame.image.load("Hunter_Man.png"),scale=(0.5))
        if male_button.draw(WIN) :
            karakter_pilihan=1
            main()
        female_button=Button(((Screen_WIDTH/2)+200),((Screen_HEIGHT/2)+100),img=pygame.image.load("Hunter_Girl.png"),scale=(0.5))
        if female_button.draw(WIN) :
            karakter_pilihan=2
            main()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.quit()

def info() :
    run = True
    while run :
        WIN.blit(BG_info, (0,0))
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.quit()

def main() :
    run=True
    while run :
        WIN.blit(BG_main,(0,0))
        start_button=Button(((Screen_WIDTH/2)-300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Mulai.png"),scale=0.6)
        if start_button.draw(WIN) :
            button_sound.play()
            play()
        karakter_button=Button((Screen_WIDTH/2),((Screen_HEIGHT/2)+200),img=pygame.image.load("Karakter.png"), scale=0.6)
        if karakter_button.draw(WIN) :
            button_sound.play()
            karakter()
        exit_button=Button(((Screen_WIDTH/2)+300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Exit.png"), scale=0.6)
        if exit_button.draw(WIN) :
            button_sound.play()
            run=False
        info_button=Button((Screen_WIDTH-50),(Screen_HEIGHT-50),img=pygame.image.load("Info.png"), scale=0.5)
        if info_button.draw(WIN) :
            button_sound.play()
            info()
        on_button=Button(50,(Screen_HEIGHT-50),img=pygame.image.load("audio.png"), scale=0.5)
        if on_button.draw(WIN) :
            button_sound.play()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        pygame.display.update()
    pygame.quit()

def play() :
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
        
        WIN.fill("black")  
        player.draw(WIN)
        player.update()
        pygame.display.flip()
        clock.tick(120)

main()