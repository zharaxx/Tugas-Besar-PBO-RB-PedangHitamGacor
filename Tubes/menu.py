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
