import pygame
import sys

import helpers as helper
from structs import GameState
from structs import Clothes
import constants as const



# initialize pygame
pygame.init()
pygame.font.init()


#game constants
FPS = 60  #fps

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#create screen
const.init_background()
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption("Peking Puppets")
const.init_images()
# Clock for controlling frame rate
clock = pygame.time.Clock()

def handle_events(game_state, color_picker):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close button
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            helper.hover_mouse(mouse_x, mouse_y, game_state)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            helper.click_mouse(mouse_x, mouse_y, game_state, color_picker)
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            #helper.motion_mouse(mouse_x, mouse_y, game_state)


def update(game_state):
    pass 

def draw(game_state):

    if not game_state.finalBG:
        screen.blit(const.BACKGROUND, (0,0))  # Clear the screen with a white background
        
        helper.draw_button(screen, game_state)
        screen.blit(color_picker, (const.COLOR_PICKER_X, const.COLOR_PICKER_Y))

    else:
        screen.blit(const.FINAL_BACKGROUND, (0,0))
    

    helper.draw_final_bg(screen, game_state)
    helper.draw_type(screen, game_state)
    helper.draw_doll(screen, game_state)
    helper.draw_clothes_on(screen, game_state)
    pygame.display.flip()

    

def main():
    clothes = Clothes()
    game_state = GameState(clothes)
    global color_picker
    color_picker = helper.generate_color_square(const.COLOR_PICKER_SIZE)

    while True:
        handle_events(game_state, color_picker)
        update(game_state)
        draw(game_state)
        clock.tick(FPS)
    


if __name__ == "__main__":
    main()
