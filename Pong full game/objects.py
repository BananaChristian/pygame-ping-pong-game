import pygame

width=1200
height=600
screen=pygame.display.set_mode((width,height))

##############Paddle##################
class Paddle():
    def __init__(self,pos,pad_no,dy):
        self.pos_x=pos[0]
        self.pos_y=pos[1]
        self.pad_no=pad_no
        self.dy=dy
        self.pad=pygame.image.load('assets/paddle.png')
        self.rect=self.pad.get_rect(center=(self.pos_x,self.pos_y))
        
    def draw(self):
        self.rect=self.pad.get_rect(center=(self.pos_x,self.pos_y))
        screen.blit(self.pad,self.rect)
        
    def update(self):
        #Paddle borders
        if self.pos_y<100:
            self.pos_y=100
            
        if self.pos_y > height-100:
            self.pos_y = height-100
        
        keys=pygame.key.get_pressed()
        
        if self.pad_no==1:
            if keys[pygame.K_UP]:
                self.pos_y-=self.dy
                
            if keys[pygame.K_DOWN]:
                self.pos_y+=self.dy
                
        if self.pad_no==2:
            if keys[pygame.K_w]:
                self.pos_y-=self.dy
                
            if keys[pygame.K_s]:
                self.pos_y+=self.dy
                
###########Ball##############    
class Ball():
    def __init__(self,dx,dy,pos):
        super().__init__()
        self.dx=dx
        self.dy=dy
        self.pos_x=pos[0]
        self.pos_y=pos[1]
        self.ball=pygame.image.load('assets/Ball.png')
        self.rect=self.ball.get_rect(center=(self.pos_x,self.pos_y))
        
    def update(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        
        #Wall collisions
        if self.pos_x<=0 or self.pos_x>=width:
            self.dx=-self.dx
            
        if self.pos_y<=0 or self.pos_y>=height:
            self.dy=-self.dy
        
    def draw(self):
        self.rect=self.ball.get_rect(center=(self.pos_x,self.pos_y))
        screen.blit(self.ball,self.rect)
        
    def reset(self):
        self.pos_x=width//2
        self.pos_y=height//2
        self.dx=-self.dx
        
################Scoreboard############
class ScoreBoard():
    def __init__(self,pos,text_input,font,color):
        self.pos_x=pos[0]
        self.pos_y=pos[1]
        self.font=font
        self.text_input=text_input
        self.color=color
        self.text=self.font.render(self.text_input,True,self.color)
        self.text_rect=self.text.get_rect(center=(self.pos_x,self.pos_y))

    def display(self,screen):
        screen.blit(self.text,self.text_rect)
        