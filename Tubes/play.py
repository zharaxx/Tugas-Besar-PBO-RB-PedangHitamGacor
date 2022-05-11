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