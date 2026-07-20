import pygame
import random
import math
import sys
import copy
import os

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

upgrade1 = []
upgrade2 = []
upgrade3 = []
mapChoice=[]
statsToPrint=[]
particles = []
Fps = pygame.time.Clock()
BlockWidth = 53
BlockHeight = 53
spacing = 2
rerolls = 0
comboRed= 0
comboGreen=200
comboWidth= 300
shakeTime=0
shakeIntensity=2
xOffset=0
yOffset=0
comboTime=0
pygame.display.set_caption("Shatter Loop")
screen = pygame.display.set_mode((1366,768))
ScreenWidth = screen.get_width()
ScreenHeight = screen.get_height()
alpha_layer = pygame.Surface((ScreenWidth,ScreenHeight),pygame.SRCALPHA)
game_surface = pygame.Surface((ScreenWidth, ScreenHeight))
coinSprite = pygame.image.load(resource_path("Sprites/coin.png")).convert_alpha()
coinSprite = pygame.transform.scale(coinSprite, (17,17))

ballSprite = pygame.image.load(resource_path("Sprites/ball.png")).convert_alpha()
ballSprite = pygame.transform.scale(ballSprite, (24,24))

blockSprite = pygame.image.load(resource_path("Sprites/block.png")).convert_alpha()
blockSprite = pygame.transform.scale(blockSprite, (52,52))

paddleSprite = pygame.image.load(resource_path("Sprites/paddle.png")).convert_alpha()
paddleSprite = pygame.transform.scale(paddleSprite, (110,35))

StartSprite = pygame.image.load(resource_path("Sprites/buttonStart.png")).convert_alpha()
StartSprite = pygame.transform.scale(StartSprite, (400,140))

StartScreenSprite = pygame.image.load(resource_path("Sprites/startScreen.png")).convert_alpha()
StartScreenSprite = pygame.transform.scale(StartScreenSprite, (ScreenWidth,ScreenHeight))

CommonBought = pygame.image.load(resource_path("Sprites/commonYes.png")).convert_alpha()
CommonBought = pygame.transform.scale(CommonBought, (850,70))

CommonNot = pygame.image.load(resource_path("Sprites/commonNo.png")).convert_alpha()
CommonNot = pygame.transform.scale(CommonNot, (850,70))

RareBought = pygame.image.load(resource_path("Sprites/rareYes.png")).convert_alpha()
RareBought = pygame.transform.scale(RareBought, (850,70))

RareNot = pygame.image.load(resource_path("Sprites/rareNo.png")).convert_alpha()
RareNot = pygame.transform.scale(RareNot, (850,70))

EpicBought = pygame.image.load(resource_path("Sprites/epicYes.png")).convert_alpha()
EpicBought = pygame.transform.scale(EpicBought, (850,70))

EpicNot = pygame.image.load(resource_path("Sprites/epicNo.png")).convert_alpha()
EpicNot = pygame.transform.scale(EpicNot, (850,70))

LegendBought = pygame.image.load(resource_path("Sprites/legendYes.png")).convert_alpha()
LegendBought = pygame.transform.scale(LegendBought, (850,70))

LegendNot = pygame.image.load(resource_path("Sprites/legendNo.png")).convert_alpha()
LegendNot = pygame.transform.scale(LegendNot, (850,70))

RerollSprite = pygame.image.load(resource_path("Sprites/RerollSprite.png")).convert_alpha()
RerollSprite = pygame.transform.scale(RerollSprite, (250,48))

ContinueSprite = pygame.image.load(resource_path("Sprites/Continue.png")).convert_alpha()
ContinueSprite = pygame.transform.scale(ContinueSprite, (400,64))

price1 = None
price2 = None
price3 = None
rareLevel1= None
rareLevel2= None
rareLevel3= None
RightPoint = 0
coin_speed=1
combo = 0
widthMult = 1
gain=1 # the amount of coins dropped by a block
comboGain=1

TextFont = pygame.font.Font(resource_path("Fonts/Silkscreen-Regular.ttf"), 70)
TextFontMid = pygame.font.Font(resource_path("Fonts/Silkscreen-Regular.ttf"), 40)
TextFontSmall = pygame.font.Font(resource_path("Fonts/Silkscreen-Regular.ttf"), 25)
TextFontXSmall = pygame.font.Font(resource_path("Fonts/Silkscreen-Regular.ttf"), 20)

Clock = 120
RenderRight = TextFont.render(str(int(RightPoint)) + "$", True, (255, 0, 0))
bought1 = False
bought2 = False
bought3 = False
level=1
Blocks=set()
mapBlank = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
map7 = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
map6 = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
map5 = [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
map4 = [
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

map3 = [
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

map2 = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
map1 = [
    [0, 1, 1, 1, 1, 1, 1,0],
    [0, 1, 1, 1, 1, 1, 1,0],
    [0, 0, 1, 0, 1, 0, 0,0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]

]
state="start"
maps=[map1, map2, map3, map4, map5, map6, map7]
#maps = [mapBlank]
#maps=[map2]
safeMaps= maps.copy()
rarities={"common" :  [1,[CommonNot, CommonBought]],
          "rare": [1.5,[RareNot,RareBought]],
          "epic": [2.5,[EpicNot, EpicBought]],
          "legendary": [3.5,[LegendNot, LegendBought]],
          }
def foundation(level):
    global gain
    gain += level
def featherweight(level):
    global coin_speed
    coin_speed *= (1-(level/25))
def expansion(level):
    global widthMult
    widthMult *= (1+(level/25))
def streak(level):
    global comboGain
    if level==3:
        comboGain += 1
    if level==4:
        comboGain += 2
StatsBlank = {
    "foundation": 0,
    "featherweight" : [0, 30],
    "Expansion Pack" : [0, 20],
    "Hit Streak" : 0
}

Stats=copy.deepcopy(StatsBlank)

upgradesCommon = [
    ["Foundation(Common) (+1 Gain)", foundation, rarities["common"],"foundation"],
    ["FeatherWeight(Common) (-4% coin speed)", featherweight, rarities["common"],"featherweight"],
    ["Expansion Pack(Common) (+4% paddle size)", expansion, rarities["common"], "Expansion Pack"]
]
upgradesRare = [
    ["Foundation(Rare) (+2 Gain)", foundation,rarities["rare"],"foundation"],
    ["FeatherWeight(Rare) (-8% coin speed)", featherweight, rarities["rare"],"featherweight"],
    ["Expansion Pack(Rare) (+8% paddle size)", expansion, rarities["rare"], "Expansion Pack"],
]
upgradesEpic = [
    ["Foundation(Epic) (+3 Gain)", foundation, rarities["epic"],"foundation"],
    ["FeatherWeight(Epic) (-12% coin speed)", featherweight, rarities["epic"],"featherweight"],
    ["Expansion Pack(Epic) (+12% paddle size)", expansion, rarities["epic"], "Expansion Pack"],
    ["Hit Streak(Epic) (+1 gain per combo)", streak, rarities["epic"], "Hit Streak"]
]
upgradesLegendary = [
    ["Foundation(Legendary!) (+4 Gain)", foundation, rarities["legendary"],"foundation"],
    ["FeatherWeight(Legendary!) (-16% coin speed)", featherweight, rarities["legendary"],"featherweight"],
    ["Expansion Pack(Legendary!) (+16% paddle size)", expansion, rarities["legendary"], "Expansion Pack"],
    ["Hit Streak(Legendary!) (+2 gain per combo)", streak, rarities["legendary"], "Hit Streak"]
]

#CLASS PADDLE
class Paddle:
    def __init__(self, x, y):
        self.height=35
        self.baseWidth=110
        self.width = self.baseWidth
        self.rect = pygame.Rect(x - self.width/2, y, self.width, self.height)
        self.speed=6
    def check_width(self):
        self.width = int(self.baseWidth * widthMult)
        centre = self.rect.centerx
        self.rect.width = self.width
        self.rect.centerx = centre
    def move(self, key_front, key_back):
        keys=pygame.key.get_pressed()
        if keys[key_back]:
            self.rect.x -= self.speed
        if keys[key_front]:
            self.rect.x += self.speed
        if self.rect.left < ScreenWidth/2 -220:
            self.rect.left = int(ScreenWidth/2 -220)
        if self.rect.right > int(ScreenWidth/2 + 220):
            self.rect.right = int(ScreenWidth/2 + 220)
    def draw(self, surface):
        scaledSprite = pygame.transform.scale(paddleSprite, (self.width, self.height))
        surface.blit(scaledSprite, (self.rect.x, self.rect.y))


class Ball:
    def __init__(self, x, y):
        self.radius = 12
        self.rect = pygame.Rect(x - self.radius, y - self.radius, 24, 24)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.baseVel = 3.5
        self.VertVel = self.baseVel
        self.HoriVel = 0

    def move(self):
        self.x += self.HoriVel
        self.y -= self.VertVel
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if self.rect.top <= 0 and self.VertVel > 0:
            self.VertVel *= -1
            self.y = 0
            self.rect.top = 0
        if self.rect.left <= ScreenWidth / 2 - 220 and self.HoriVel < 0:
            self.HoriVel *= -1
            self.x = ScreenWidth / 2 - 220
            self.rect.left = int(ScreenWidth / 2 - 220)
        if self.rect.right >= ScreenWidth / 2 + 220 and self.HoriVel > 0:
            self.HoriVel *= -1
            self.x = ScreenWidth / 2 + 220 - self.rect.width
            self.rect.right = int(ScreenWidth / 2 + 220)

    def collide(self, paddle):
        if paddle.rect.colliderect(self.rect):
            # 1. Get where it hit (-1.0 to 1.0)
            distance = self.rect.centerx - paddle.rect.centerx
            direction = distance / (paddle.width / 2)
            direction = max(-1.0, min(1.0, direction))
            max_angle = math.radians(60)
            bounce_angle = direction * max_angle
            self.HoriVel = self.baseVel * math.sin(bounce_angle)
            self.VertVel = self.baseVel * math.cos(bounce_angle)
            self.rect.bottom = paddle.rect.top
            self.y = float(self.rect.y)

    def LossDetection(self):
        return self.rect.top >= ScreenHeight

    def draw(self, surface):
        surface.blit(ballSprite,(self.rect.x, self.rect.y))
class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 48, 48)
    def collide(self, ball):
        if ball.rect.colliderect(self.rect):
            overlapX = min(self.rect.right, ball.rect.right) - max(self.rect.left, ball.rect.left)
            overlapY = min(self.rect.bottom, ball.rect.bottom) - max(self.rect.top, ball.rect.top)
            if overlapX < overlapY:
                ball.HoriVel *= -1
                if ball.HoriVel > 0:
                     ball.rect.left = self.rect.right
                else:
                    ball.rect.right = self.rect.left
                ball.x = float(ball.rect.x) # <-- ADD THIS LINE
            elif overlapY < overlapX:
                ball.VertVel *= -1
                if ball.VertVel > 0:
                    ball.rect.bottom = self.rect.top
                else:
                    ball.rect.top = self.rect.bottom
                ball.y = float(ball.rect.y) # <-- ADD THIS LINE
            return True
        return False
    def draw(self, surface):
        surface.blit(blockSprite,(self.rect.x, self.rect.y))
class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 17, 17)
        self.vertVel = 0
        self.horiVel = 0
        self.gravity = random.uniform(0.13, 0.17)
        self.friction = random.uniform(0.8, 0.98)
        self.coinStuck = False
    def collidePaddle(self, paddle):
        if paddle.rect.colliderect(self.rect):
            return True
        return False
    def collideBlock(self,Block):
        if Block.rect.colliderect(self.rect):
            overlapX = min(Block.rect.right, self.rect.right) - max(Block.rect.left, self.rect.left)
            overlapY = min(Block.rect.bottom, self.rect.bottom) - max(Block.rect.top, self.rect.top)
            if overlapX < overlapY:
                self.horiVel *= -1
                if self.horiVel > 0:
                    self.rect.left = Block.rect.right
                else:
                    self.rect.right = Block.rect.left
            elif overlapY < overlapX:
                if self.vertVel > 0 and self.rect.bottom > Block.rect.top and self.rect.top < Block.rect.top:
                    self.vertVel = 0
                    self.rect.bottom = Block.rect.top  # Snap clean to top
                else:
                    self.vertVel *= -0.5
                    if self.vertVel > 0:
                        self.rect.top = Block.rect.bottom
                    else:
                        self.rect.bottom = Block.rect.top
    def move(self):
        if random.choice([True, False]) == True:
            self.horiVel *= self.friction
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vertVel = self.vertVel * -1
        if self.rect.left <= ScreenWidth/2 -220:
            self.rect.left = int(ScreenWidth/2 -220)
            self.horiVel *= -1
        if self.rect.right >= ScreenWidth /2 +220:
            self.horiVel *= -1
            self.rect.right = int(ScreenWidth/2 +220)

        self.vertVel += self.gravity
        self.rect.x += self.horiVel
        self.rect.y += self.vertVel * coin_speed
    def draw(self, surface):
        surface.blit(coinSprite,(self.rect.x, self.rect.y))
class Border:
    def __init__(self, x):
        self.x = x
        self.top= 0
        self.bottom = ScreenHeight
    def draw(self, surface):
        pygame.draw.line(surface,(255,255,255),(self.x, self.top),(self.x, self.bottom), 2)
class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, ButtonColor, TextColor,Text="", Width=0, border=10, Font=TextFont,BorderColour=None, Sprite=None):

        if Sprite is not None:
            screen.blit(Sprite, (self.rect.x, self.rect.y))
            if Text != "":
                text_element = Font.render(Text, True, TextColor)
                TextRect = text_element.get_rect()
                TextRect.centerx = self.rect.centerx
                TextRect.centery = self.rect.centery
                screen.blit(text_element, TextRect)
        else:
            pygame.draw.rect(screen, ButtonColor, self.rect, Width, border_radius=border)
            if BorderColour is not None:
                pygame.draw.rect(screen, BorderColour, self.rect, 4, border_radius=border)
            text_element = Font.render(Text, True, TextColor)
            TextRect = text_element.get_rect()
            TextRect.centerx = self.rect.centerx
            TextRect.centery = self.rect.centery
            screen.blit(text_element, TextRect)

    def clickable(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    return True
        return False

class Text:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, TextColor, string, TextFont=TextFontSmall):
        text_surf = TextFont.render(string, True, TextColor)
        screen.blit(text_surf, (self.x, self.y))

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVel = random.uniform(-2, 2)
        self.yVel = random.uniform(-2, 2)
        self.lifetime = 30

    def move(self):
        self.x += self.xVel
        self.y += self.yVel
        self.lifetime -= 1

    def draw(self, surface):
        size = max(1, int(self.lifetime / 3))
        pygame.draw.rect(surface, (200, 200, 200), (int(self.x), int(self.y), size, size))
class ComboBar:
    def __init__(self, x, y, height):
        self.x = x
        self.y =y
        self.height = height
        self.StartWidth = comboWidth
    def draw(self, surface, red, green):
        red = min(255, red)
        green = max(0, green)
        self.outlineRect = pygame.Rect(self.x - 5, self.y - 5, self.StartWidth + 10, self.height + 10)
        self.rect = pygame.Rect(self.x, self.y, comboWidth, self.height)
        pygame.draw.rect(surface, (0, 0, 0), self.outlineRect)
        pygame.draw.rect(surface, (255, 255, 255), self.outlineRect, width= 2)
        pygame.draw.rect(surface, (red, green, 0), self.rect)
        comboRender1=TextFontSmall.render("x" + str(combo), True ,(255,255,255))
        game_surface.blit(comboRender1, (self.x, self.y + self.height + 5))
        comboRender2=TextFontXSmall.render("combo", True ,(255,255,255))
        game_surface.blit(comboRender2, (self.x + 220, self.y - 35))
paddle1= Paddle(ScreenWidth/2, ScreenHeight-40)
ball1 = Ball(ScreenWidth/2, ScreenHeight-150)
comboMeter = ComboBar(ScreenWidth - 430, 50, 30)
def randomize():
    global maps
    if len(maps) == 0:
        maps=safeMaps.copy()
    mapChoice = random.choice(maps)
    maps.remove(mapChoice)
    return mapChoice
def loadLevel(map):
    for line, lineValue in enumerate(map):
        for column, value in enumerate(lineValue):
            if value == 1:
                x = ScreenWidth/2 -220 + column * (BlockWidth + spacing)
                y = 50 + line * (BlockHeight + spacing)
                new_block = Block(x, y)
                new_block.rect = pygame.Rect(x, y, BlockWidth, BlockHeight)
                Blocks.add(new_block)
    ball1.rect.width = 24
    ball1.rect.height = 24
    ball1.rect.centerx = int(ScreenWidth / 2)
    ball1.rect.centery = ScreenHeight - 150
    ball1.x = float(ball1.rect.x)
    ball1.y = float(ball1.rect.y)
    ball1.baseVel = 3.2 + (level * 0.2)  # Gets slightly faster each level you beat!
    ball1.HoriVel = 0
    ball1.VertVel = ball1.baseVel
    paddle1.check_width()
    paddle1.rect.centerx=int(ScreenWidth/2)
    paddle1.rect.centery=ScreenHeight -40
buttonUpgrade1 = Button(150, 150, 850, 70)
buttonUpgrade2 = Button(150, 250, 850, 70)
buttonUpgrade3 = Button(150, 350, 850, 70)
def setup_upgrades():
    global upgrade1, upgrade2, upgrade3, bought1, bought2, bought3, rareLevel1, rareLevel2, rareLevel3, price1, price2, price3, rerollPrice

    OpenKeys = []
    for key, value in Stats.items():
        if type(value) == list:
            if value[0] < value[1]:
                OpenKeys.append(key)
        else:
            OpenKeys.append(key)

    OpenCommon = []
    for x in upgradesCommon:
        if x[3] in OpenKeys:
            OpenCommon.append(x)

    OpenRare = []
    for x in upgradesRare:
        if x[3] in OpenKeys:
            OpenRare.append(x)

    OpenEpic = []
    for x in upgradesEpic:
        if x[3] in OpenKeys:
            OpenEpic.append(x)

    OpenLegend = []
    for x in upgradesLegendary:
        if x[3] in OpenKeys:
            OpenLegend.append(x)

    if len(OpenCommon) == 0:
        OpenCommon = upgradesCommon
        OpenRare = upgradesRare
        OpenEpic = upgradesEpic
        OpenLegend = upgradesLegendary

    chosen_pools = random.choices(
        (OpenCommon, OpenRare, OpenEpic, OpenLegend),(10, 5, 2, 1),k=3)

    bought1 = False
    bought2 = False
    bought3 = False
    rerollPrice = math.pow(4, rerolls + 1)
    upgrade1 = random.choice(chosen_pools[0])
    upgrade2 = random.choice(chosen_pools[1])
    upgrade3 = random.choice(chosen_pools[2])
    if upgrade1[2] == rarities["common"]:
        rareLevel1=1
    if upgrade1[2] == rarities["rare"]:
        rareLevel1=2
    if upgrade1[2] == rarities["epic"]:
        rareLevel1=3
    if upgrade1[2] == rarities["legendary"]:
        rareLevel1=4
    if upgrade2[2] == rarities["common"]:
        rareLevel2=1
    if upgrade2[2] == rarities["rare"]:
        rareLevel2=2
    if upgrade2[2] == rarities["epic"]:
        rareLevel2=3
    if upgrade2[2] == rarities["legendary"]:
        rareLevel2=4
    if upgrade3[2] == rarities["common"]:
        rareLevel3=1
    if upgrade3[2] == rarities["rare"]:
        rareLevel3=2
    if upgrade3[2] == rarities["epic"]:
        rareLevel3=3
    if upgrade3[2] == rarities["legendary"]:
        rareLevel3=4
    price1 = int(calculate(upgrade1))
    price2 = int(calculate(upgrade2))
    price3 = int(calculate(upgrade3))
def calculate(upgrade):
    rarityMult = upgrade[2][0]
    upgradeKey = upgrade[3]
    statLvl = Stats.get(upgradeKey)
    if type(statLvl) == list:
        statLvl = statLvl[0]
    basePrice = 12 * math.pow(1.5, statLvl)
    return int(basePrice * rarityMult * random.uniform(0.8,1.2))

def load_upgrades():
    if bought1 == True:
        buttonUpgrade1.draw(game_surface,(0,100,0),(0,0,0),Text=upgrade1[0] + " " + str(price1) + "$", Font= TextFontSmall, Sprite=upgrade1[2][1][1])
    elif bought1 == False:
        buttonUpgrade1.draw(game_surface,(0,100,0),(0,0,0),Text=upgrade1[0] + " " + str(price1) + "$", Font= TextFontSmall, Sprite=upgrade1[2][1][0])

    if bought2 == True:
        buttonUpgrade2.draw(game_surface, (0, 100, 0), (0, 0, 0), Text=upgrade2[0] + " " + str(price2) + "$", Font=TextFontSmall,Sprite=upgrade2[2][1][1])
    elif bought2 == False:
        buttonUpgrade2.draw(game_surface, (0, 100, 0), (0, 0, 0), Text=upgrade2[0] + " " + str(price2) + "$", Font=TextFontSmall,Sprite=upgrade2[2][1][0])

    if bought3 == True:
        buttonUpgrade3.draw(game_surface, (0, 100, 0), (0, 0, 0), Text=upgrade3[0] + " " + str(price3) + "$", Font=TextFontSmall,Sprite=upgrade3[2][1][1])
    elif bought3 == False:
        buttonUpgrade3.draw(game_surface, (0, 100, 0), (0, 0, 0), Text=upgrade3[0] + " " + str(price3) + "$", Font=TextFontSmall,Sprite=upgrade3[2][1][0])
def load_stats():
    global statsToPrint
    x = ScreenWidth - 350
    y = 130
    for key, value in Stats.items():
        if type(value) == list:
            if value[0] > 0:
                statsToPrint.append(key + ": " + str(value[0])+"/"+ str(value[1]))
        else:
            if value > 0:
                statsToPrint.append(key + ": " + str(value))
    for stat in statsToPrint:
        statSurf = TextFontXSmall.render(stat, True, (255,255,255))
        screen.blit(statSurf, (x, y))
        y += 30
    statsToPrint = []

border1 = Border(ScreenWidth/2-220)
border2 = Border(ScreenWidth/2+220)
buttonPlay = Button(ScreenWidth/2 + 200, ScreenHeight-200, 400, 150)
buttonContinue = Button(160,450, 400, 64)
buttonReroll = Button(ScreenWidth - 400, 50, 250, 48)
titleText = Text(ScreenWidth/2 - 370,100)


coins=[]
Running = True
while Running:
    dt = Fps.tick(Clock) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(RightPoint)
            Running = False
            pygame.quit()
            sys.exit()
        elif buttonPlay.clickable(event) and state == "start":
            state = "gameplay"
            loadLevel(randomize())
        elif state == "upgrades":
            if buttonContinue.clickable(event):
                level += 1
                state = "gameplay"
                loadLevel(randomize())
            elif buttonUpgrade1.clickable(event) and bought1 == False and RightPoint >= price1:
                bought1 = True
                RightPoint -= price1
                upgrade1[1](rareLevel1)
                if type(Stats[upgrade1[3]]) == list:
                    Stats[upgrade1[3]][0] += rareLevel1
                else:
                    Stats[upgrade1[3]] += rareLevel1
            elif buttonUpgrade2.clickable(event) and bought2 == False and RightPoint >= price2:
                bought2 = True
                RightPoint -= price2

                upgrade2[1](rareLevel2)
                if type(Stats[upgrade2[3]]) == list:
                    Stats[upgrade2[3]][0] += rareLevel2
                else:
                    Stats[upgrade2[3]] += rareLevel2
            elif buttonUpgrade3.clickable(event) and bought3 == False and RightPoint >= price3:
                bought3 = True
                RightPoint -= price3
                upgrade3[1](rareLevel3)
                if type(Stats[upgrade3[3]]) == list:
                    Stats[upgrade3[3]][0] += rareLevel3
                else:
                    Stats[upgrade3[3]] += rareLevel3

            elif buttonReroll.clickable(event) and RightPoint >= rerollPrice:
                rerolls += 1
                RightPoint -= rerollPrice
                setup_upgrades()
            RenderRight = TextFont.render(str(int(RightPoint)) + "$", True, (255, 0, 0))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == "gameplay":
                    state = "pause"
                elif state == "pause":
                    state = "gameplay"
    if state == "start":
        game_surface.fill((0,0,0))
        game_surface.blit(StartScreenSprite, (0,0))
        buttonPlay.draw(game_surface,(0,255,0), (0,0,0), Sprite=StartSprite)
    if state == "upgrades":
        game_surface.fill((0, 0, 0))
        paddle1.draw(game_surface)
        ball1.draw(game_surface)
        border1.draw(game_surface)
        border2.draw(game_surface)
        alpha_layer.fill((0,0,0, 220))
        game_surface.blit(alpha_layer, (0,0))
        game_surface.blit(RenderRight, (0 + 30, 0 + 30))
        buttonContinue.draw(game_surface,(0,255,0),(0,0,0),Text="Continue", Font= TextFontMid,Sprite = ContinueSprite)
        buttonReroll.draw(game_surface, (200, 200, 200),(255,255,255), border = 5, Font=TextFontSmall ,Text ="Reroll " + str(int(rerollPrice)) + "$", Sprite=RerollSprite)
        load_upgrades()
        load_stats()

    if state == "pause":
        game_surface.fill((0, 0, 0))
        for block in Blocks:
            block.draw(game_surface)
        for coin in coins:
            coin.draw(game_surface)
        paddle1.draw(game_surface)
        ball1.draw(game_surface)
        border1.draw(game_surface)
        border2.draw(game_surface)
        game_surface.blit(RenderRight, (0 + 30, 0 + 30))
        alpha_layer.fill((0,0,0, 150))
        game_surface.blit(alpha_layer, (0,0))
    if state == "loss":
        game_surface.fill((0, 0, 0))
        for block in Blocks:
            block.draw(game_surface)
        for coin in coins:
            coin.draw(game_surface)
        paddle1.draw(game_surface)
        ball1.draw(game_surface)
        border1.draw(game_surface)
        border2.draw(game_surface)
        game_surface.blit(RenderRight, (0 + 30, 0 + 30))
        alpha_layer.fill((0,0,0, 150))
        game_surface.blit(alpha_layer, (0,0))
    if state == "gameplay":
        game_surface.fill((50, 50, 50))
        ball1.move()
        paddle1.move(pygame.K_d, pygame.K_a)
        ball1.collide(paddle1)
        xOffset = 0
        yOffset = 0
        if shakeTime > 0:
            shakeTime -= dt
            xOffset = random.randint(-shakeIntensity,shakeIntensity)
            yOffset = random.randint(-shakeIntensity,shakeIntensity)
        for particle in particles:
            particle.move()
            particle.draw(game_surface)
            if particle.lifetime <= 0:
                particles.remove(particle)

        for block in list(Blocks):
            block.draw(game_surface)
            if block.collide(ball1):
                Blocks.remove(block)
                shakeTime = 0.10
                for _ in range(6):
                    particles.append(Particle(block.rect.centerx, block.rect.centery))

                for i in range(gain + (combo * comboGain)):
                    coin = Coin(block.rect.centerx, block.rect.centery)
                    coin.horiVel = random.uniform(-1.5, 1.5)
                    coin.vertVel = random.uniform(-5, -2)
                    coins.append(coin)
                combo += 1
                comboTime = 1
                comboRed = 1
                comboGreen = 255
                comboWidth=300

        if combo > 0:
            if comboTime > 0:
                comboTime -= dt
                comboRed= int(max(0, 254 * (1- comboTime)))
                comboGreen= int(min(255,255* comboTime))
                comboWidth = int(300* comboTime)
                comboMeter.draw(game_surface, comboRed, comboGreen)
            else:
                comboTime=0
                comboRed = 1
                comboGreen = 255
                comboWidth = 300
                combo = 0
        for coin in list(coins):

            coin.draw(game_surface)
            BlocksToCheck=Blocks.copy()
            coin.speed = 0
            coin.move()
            for block in list(BlocksToCheck):
                coin.collideBlock(block)
                if block.rect.bottom <= coin.rect.top:
                    BlocksToCheck.remove(block)
            if coin.collidePaddle(paddle1):
                coins.remove(coin)
                RightPoint+=1
                RenderRight = TextFont.render(str(int(RightPoint)) + "$", True, (255, 0, 0))
            elif coin.rect.top >= ScreenHeight:
                coins.remove(coin)
        if len(coins) == 0 and len(Blocks) == 0:
            print(Stats)
            rerolls=0
            combo=0
            comboTime=0
            state = "upgrades"
            setup_upgrades()

        paddle1.draw(game_surface)
        ball1.draw(game_surface)
        border1.draw(game_surface)
        border2.draw(game_surface)
        if ball1.LossDetection():
            RightPoint = 0
            coins = []
            state="start"
            Blocks.clear()
            RenderRight = TextFont.render(str(int(RightPoint)) + "$", True, (255, 0, 0))
            gain = 1
            coin_speed = 1
            widthMult = 1
            level = 1
            rerolls = 0
            comboGain = 1
            combo=0
            comboTime = 0
            Stats = copy.deepcopy(StatsBlank)
        game_surface.blit(RenderRight, (0 + 30, 0 + 30))
    screen.blit(game_surface, (xOffset, yOffset))
    pygame.display.flip()
