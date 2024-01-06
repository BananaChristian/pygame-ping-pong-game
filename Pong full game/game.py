import pygame
from pygame import*
from button import Button
from objects import Paddle,Ball,ScoreBoard
import menu as menu

pygame.init()

width=1200
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Ping Pong')
clock=pygame.time.Clock()
FPS=60

def get_font(size):
    return pygame.font.Font('assets/sewer.ttf',size)

pad_r=Paddle(
    pos=(1100,300),
    pad_no=1,
    dy=5
)
pad_l=Paddle(
    pos=(100,300),
    pad_no=2,
    dy=5
)      
ball=Ball(
    dx=5,
    dy=5,
    pos=(width//2,height//2)
)

score=0     
Score_Board=ScoreBoard(
            pos=(600,50),
            text_input='Score : '+str(score),
            font=get_font(20),
            color=(255,255,255)
        )
def game():
    global score
    run=True
    while run:
        play_mouse_pos=pygame.mouse.get_pos()
        
        back_button=Button(
            image=pygame.image.load('assets/Play rect.png'),
            font=get_font(20),
            text_input='BACK',
            pos=(600,500),
            base_color='white',
            hover_color=(0,0,0)
        )
        
        #Event handlers
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if back_button.check_update(play_mouse_pos):
                    menu.main_menu()
                
        
        
        screen.fill((0,100,0))
        ball.draw()
        ball.update()
        back_button.change_color(play_mouse_pos)
        back_button.update(play_mouse_pos)
        
        for pad in [pad_l,pad_r]:
            pad.draw()
            pad.update()
            
        
        
        if ball.rect.colliderect(pad_l.rect):
            ball.dx=abs(ball.dx)
            score+=1
            
        if ball.rect.colliderect(pad_r):
            ball.dx=-abs(ball.dx)
            score+=1
        
        if ball.rect.right < pad_l.rect.left or ball.rect.left > pad_r.rect.right:
            ball.reset()
            score=0
            
        Score_Board.text_input='Score: ' + str(score)
        Score_Board.text = Score_Board.font.render(Score_Board.text_input, True, Score_Board.color)
        Score_Board.text_rect = Score_Board.text.get_rect(center=(Score_Board.pos_x, Score_Board.pos_y))
        
        clock.tick(FPS)    
        Score_Board.display(screen) 
        pygame.display.update()
        
if __name__=='__main__':
    game()