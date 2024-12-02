import pygame
import sys

import constants as const
from structs import GameState
import colorsys

#DRAW FUNCTIONS

def generate_color_square(size):
    surface = pygame.Surface((size, size))
    for x in range(size):
        for y in range(size):
            hue = x / size  # X-axis: Hue (0-1)
            saturation = y / size  # Y-axis: Saturation (0-1)
            value = 1.0  # Full brightness
            # Convert HSV to RGB
            r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
            color = (int(r * 255), int(g * 255), int(b * 255))
            surface.set_at((x, y), color)
    return surface

# Function to get color from position
def get_color_from_position(surface, pos):
    if 0 <= pos[0] < surface.get_width() and 0 <= pos[1] < surface.get_height():
        color = surface.get_at(pos)  # Get the color as an RGBA tuple
        return color[:3]  # Return only the RGB values (ignore alpha)
    return None


def draw_final_bg(screen, game_state):
    #draw the label as a button for final background at top left
    label = const.LABEL_LIT if game_state.bgHov else const.LABEL_UNLIT
    screen.blit(label, (40, 40))

    text = const.TRAJANUS.render("change", True, const.GOLD)
    text_rect = text.get_rect(center=(40 + const.LABEL_WIDTH/2, 40 + const.LABEL_HEIGHT/2))
    screen.blit(text, text_rect)

def draw_type(screen, game_state):
    label = const.LABEL_LIT if game_state.typeHov else const.LABEL_UNLIT
    screen.blit(label, (60 + const.LABEL_WIDTH, 40))

    text = const.TRAJANUS.render("doll", True, const.GOLD)
    text_rect = text.get_rect(center=(60 + const.LABEL_WIDTH + const.LABEL_WIDTH/2, 40 + const.LABEL_HEIGHT/2))
    screen.blit(text, text_rect)
    
def draw_button(screen, game_state):
    #draw button on the furthest right of screen, in middle
    if game_state.closetOn:
        draw_closet(screen, game_state)
        return
    else:
        button = const.BUTTON_LIT if game_state.closetHov else const.BUTTON_UNLIT
    
    screen.blit(button, (const.SCREEN_WIDTH - const.BUTTON_WIDTH - 40, 
                         const.SCREEN_HEIGHT/2-const.BUTTON_HEIGHT/2))

def draw_label(screen, i, game_state):
    #draw labels over cabinet, spaced out evenly
    label = const.LABEL_LIT if game_state.currCategory == const.CATEGORIES[i] else const.LABEL_UNLIT
    screen.blit(label, (const.SCREEN_WIDTH - const.LABEL_WIDTH*4 + i*const.LABEL_WIDTH,
                              const.SCREEN_HEIGHT/6 - const.LABEL_HEIGHT/2))
    label = const.CATEGORIES[i]
    text = const.TRAJANUS.render(label, True, const.GOLD)
    text_chinese = const.CHINESE.render(const.CATEGORIES_CHINESE[i], True, const.GOLD)
    text_rect = text.get_rect(center=(const.SCREEN_WIDTH - const.LABEL_WIDTH*3.5 + i*const.LABEL_WIDTH,
                                    const.SCREEN_HEIGHT/6 - 8))
    text_rect_chinese = text_chinese.get_rect(center=
                                (const.SCREEN_WIDTH - const.LABEL_WIDTH*3.5 + i*const.LABEL_WIDTH,
                                const.SCREEN_HEIGHT/6 + 8))
    #draw text centered over each label
    screen.blit(text, text_rect)
    screen.blit(text_chinese, text_rect_chinese)
def draw_clothes(screen, clothes_dict, game_state):
    i = 0
    for key in clothes_dict.keys():
        #draw clothes in cabinet
        #draw label two per row in cabinet in center of cabinet with space in between labels
        screen.blit(const.SMALL_LABEL, (const.SCREEN_WIDTH - const.CABINET_WIDTH - 40 + 65 + const.SMALL_LABEL_WIDTH*(i%2) + 20*(i%2),
                                const.SCREEN_HEIGHT/2 - const.CABINET_HEIGHT/2 + 100 + const.SMALL_LABEL_HEIGHT*(i//2) + 20 * (i//2)))


        label = key
        text = const.TRAJANUS.render(label, True, const.GOLD)
        #put text in middle of small_label
        text_rect = text.get_rect(center=(const.SCREEN_WIDTH - const.CABINET_WIDTH - 40 + 65 + const.SMALL_LABEL_WIDTH*(i%2) + 20*(i%2) + const.SMALL_LABEL_WIDTH/2,
                                        const.SCREEN_HEIGHT/2 - const.CABINET_HEIGHT/2 + 100 + const.SMALL_LABEL_HEIGHT*(i//2) + 20 * (i//2) + const.SMALL_LABEL_HEIGHT/2))

        screen.blit(text, text_rect)
        i+=1

def draw_closet(screen, game_state):
    #draw cabinet
    screen.blit(const.CABINET, (const.SCREEN_WIDTH - const.CABINET_WIDTH - 40, 
                          const.SCREEN_HEIGHT/2 - const.CABINET_HEIGHT/2))

    #draw labels
    for i in range(len(const.CATEGORIES)):
        draw_label(screen, i, game_state)

    #draw x button
    x = const.X_LIT if game_state.xHov else const.X_UNLIT
    screen.blit(x, (const.SCREEN_WIDTH - const.X_WIDTH - 40, const.SCREEN_HEIGHT/2 - const.CABINET_HEIGHT/2))
    
    #draw buttons
    clothes_dict = const.CATEGORY_DICT[game_state.currCategory]
    draw_clothes(screen, clothes_dict, game_state)


def draw_doll(screen, game_state):
    doll = const.GIRL if game_state.doll else const.BOY
    if not game_state.finalBG:
    #draw doll in middle of screen
        screen.blit(doll, 
                    (const.SCREEN_WIDTH/2 - const.GIRL_WIDTH/2+20, const.SCREEN_HEIGHT/2 - const.GIRL_HEIGHT/2+20))
    else:
        screen.blit(doll, (const.SCREEN_WIDTH/2 - const.GIRL_WIDTH/2, const.SCREEN_HEIGHT/2 - const.GIRL_HEIGHT/2 + 80))
def draw_clothes_on(screen, game_state):
    #draw whatever clothes are not None at the coordinates specified in clothes_positions
    #add positions to list in clothes class
    x = 0
    y = 0
    y2 = 0
    if game_state.finalBG:
        x = -20
        y = 60
    if not game_state.doll:
        y2 = -20
    if game_state.clothes.bottom:
        bottom = const.BOTTOMS[game_state.clothes.bottom].copy()
        value = game_state.clothes.bottomColor + (250,)
        bottom.fill(value, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(bottom,
        #screen.blit(BOTTOMS[game_state.clothes.bottom], 
                    (524+x, 295+y+y2))
    
    if game_state.clothes.top:
        top = const.TOPS[game_state.clothes.top].copy()
        value = game_state.clothes.topColor + (250,)
        top.fill(value, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(top, 
                    (527+x, 218+y+y2))
                    #game_state.clothes.clothes_positions["tops"])
    
    if game_state.clothes.dress:
        dress = const.DRESSES[game_state.clothes.dress].copy()
        value = game_state.clothes.dressColor + (250,)
        dress.fill(value, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(dress,
        #screen.blit(const.DRESSES[game_state.clothes.dress], 
                    (512+x,217+y+y2))
    if game_state.clothes.accessory:
        accessory = const.ACCESSORIES[game_state.clothes.accessory].copy()
        value = game_state.clothes.accessoryColor + (250,)
        accessory.fill(value, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(accessory,
        #screen.blit(const.ACCESSORIES[game_state.clothes.accessory], 
                    (567+x,274+y+y2))




#MOUSE FUNCTIONS
def overCloset(mouse_x, mouse_y):
    button_x = const.SCREEN_WIDTH - const.BUTTON_WIDTH - 40
    button_y = const.SCREEN_HEIGHT/2 - const.BUTTON_HEIGHT/2

    button_rect = pygame.Rect(button_x, button_y, const.BUTTON_WIDTH, const.BUTTON_HEIGHT)

    if button_rect.collidepoint(mouse_x, mouse_y):
        return True
    return False

def overLabel(mouse_x, mouse_y):
    for i in range(len(const.CATEGORIES)):
        label_x = const.SCREEN_WIDTH - const.LABEL_WIDTH*4 + i*const.LABEL_WIDTH
        label_y = const.SCREEN_HEIGHT/6 - const.LABEL_HEIGHT/2


        label_rect = pygame.Rect(label_x, label_y, const.LABEL_WIDTH, const.LABEL_HEIGHT)

        if label_rect.collidepoint(mouse_x, mouse_y):
            return i
    return -1

def overX(mouse_x, mouse_y):
    x_x = const.SCREEN_WIDTH - const.X_WIDTH - 40
    x_y = const.SCREEN_HEIGHT/2 - const.CABINET_HEIGHT/2

    x_rect = pygame.Rect(x_x, x_y, const.X_WIDTH, const.X_HEIGHT)

    if x_rect.collidepoint(mouse_x, mouse_y):
        return True
    return False

def overClothes(mouse_x, mouse_y, game_state):
    clothes_dict = const.CATEGORY_DICT[game_state.currCategory]
    i = 0
    for key in clothes_dict.keys():
        #draw clothes in cabinet
        #draw label two per row in cabinet in center of cabinet with space in between labels
        label_x = const.SCREEN_WIDTH - const.CABINET_WIDTH - 40 + 65 + const.SMALL_LABEL_WIDTH*(i%2) + 20*(i%2)
        label_y = const.SCREEN_HEIGHT/2 - const.CABINET_HEIGHT/2 + 100 + const.SMALL_LABEL_HEIGHT*(i//2) + 20 * (i//2)
        label_rect = pygame.Rect(label_x, label_y, const.SMALL_LABEL_WIDTH, const.SMALL_LABEL_HEIGHT)
        if label_rect.collidepoint(mouse_x, mouse_y):
            return key
        i+=1
    return None

def overFinalBG(mouse_x, mouse_y, game_state):
    label_x = 40
    label_y = 40
    label_rect = pygame.Rect(label_x, label_y, const.LABEL_WIDTH, const.LABEL_HEIGHT)
    if label_rect.collidepoint(mouse_x, mouse_y):
        return True
    return False

def overDoll(mouse_x, mouse_y, game_state):
    #check items in clothes position list to see if mouse is over them
    for key in game_state.clothes.clothes_positions.keys():
        x, y = game_state.clothes.clothes_positions[key]
        if x < mouse_x < x + 100 and y < mouse_y < y + 100:
            return True, key
    return False, None

def overType(mouse_x, mouse_y, game_state):
    label_x = 60 + const.LABEL_WIDTH
    label_y = 40
    label_rect = pygame.Rect(label_x, label_y, const.LABEL_WIDTH, const.LABEL_HEIGHT)
    if label_rect.collidepoint(mouse_x, mouse_y):
        return True
    return False

def overColorPicker(mouse_x, mouse_y, game_state, color_picker):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Check if click is within the color picker
    if 50 <= mouse_x < 50 + const.COLOR_PICKER_SIZE and 200 <= mouse_y < 200 + const.COLOR_PICKER_SIZE:
        selected_color = get_color_from_position(color_picker, (mouse_x - 50, mouse_y - 200))
    else:
        return None
    return selected_color
def click_mouse(mouse_x, mouse_y, game_state, color_picker):
    if overCloset(mouse_x, mouse_y):
        if not game_state.closetOn:
            game_state.closetOn = not game_state.closetOn
        else:
            #check for on options
            pass
    i = overLabel(mouse_x, mouse_y)
    if i != -1:
        game_state.currCategory = const.CATEGORIES[i]
    
    if overX(mouse_x, mouse_y):
        game_state.closetOn = False
    
    key = overClothes(mouse_x, mouse_y, game_state)
    if key:
        if game_state.currCategory == "tops":
            if game_state.clothes.top == key:
                game_state.clothes.top = None
            else:
                game_state.clothes.top = key
        elif game_state.currCategory == "bottoms":
            if game_state.clothes.bottom == key:
                game_state.clothes.bottom = None
            else:
                game_state.clothes.bottom = key
        elif game_state.currCategory == "dresses":
            if game_state.clothes.dress == key:
                game_state.clothes.dress = None
            else:
                game_state.clothes.dress = key
        elif game_state.currCategory == "accessories":
            if game_state.clothes.accessory == key:
                game_state.clothes.accessory = None
            else:
                game_state.clothes.accessory = key
    if overFinalBG(mouse_x, mouse_y, game_state):
        game_state.finalBG = not game_state.finalBG

    valid, key = overDoll(mouse_x, mouse_y, game_state)
    if valid:
        if game_state.selectedItem == key:
            game_state.selectedItem = None
            print(game_state.clothes.clothes_positions[key])
        else:
            game_state.selectedItem = key
    
    if overType(mouse_x, mouse_y, game_state):
        game_state.doll = not game_state.doll
    
    selected_color = overColorPicker(mouse_x, mouse_y, game_state, color_picker)
    if(selected_color):
        if(game_state.currCategory == "tops"):
            game_state.clothes.topColor = selected_color
        elif(game_state.currCategory == "bottoms"):
            game_state.clothes.bottomColor = selected_color
        elif(game_state.currCategory == "dresses"):
            game_state.clothes.dressColor = selected_color
        elif(game_state.currCategory == "accessories"):
            game_state.clothes.accessoryColor = selected_color

    
def hover_mouse(mouse_x, mouse_y, game_state):
    if overCloset(mouse_x, mouse_y):
        game_state.closetHov = True
    elif overX(mouse_x, mouse_y):
        game_state.xHov = True
    elif overFinalBG(mouse_x, mouse_y, game_state):
        game_state.bgHov = True
    elif overType(mouse_x, mouse_y, game_state):
        game_state.typeHov = True
    else:
        game_state.closetHov = False
        game_state.xHov = False
        game_state.bgHov = False
        game_state.typeHov = False
    

def motion_mouse(mouse_x, mouse_y, game_state):
    valid, key = overDoll(mouse_x, mouse_y, game_state)
    if valid:
        if key == game_state.selectedItem:
            game_state.clothes.clothes_positions[key] = (mouse_x-50, mouse_y-50)