import pygame
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
