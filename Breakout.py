import pygame
import random

pygame.init()
upgrade1 = None
upgrade2 = None
upgrade3 = None
mapChoice=[]
Fps = pygame.time.Clock()
BlockWidth = 53
BlockHeight = 53
spacing = 2
pygame.display.set_caption("BREAKOUT")
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
alpha_layer = pygame.Surface((0,0),pygame.SRCALPHA, pygame.RESIZABLE)
ScreenWidth = screen.get_width()
ScreenHeight = screen.get_height()
LeftPoint = 0
RightPoint = 0
gain=1 #the amount of coins dropped by a block
TextFont = pygame.font.SysFont("Arial", 70)
TextFontSmall = pygame.font.SysFont("Arial", 40)
Clock = 120
RenderRight = TextFont.render(str(RightPoint), True, (255, 0, 0))
Blocks=set()
mapBlank = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
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
safeMaps=maps
rarities={"common" : (100,100,100)}
def strong_foundations():
    global gain
    gain += 3
upgrades = [
    ("Strong Foundations (+3 Coins)", strong_foundations,rarities["common"] )
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
            self.y = float(self.rect.y)  # Sync float tracker
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
                     ball.rect.left =self.rect.right
                else:
                    ball.rect.right =self.rect.left
            elif overlapY < overlapX:
                ball.VertVel *= -1
                if ball.VertVel > 0:
                    ball.rect.bottom =self.rect.top
                else:
                    ball.rect.top =self.rect.bottom
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
                    # Hit the bottom of a block while moving upward
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
        self.rect.y += self.vertVel
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

    def draw(self, screen, ButtonColor, text, TextColor, Width=0, border=10, Font=TextFont,):
        pygame.draw.rect(screen, ButtonColor, self.rect, Width, border_radius=border)
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
paddle1= Paddle(ScreenWidth/2, ScreenHeight-40)
ball1 = Ball(ScreenWidth/2, ScreenHeight-150)
def randomize():
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
buttonUpgrade1 = Button(150, 150, 500, 50)
buttonUpgrade2 = Button(150, 250, 500, 50)
buttonUpgrade3 = Button(150, 350, 500, 50)
def load_upgrades():
    global upgrade1, upgrade2, upgrade3
    upgrade1 = random.choice(upgrades)
    upgrade2 = random.choice(upgrades)
    upgrade3 = random.choice(upgrades)
    buttonUpgrade1.draw(screen,upgrade1[2],upgrade1[0],(0,0,0), Font= TextFontSmall)
    buttonUpgrade2.draw(screen,upgrade2[2],upgrade2[0],(0,0,0), Font= TextFontSmall)
    buttonUpgrade3.draw(screen,upgrade3[2],upgrade3[0],(0,0,0), Font= TextFontSmall)
border1 = Border(ScreenWidth/2-220)
border2 = Border(ScreenWidth/2+220)
buttonPlay = Button(ScreenWidth/2, ScreenHeight-150, 200, 70)
buttonContinue = Button(ScreenWidth/2, ScreenHeight-150, 250, 70)


coins=[]
Running = True
while Running:
    Fps.tick(Clock)
    if len(maps) == 0:
        maps=safeMaps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(RightPoint)
            Running = False
            pygame.quit()
        elif buttonPlay.clickable(event) and state == "start":
            state = "gameplay"
            loadLevel(randomize())
        elif buttonContinue.clickable(event) and state == "upgrades":
            state = "gameplay"
            loadLevel(randomize())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == "gameplay":
                    state = "pause"
                elif state == "pause":
                    state = "gameplay"
    if state == "start":
        buttonPlay.draw(screen,(0,255,0), "START", (0,0,0))
    if state == "upgrades":
        screen.fill((0, 0, 0))
        paddle1.draw(screen)
        ball1.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        screen.blit(RenderRight, (0 + 30, 0 + 30))
        alpha_layer.fill((0,0,0, 220))
        screen.blit(alpha_layer, (0,0))
        buttonContinue.draw(screen,(0,255,0), "continue", (0,0,0))
        load_upgrades()
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
                RenderRight = TextFont.render(str(RightPoint), True, (255, 0, 0))
            elif coin.rect.top >= ScreenHeight:
                coins.remove(coin)
        if len(coins) == 0 and len(Blocks) == 0:
            state = "upgrades"

        paddle1.draw(screen)
        ball1.draw(screen)
        border1.draw(screen)
        border2.draw(screen)
        if ball1.LossDetection():
            Running = False
        screen.blit(RenderRight, (0 + 30, 0 + 30))
    pygame.display.flip()