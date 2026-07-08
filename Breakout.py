import pygame
import random
import math
import sys

pygame.init()
upgrade1 = []
upgrade2 = []
upgrade3 = []
mapChoice=[]
statsToPrint=[]
Fps = pygame.time.Clock()
BlockWidth = 53
BlockHeight = 53
spacing = 2
rerolls = 0
pygame.display.set_caption("BREAKOUT")
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
ScreenWidth = screen.get_width()
ScreenHeight = screen.get_height()
alpha_layer = pygame.Surface((ScreenWidth,ScreenHeight),pygame.SRCALPHA)
price1 = None
price2 = None
price3 = None
rareLevel1= None
rareLevel2= None
rareLevel3= None
LeftPoint = 0
RightPoint = 0
coin_speed=1
gain=1#the amount of coins dropped by a block
TextFont = pygame.font.SysFont("Helvetica", 70)
TextFontSmall = pygame.font.SysFont("Helvetica", 40)
TextFontXSmall = pygame.font.SysFont("Helvetica", 30)
TitleFont = pygame.font.SysFont("Courier new",120)
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
safeMaps= maps.copy()
rarities={"common" :  [1,(130,130,130)],
          "rare": [1.5,(47,147,255)],
          "epic": [2.5,(168,0,255)],
          "legendary": [3.5,(255,156,0)]
          }
def foundation(level):
    global gain
    gain += level
def featherweight(level):
    global coin_speed
    coin_speed *= (1-(level/50))


Stats = {
    "foundation": 0,
    "featherweight" : [0, 30]
}

upgradesCommon = [
    ["Foundation(Common) (+1 Gain)", foundation, rarities["common"],"foundation"],
    ["FeatherWeight(Common) (-2% coin speed)", featherweight, rarities["common"],"featherweight"]
]
upgradesRare = [
    ["Foundation(Rare) (+2 Gain)", foundation,rarities["rare"],"foundation"],
    ["FeatherWeight(Rare) (-4% coin speed)", featherweight, rarities["rare"],"featherweight"]
]
upgradesEpic = [
    ["Foundation(Epic) (+3 Gain)", foundation, rarities["epic"],"foundation"],
    ["FeatherWeight(Epic) (-6% coin speed)", featherweight, rarities["epic"],"featherweight"]
]
upgradesLegendary = [
    ["Foundation(Legendary!) (+4 Gain)", foundation, rarities["legendary"],"foundation"],
    ["FeatherWeight(Legendary!) (-8% coin speed)", featherweight, rarities["legendary"],"featherweight"]
]

#CLASS PADDLE
class Paddle:
    def __init__(self, x, y):
        self.height=30
        self.width=110
        self.rect = pygame.Rect(x - self.width/2, y, self.width, self.height)
        self.speed=6
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
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=20)


class Ball:
    def __init__(self, x, y):
        self.radius = 12
        self.rect = pygame.Rect(x - self.radius, y - self.radius, 24, 24)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.VertVel = 2.2
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
        if self.rect.left <= ScreenWidth /2 -220 and self.HoriVel < 0:
            self.HoriVel *= -1
            self.x = ScreenWidth /2 -220
            self.rect.left = int(ScreenWidth/2 -220)
        if self.rect.right >= ScreenWidth /2 + 220 and self.HoriVel > 0:
            self.HoriVel *= -1
            self.x = ScreenWidth /2 +220 - self.rect.width
            self.rect.right = int(ScreenWidth /2 +220)

    def collide(self, paddle):
        if paddle.rect.colliderect(self.rect):
            distance = self.rect.centerx - paddle.rect.centerx
            direction = distance / (paddle.width / 2)
            direction = max(-1.0, min(1.0, direction))

            self.HoriVel = direction * 2.2
            if abs(self.HoriVel) < 0.5:
                self.HoriVel = 0.6 if direction >= 0 else -0.6

            self.rect.bottom = paddle.rect.top
            self.y = float(self.rect.y)
            self.VertVel = 2.2

    def LossDetection(self):
        return self.rect.top >= ScreenHeight

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.rect.center, self.radius)
        pygame.draw.circle(surface, (0, 0, 0), self.rect.center, self.radius, 2)
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
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=3)
class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
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
        pygame.draw.circle(surface, (255, 255, 0), self.rect.center, 8)
        pygame.draw.circle(surface, (0, 0, 0), self.rect.center, 8, 2)
class Border:
    def __init__(self, x):
        self.x = x
        self.top= 0
        self.bottom = ScreenHeight
    def draw(self, surface):
        pygame.draw.line(surface,(255,255,255),(self.x, self.top),(self.x, self.bottom), 1)
class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen, ButtonColor, text, TextColor, Width=0, border=10, Font=TextFont,BorderColour=None):
        pygame.draw.rect(screen, ButtonColor, self.rect, Width, border_radius=border)
        if BorderColour is not None:
            pygame.draw.rect(screen, BorderColour, self.rect, 4, border_radius=border)
        text_element = Font.render(text, True, TextColor)
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

paddle1= Paddle(ScreenWidth/2, ScreenHeight-40)
ball1 = Ball(ScreenWidth/2, ScreenHeight-150)
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
    ball1.HoriVel=0
    ball1.VertVel=2.2
    paddle1.rect.centerx=int(ScreenWidth/2)
    paddle1.rect.centery=ScreenHeight -40
buttonUpgrade1 = Button(150, 150, 800, 50)
buttonUpgrade2 = Button(150, 250, 800, 50)
buttonUpgrade3 = Button(150, 350, 800, 50)
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

    # 8. Pull a random upgrade out of the valid pools you rolled
    upgrade1 = random.choice(chosen_pools[0])
    upgrade2 = random.choice(chosen_pools[1])
    upgrade3 = random.choice(chosen_pools[2])

    # ... (Keep your exact rareLevel check and price calculation logic here)
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
        buttonUpgrade1.draw(screen,(0,100,0),upgrade1[0] + str(price1) + "$",(0,0,0), Font= TextFontSmall, BorderColour= upgrade1[2][1])
    elif bought1 == False:
        buttonUpgrade1.draw(screen,upgrade1[2][1],upgrade1[0] + str(price1)+"$",(0,0,0), Font= TextFontSmall)

    if bought2 == True:
        buttonUpgrade2.draw(screen,(0,100,0),upgrade2[0] + str(price2) +"$",(0,0,0), Font= TextFontSmall, BorderColour= upgrade2[2][1])
    elif bought2 == False:
        buttonUpgrade2.draw(screen,upgrade2[2][1],upgrade2[0] + str(price2)+"$",(0,0,0), Font= TextFontSmall)

    if bought3 == True:
        buttonUpgrade3.draw(screen,(0,100,0),upgrade3[0] + str(price3) + "$",(0,0,0), Font= TextFontSmall, BorderColour= upgrade3[2][1])
    elif bought3 == False:
        buttonUpgrade3.draw(screen,upgrade3[2][1],upgrade3[0] + str(price3) + "$",(0,0,0), Font= TextFontSmall)
def load_stats():
    global statsToPrint
    x = ScreenWidth - 400
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
buttonPlay = Button(ScreenWidth/2 - 100, ScreenHeight-150, 200, 70)
buttonContinue = Button(ScreenWidth/2, ScreenHeight-150, 250, 70)
buttonReroll = Button(ScreenWidth - 300, 50, 200, 50)
titleText = Text(ScreenWidth/2 - 370,100)


coins=[]
Running = True
while Running:
    Fps.tick(Clock)
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
        screen.fill((0,0,0))
        buttonPlay.draw(screen,(0,255,0), "START", (0,0,0))
        titleText.draw(screen, (255,0,0), "Breakout.py",TextFont=TitleFont)
    if state == "upgrades":
        screen.fill((0, 0, 0))
        paddle1.draw(screen)
        ball1.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        alpha_layer.fill((0,0,0, 220))
        screen.blit(alpha_layer, (0,0))
        screen.blit(RenderRight, (0 + 30, 0 + 30))
        buttonContinue.draw(screen,(0,255,0), "continue", (0,0,0))
        buttonReroll.draw(screen, (200, 200, 200),"Reroll " + str(int(rerollPrice)) + "$", (255,255,255), border = 5, Font= TextFontSmall)
        load_upgrades()
        load_stats()

    if state == "pause":
        screen.fill((0, 0, 0))
        for block in Blocks:
            block.draw(screen)
        for coin in coins:
            coin.draw(screen)
        paddle1.draw(screen)
        ball1.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        screen.blit(RenderRight, (0 + 30, 0 + 30))
        alpha_layer.fill((0,0,0, 150))
        screen.blit(alpha_layer, (0,0))
    if state == "loss":
        screen.fill((0, 0, 0))
        for block in Blocks:
            block.draw(screen)
        for coin in coins:
            coin.draw(screen)
        paddle1.draw(screen)
        ball1.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        screen.blit(RenderRight, (0 + 30, 0 + 30))
        alpha_layer.fill((0,0,0, 150))
        screen.blit(alpha_layer, (0,0))
    if state == "gameplay":
        screen.fill((50, 50, 50))
        ball1.move()
        paddle1.move(pygame.K_d, pygame.K_a)
        ball1.collide(paddle1)

        for block in list(Blocks):
            block.draw(screen)
            if block.collide(ball1):
                Blocks.remove(block)
                for i in range(gain):
                    coin = Coin(block.rect.centerx, block.rect.centery)
                    coin.horiVel = random.uniform(-1.5, 1.5)
                    coin.vertVel = random.uniform(-5, -2)
                    coins.append(coin)
        for coin in list(coins):

            coin.draw(screen)
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
            state = "upgrades"
            setup_upgrades()

        paddle1.draw(screen)
        ball1.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        if ball1.LossDetection():
            RightPoint = 0
            coins = []
            state="start"
            Blocks.clear()
            RenderRight = TextFont.render(str(int(RightPoint)) + "$", True, (255, 0, 0))
        screen.blit(RenderRight, (0 + 30, 0 + 30))
    pygame.display.flip()
