import pygame,sys

pygame.init()
Screen_WIDTH = 1000
Screen_HEIGHT = 650
WIN = pygame.display.set_mode((Screen_WIDTH,Screen_HEIGHT))
pygame.display.set_caption("Hunter and Guardian")
BG_main = pygame.image.load("Background.png")
BG_main = pygame.transform.scale(BG_main, (1000, 650))
BG_karakter = pygame.image.load("Bg_Karakter.png")
BG_karakter = pygame.transform.scale(BG_karakter,(1000, 650))
karakter_pilihan=1

#Music
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

def main() :
    run=True
    while run :
        WIN.blit(BG_main,(0,0))
        start_button=Button(((Screen_WIDTH/2)-300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Mulai.png"),scale=0.6)
        if start_button.draw(WIN) :
            play()
        karakter_button=Button((Screen_WIDTH/2),((Screen_HEIGHT/2)+200),img=pygame.image.load("Karakter.png"), scale=0.6)
        if karakter_button.draw(WIN) :
            karakter()
        exit_button=Button(((Screen_WIDTH/2)+300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Exit.png"), scale=0.6)
        if exit_button.draw(WIN) :
            run=False
        info_button=Button((Screen_WIDTH-50),(Screen_HEIGHT-50),img=pygame.image.load("Info.png"), scale=0.5)
        info_button.draw(WIN)
        sound_button=Button(50,(Screen_HEIGHT-50),img=pygame.image.load("Audio.png"), scale=0.5)
        sound_button.draw(WIN)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        pygame.display.update()
    pygame.quit()
