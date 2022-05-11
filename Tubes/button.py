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