import pygame
from Coin import coin
from Guardian import Guardian
from Maps import Maps
from Guardian import Guardian
from Button import Button
import Path

pygame.init()
Screen_WIDTH = 1000
Screen_HEIGHT = 650
font=pygame.font.Font('freesansbold.ttf',30)
WIN = pygame.display.set_mode((Screen_WIDTH,Screen_HEIGHT))
pygame.display.set_caption("Hunter and Guardian")

def karakter() :
    male_button=Button(((Screen_WIDTH/2)-200),((Screen_HEIGHT/2)+100),img=pygame.image.load("Assets/Gambar/Hunter_Man.png"),scale=(0.5))
    female_button=Button(((Screen_WIDTH/2)+200),((Screen_HEIGHT/2)+100),img=pygame.image.load("Assets/Gambar/Hunter_Girl.png"),scale=(0.5))
    run = True
    while run :
        WIN.blit(Path.BG_karakter, (0,0))
        male_button.show(WIN)
        female_button.show(WIN)
        if male_button.draw() :
            Path.karakter_pilihan=1
            Path.button_sound.play()
            main()
        if female_button.draw() :
            Path.karakter_pilihan=2
            Path.button_sound.play()
            main()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        pygame.display.update()

def info() :
    back_button=Button((90),(50),img=pygame.image.load("Assets/Gambar/Back.png"),scale=0.4)
    run = True
    while run :
        WIN.blit(Path.BG_info, (0,0))
        back_button.show(WIN)
        if back_button.draw() :
            Path.button_sound.play()
            main()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
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
            message_to_screen("Press P to continue or Q to quit.", (0, 0, 0), 10, (500, 500))
            pygame.display.update()
            continue
        else:
            return

def main() :
    run=True
    music = True
    start_button=Button(((Screen_WIDTH/2)-300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Assets/Gambar/Mulai.png"),scale=0.6)
    karakter_button=Button((Screen_WIDTH/2),((Screen_HEIGHT/2)+200),img=pygame.image.load("Assets/Gambar/Karakter.png"), scale=0.6)
    exit_button=Button(((Screen_WIDTH/2)+300),((Screen_HEIGHT/2)+200),img=pygame.image.load("Assets/Gambar/Exit.png"), scale=0.6)
    info_button=Button((Screen_WIDTH-50),(Screen_HEIGHT-50),img=pygame.image.load("Assets/Gambar/info.png"), scale=0.5)
    on_button=Button(50,(Screen_HEIGHT-50),img=pygame.image.load("Assets/Gambar/Audio.png"), scale=0.5)
    off_button=Button(50,(Screen_HEIGHT-50),img=pygame.image.load("Assets/Gambar/off.png"), scale=0.15)
    while run :
        WIN.blit(Path.BG_main,(0,0))
        start_button.show(WIN)
        karakter_button.show(WIN)
        exit_button.show(WIN)
        info_button.show(WIN)
        if music:
            on_button.show(WIN)
        else:
            off_button.show(WIN)
        if start_button.draw() :
            Path.button_sound.play()
            play()
        if karakter_button.draw() :
            Path.button_sound.play()
            karakter()
        if exit_button.draw() :
            Path.button_sound.play()
            run=False
        if info_button.draw() :
            Path.button_sound.play()
            info()
        if music:
            if on_button.draw():
                pygame.mixer.music.stop()
                music = False
        else:
            if off_button.draw():
                pygame.mixer.music.play(-1)
                music = True
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        pygame.display.update()
    pygame.quit()

def play() :
    from Male import Male
    from Female import Female
    time = pygame.USEREVENT + 1
    waktu = 0
    halangan=Maps()
    musuh=pygame.sprite.Group()
    musuh.add(Guardian(905,56),Guardian(891,517),Guardian(57,53),Guardian(73,516))
    clock=pygame.time.Clock()
    koin=pygame.sprite.Group()
    koin.add(coin())
    potion=pygame.sprite.Group()
    if (Path.karakter_pilihan==1) :
        player = Male((Screen_WIDTH/2),(Screen_HEIGHT/2))
    elif (Path.karakter_pilihan==2) :
        player = Female((Screen_WIDTH/2),(Screen_HEIGHT/2))
    pygame.time.set_timer(time, 1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == time:
                waktu+=1
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
        WIN.blit(Path.BG_map,(0,0))
        teks_score = font.render(f"Skor : {player.score}",True,(255,255,255))
        teks_waktu = font.render(f"Waktu : {waktu}",True,(255,255,255))
        WIN.blit(teks_score,(750,600))
        WIN.blit(teks_waktu,(50,600))
        player.draw(WIN)
        player.update(halangan.kotak,musuh,koin,potion,waktu)
        musuh.update(halangan.kotak, player)
        for i in koin :
            i.draw(WIN,player,koin)
        for i in potion :
            i.draw(WIN,player,musuh)
        for i in musuh :
            i.draw(WIN)
        pygame.display.flip()
        clock.tick(30)

def dead() :
    run = True
    back_button=Button((100),(Screen_HEIGHT-50),img=pygame.image.load("Assets/Gambar/Back.png"),scale=0.5)
    playagain_button=Button((Screen_WIDTH-100),(Screen_HEIGHT-50),img=pygame.image.load("Assets/Gambar/play again.png"),scale=0.5)
    Path.dead_sound.play()
    while run :
        WIN.blit(Path.BG_dead, (0,0))
        back_button.show(WIN)
        playagain_button.show(WIN)
        if back_button.draw() :
            main()
        if playagain_button.draw() :
            play()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
            teks_skor = font.render(f"Skor : {Path.skor}",True,(255,255,255))
            WIN.blit(teks_skor,(450,475))
            pygame.display.update()

if __name__ == "__main__":
    main()