import sys
import pygame
from button import Button
import game as game

pygame.init()

width=1200
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Main menu')

def get_font(size):
    return pygame.font.Font('assets/sewer.ttf',size)

def main_menu():
    #menu_bg=pygame.image.load('assets/money bg.jfif')
    menu_text=get_font(100).render('PONG',True,(60,100,60))
    menu_rect=menu_text.get_rect(center=(600,100))
    
    while True:
        menu_mouse_pos=pygame.mouse.get_pos()
        screen.fill((0,100,0))
        screen.blit(menu_text,menu_rect)
        
        #Buttons
        play_button=Button(
            image=pygame.image.load('assets/Play rect.png'),
            text_input='PLAY',
            font=get_font(45),
            pos=(600,200),
            base_color=(255,255,255),
            hover_color=(0,0,0)
        )
        tutorial_button=Button(
            image=pygame.image.load('assets/Play rect.png'),
            font=get_font(45),
            text_input='TUTORIAL',
            pos=(600,300),
            base_color=(255,255,255),
            hover_color=(0,0,0)
        )
        quit_button=Button(
            image=pygame.image.load('assets/Play rect.png'),
            font=get_font(45),
            text_input='QUIT',
            pos=(600,400),
            base_color=(255,255,255),
            hover_color=(0,0,0)
        )
        
        #Event handlers
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if play_button.check_update(menu_mouse_pos):
                    play()
                if tutorial_button.check_update(menu_mouse_pos):
                    tutorial()
                if quit_button.check_update(menu_mouse_pos):
                    quit()
                    
        for button in [play_button,tutorial_button,quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)         
        pygame.display.update()
        
def play():
    game.game()
    
def tutorial():
    while True:
        tutorial_menu_pos=pygame.mouse.get_pos()
        
        back_button=Button(
            image=pygame.image.load('assets/Play rect.png'),
            font=get_font(45),
            text_input='BACK',
            pos=(600,500),
            base_color='white',
            hover_color=(0,0,0)
        )
        
        text=' w and s keys: move the left paddle up and down respectively,  up and down arrow keys:move the right paddle up and down'
        tutorial_text=get_font(20).render(text,True,(0,0,0))
        tutorial_rect=tutorial_text.get_rect(center=(600,300))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type==pygame.MOUSEBUTTONDOWN:
                if back_button.check_update(tutorial_menu_pos):
                    main_menu()
        
                    
        back_button.change_color(tutorial_menu_pos)  
        screen.blit(tutorial_text,tutorial_rect)          
        back_button.update(screen)
        
        pygame.display.update()
    
def quit():
    sys.exit()
    
if __name__ == '__main__':
    main_menu()        
        
        
        