import pygame
width=1200
height=600
screen=pygame.display.set_mode((width,height))
class Button():
    def __init__(self,image,font,text_input,pos,base_color,hover_color):
        self.image=image
        self.text_input=text_input
        self.pos_x=pos[0]
        self.pos_y=pos[1]
        self.font=font
        self.base_color=base_color
        self.hover_color=hover_color
        self.text=self.font.render(self.text_input,True,self.base_color)
        #If no image is provided then text is used instead
        if self.image is None:
            self.image=self.text
        
        self.rect=self.image.get_rect(center=(self.pos_x,self.pos_y),)
        self.text_rect=self.text.get_rect(center=(self.pos_x,self.pos_y))
        
    def update(self,position):
        #If the mouse clicks on the image rectangle 
        if self.image is not None:
            screen.blit(self.image,self.rect)
        #If the mouse clicks on the text rectangle 
        screen.blit(self.text,self.text_rect)
        
    def check_update(self,position):
        if self.rect.collidepoint(position):
            return True
        return False
    
    def change_color(self,position):
        if self.rect.collidepoint(position):
            self.text=self.font.render(self.text_input,True,self.hover_color)
        else:
            self.text=self.font.render(self.text_input,True,self.base_color)