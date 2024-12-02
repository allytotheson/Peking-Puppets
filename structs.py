import constants as const
class GameState:
    def __init__(self, clothes):
        self.closetOn = False
        self.closetHov = False
        self.currClothesOn = False
        self.currCategory = "tops"
        self.xHov = False
        self.clothes = clothes
        self.finalBG = False
        self.bgHov = False
        self.selectedItem = None
        self.doll = True
        self.typeHov = False


class Clothes:
    def __init__(self):
        self.top = None
        self.topColor = (255,255,255)
        self.bottom = None
        self.bottomColor = (255,255,255)
        self.dress = None
        self.dressColor = (255,255,255)
        self.accessory = None
        self.accessoryColor = (255,255,255)
        self.clothes_positions = {"tops" : (const.BACKGROUND_WIDTH*0.5, const.BACKGROUND_HEIGHT*0.5), 
                                  "bottoms" : (const.BACKGROUND_WIDTH*0.6, const.BACKGROUND_HEIGHT*0.6), 
                                  "dresses" : (const.BACKGROUND_WIDTH*0.7, const.BACKGROUND_HEIGHT*0.7), 
                                  "accessories" : (const.BACKGROUND_WIDTH*0.8, const.BACKGROUND_HEIGHT*0.8)}