from PIL import Image, ImageDraw
import pygame
import sys

pygame.font.init()
pygame.init()
#IMAGES
def init_background():
    global BACKGROUND, BACKGROUND_WIDTH, BACKGROUND_HEIGHT
    global FINAL_BACKGROUND
    global SCREEN_WIDTH, SCREEN_HEIGHT

    BACKGROUND = Image.open("images/background.jpg")
    BACKGROUND_WIDTH = BACKGROUND.size[0]
    BACKGROUND_HEIGHT = BACKGROUND.size[1]

    BACKGROUND = pygame.image.load("images/background.jpg")
    BACKGROUND = pygame.transform.scale(BACKGROUND, (BACKGROUND_WIDTH*1.4,  
                                                        BACKGROUND_HEIGHT*1.4))

    FINAL_BACKGROUND = pygame.image.load("images/final_background.jpg")
    FINAL_BACKGROUND = pygame.transform.scale(FINAL_BACKGROUND, (BACKGROUND_WIDTH*1.4,
                                            BACKGROUND_HEIGHT*1.4))
    
    #GAME CONSTANTS
    SCREEN_WIDTH = BACKGROUND_WIDTH * 1.4
    SCREEN_HEIGHT = BACKGROUND_HEIGHT * 1.4


def init_images():
    global COLOR_PICKER_SIZE
    global COLOR_PICKER_X, COLOR_PICKER_Y
    global BUTTON, BUTTON_WIDTH, BUTTON_HEIGHT
    global BUTTON_UNLIT, BUTTON_LIT
    global CABINET, CABINET_WIDTH, CABINET_HEIGHT
    global LABEL, LABEL_WIDTH, LABEL_HEIGHT
    global LABEL_UNLIT, LABEL_LIT
    global SMALL_LABEL, SMALL_LABEL_WIDTH, SMALL_LABEL_HEIGHT
    global X, X_WIDTH, X_HEIGHT
    global X_UNLIT, X_LIT
    global GIRL, GIRL_WIDTH, GIRL_HEIGHT
    global BOY, BOY_WIDTH, BOY_HEIGHT
    global TOP, TOP_WIDTH, TOP_HEIGHT
    global TOP1, TOP2, TOP3, TOP4
    global BOTTOM, BOTTOM_WIDTH, BOTTOM_HEIGHT
    global BOTTOM1, BOTTOM2, BOTTOM3
    global DRESS, DRESS_WIDTH, DRESS_HEIGHT
    global DRESS1, DRESS2, DRESS3, DRESS4
    global FAN, FAN_WIDTH, FAN_HEIGHT
    global SWORD, SWORD_WIDTH, SWORD_HEIGHT
    global FAN1, SWORD1
    global ACCESSORIES
    global CHINESE, PAPYRUS, TRAJANUS
    global DARK_BROWN, GOLD
    global CATEGORIES, CATEGORIES_CHINESE
    global CATEGORY_DICT
    global BOTTOMS, DRESSES, TOPS, ACCESSORIES
    
    COLOR_PICKER_SIZE = 250
    COLOR_PICKER_X = 50
    COLOR_PICKER_Y = 200
    BUTTON = Image.open("images/button_unlit.png")
    BUTTON_WIDTH = BUTTON.size[0]
    BUTTON_HEIGHT = BUTTON.size[1]

    BUTTON_UNLIT = pygame.image.load("images/button_unlit.png")
    BUTTON_UNLIT = pygame.transform.scale(BUTTON_UNLIT, 
                                    (BUTTON_WIDTH*0.5, BUTTON_HEIGHT*0.5))
    BUTTON_LIT = pygame.image.load("images/button_lit.png")
    BUTTON_LIT = pygame.transform.scale(BUTTON_LIT, 
                                    (BUTTON_WIDTH*0.5, BUTTON_HEIGHT*0.5))
    BUTTON_WIDTH = BUTTON_WIDTH * 0.5
    BUTTON_HEIGHT = BUTTON_HEIGHT * 0.5

    CABINET = Image.open("images/cabinet.png")
    CABINET_WIDTH = CABINET.size[0]
    CABINET_HEIGHT = CABINET.size[1]
    CABINET = pygame.image.load("images/cabinet.png")
    CABINET = pygame.transform.scale(CABINET, 
                                    (CABINET_WIDTH*0.65, CABINET_HEIGHT*0.65))
    CABINET_WIDTH = CABINET_WIDTH * 0.65
    CABINET_HEIGHT = CABINET_HEIGHT * 0.65

    LABEL = Image.open("images/label_unlit.png")
    LABEL_WIDTH = LABEL.size[0]
    LABEL_HEIGHT = LABEL.size[1]
    LABEL_UNLIT = pygame.image.load("images/label_unlit.png")
    LABEL_UNLIT = pygame.transform.scale(LABEL_UNLIT, 
                                    (LABEL_WIDTH*0.25, LABEL_HEIGHT*0.25))
    LABEL_LIT = pygame.image.load("images/label_lit.png")
    LABEL_LIT = pygame.transform.scale(LABEL_LIT, 
                                    (LABEL_WIDTH*0.25, LABEL_HEIGHT*0.25))
    LABEL_WIDTH = LABEL_WIDTH * 0.25
    LABEL_HEIGHT = LABEL_HEIGHT * 0.25

    SMALL_LABEL = pygame.transform.scale(LABEL_UNLIT,
                                        (LABEL_WIDTH*0.8, LABEL_HEIGHT*0.8))
    SMALL_LABEL_WIDTH = LABEL_WIDTH * 0.8
    SMALL_LABEL_HEIGHT = LABEL_HEIGHT * 0.8
    X = Image.open("images/x_unlit.png")
    X_WIDTH = X.size[0]
    X_HEIGHT = X.size[1]
    X_UNLIT = pygame.image.load("images/x_unlit.png")
    X_UNLIT = pygame.transform.scale(X_UNLIT, 
                                    (X_WIDTH*0.5, X_HEIGHT*0.5))
    X_LIT = pygame.image.load("images/x_lit.png")
    X_LIT = pygame.transform.scale(X_LIT, 
                                    (X_WIDTH*0.5, X_HEIGHT*0.5))
    X_WIDTH = X_WIDTH * 0.5
    X_HEIGHT = X_HEIGHT * 0.5

    GIRL = Image.open("images/girl.png")
    GIRL_WIDTH = GIRL.size[0]
    GIRL_HEIGHT = GIRL.size[1]
    GIRL = pygame.image.load("images/girl.png")
    GIRL = pygame.transform.scale(GIRL, (GIRL_WIDTH*0.40, GIRL_HEIGHT*0.40))
    GIRL_WIDTH = GIRL_WIDTH * 0.40
    GIRL_HEIGHT = GIRL_HEIGHT * 0.40
    BOY = pygame.image.load("images/boy.png")
    BOY = pygame.transform.scale(BOY, (GIRL_WIDTH, GIRL_HEIGHT))

    TOP = Image.open("images/clothes/tops/top1.png")
    TOP_WIDTH = TOP.size[0]
    TOP_HEIGHT = TOP.size[1]
    TOP1 = pygame.image.load("images/clothes/tops/top1.png").convert_alpha()
    TOP1 = pygame.transform.scale(TOP1, (TOP_WIDTH*0.8, TOP_HEIGHT*0.8))
    TOP_WIDTH = TOP_WIDTH * 0.8
    TOP_HEIGHT = TOP_HEIGHT * 0.8
    TOP2 = pygame.image.load("images/clothes/tops/top3.png").convert_alpha()
    TOP2 = pygame.transform.scale(TOP2, (TOP_WIDTH, TOP_HEIGHT))

    TOPS = {"top 1" : TOP1, "top 2" : TOP2}

    BOTTOM = Image.open("images/clothes/bottoms/bottom1.png")
    BOTTOM_WIDTH = BOTTOM.size[0]
    BOTTOM_HEIGHT = BOTTOM.size[1]
    BOTTOM1 = pygame.image.load("images/clothes/bottoms/bottom1.png").convert_alpha()
    BOTTOM1 = pygame.transform.scale(BOTTOM1, (BOTTOM_WIDTH*0.9, BOTTOM_HEIGHT*0.9))
    BOTTOM_WIDTH = BOTTOM_WIDTH*0.9
    BOTTOM_HEIGHT = BOTTOM_HEIGHT*0.9
    BOTTOM2 = pygame.image.load("images/clothes/bottoms/bottom2.png").convert_alpha()
    BOTTOM2 = pygame.transform.scale(BOTTOM2, (BOTTOM_WIDTH, BOTTOM_HEIGHT))
    BOTTOM3 = pygame.image.load("images/clothes/bottoms/bottom3.png").convert_alpha()
    BOTTOM3 = pygame.transform.scale(BOTTOM3, (BOTTOM_WIDTH, BOTTOM_HEIGHT))

    BOTTOMS = {"bottom 1" : BOTTOM1, "bottom 2" : BOTTOM2, "bottom 3" : BOTTOM3}

    DRESS = Image.open("images/clothes/dresses/dress1.png")
    DRESS_WIDTH = DRESS.size[0]
    DRESS_HEIGHT = DRESS.size[1]
    DRESS1 = pygame.image.load("images/clothes/dresses/dress1.png").convert_alpha()
    DRESS1 = pygame.transform.scale(DRESS1, (DRESS_WIDTH*0.5, DRESS_HEIGHT*0.5))
    DRESS_WIDTH = DRESS_WIDTH * 0.5
    DRESS_HEIGHT = DRESS_HEIGHT * 0.5

    DRESS2 = pygame.image.load("images/clothes/dresses/dress2.png").convert_alpha()
    DRESS2 = pygame.transform.scale(DRESS2, (DRESS_WIDTH, DRESS_HEIGHT))

    DRESS3 = pygame.image.load("images/clothes/dresses/dress3.png").convert_alpha()
    DRESS3 = pygame.transform.scale(DRESS3, (DRESS_WIDTH, DRESS_HEIGHT))
    DRESS4 = pygame.image.load("images/clothes/dresses/dress4.png").convert_alpha()
    DRESS4 = pygame.transform.scale(DRESS4, (DRESS_WIDTH, DRESS_HEIGHT))

    DRESSES = {"dress 1" : DRESS1, "dress 2" : DRESS2, "dress 3" : DRESS3, 
                "dress 4" : DRESS4}

    FAN = Image.open("images/clothes/accessories/fan.png")
    FAN_WIDTH = FAN.size[0]
    FAN_HEIGHT = FAN.size[1]
    FAN = pygame.image.load("images/clothes/accessories/fan.png").convert_alpha()
    FAN = pygame.transform.scale(FAN, (FAN_WIDTH*0.4, FAN_HEIGHT*0.4))
    FAN_WIDTH = FAN_WIDTH * 0.4
    FAN_HEIGHT = FAN_HEIGHT * 0.4
    SWORD = Image.open("images/clothes/accessories/sword.png")
    SWORD_WIDTH = SWORD.size[0]
    SWORD_HEIGHT = SWORD.size[1]
    SWORD = pygame.image.load("images/clothes/accessories/sword.png").convert_alpha()
    SWORD = pygame.transform.scale(SWORD, (SWORD_WIDTH*0.3, SWORD_HEIGHT*0.3))
    SWORD_WIDTH = SWORD_WIDTH * 0.3
    SWORD_HEIGHT = SWORD_HEIGHT * 0.3
    FAN1 = pygame.image.load("images/clothes/accessories/fan1.png").convert_alpha()
    FAN1 = pygame.transform.scale(FAN1, (FAN_WIDTH, FAN_HEIGHT))
    SWORD1 = pygame.image.load("images/clothes/accessories/sword1.png").convert_alpha()
    SWORD1 = pygame.transform.scale(SWORD1, (SWORD_WIDTH, SWORD_HEIGHT))

    ACCESSORIES = {"fan" : FAN, "sword" : SWORD, "fan1" : FAN1, "sword1" : SWORD1}

    #COLORS
    CHINESE = pygame.font.Font("images/yrdzst.ttf", 18)
    PAPYRUS = pygame.font.Font("images/papyrus.ttf", 18)
    TRAJANUS = pygame.font.Font("images/trajanus.ttf", 18)
    DARK_BROWN = (71,16,3)
    GOLD = (184, 134, 11)

    #CLOTHES
    CATEGORIES = ["tops", "bottoms", "dresses", "accessories"]
    CATEGORIES_CHINESE = ["上衣", "裤子", "裙子", "配饰"]

    CATEGORY_DICT = {"tops" : TOPS, "bottoms" : BOTTOMS, 
                    "dresses" : DRESSES, "accessories" : ACCESSORIES}