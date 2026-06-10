
import pygame


pygame.init()
Fps = pygame.time.Clock()
ScreenWidth = 1000
ScreenHeight = 700
BlockWidth = 53
BlockHeight = 53
spacing = 2
pygame.display.set_caption("BREAKOUT")
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
LeftPoint = 0
RightPoint = 0
TextFont = pygame.font.SysFont("Arial", 70)
Clock = 120
RenderRight = TextFont.render(str(RightPoint), True, (255, 0, 0))
Blocks=set()
map2 = [
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0]
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

#CLASS PADDLE
class Paddle:
    def __init__(self, x, y):
        self.height=40
        self.width=100
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.speed=6
    def move(self, key_front, key_back):
        keys=pygame.key.get_pressed()
        if keys[key_back]:
            self.rect.x -= self.speed
        if keys[key_front]:
            self.rect.x += self.speed
        if self.rect.left < 0+280:
            self.rect.left = 0+280
        if self.rect.right > ScreenWidth-280:
            self.rect.right = ScreenWidth-280
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, border_radius=20)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y,24, 24)
        self.radius=10
        self.VertVel=2
        self.HoriVel=2
    def move(self):
        self.rect.x += self.HoriVel
        self.rect.y -= self.VertVel
        if self.rect.y <= 0 + self.radius:
            self.VertVel = self.VertVel*-1
        if self.rect.x <= 0+280 + self.radius or self.rect.x >= ScreenWidth - self.radius - 280 - self.radius:
            self.HoriVel *= -1

    def collide(self, paddle):
        if paddle.rect.colliderect(self.rect):
            distance = self.rect.centerx - paddle.rect.centerx
            direction = distance / (paddle.width / 2)
            self.HoriVel = direction * 3
            self.rect.bottom = paddle.rect.top
            self.VertVel = 4 - abs(self.HoriVel)
    def LossDetection(self):
        if self.rect.top >= ScreenHeight:
            return True
        return False

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.rect.center, self.radius)
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
        self.speed = 6
        self.coinStuck = False
    def collidePaddle(self, paddle):
        if paddle.rect.colliderect(self.rect):
            return True
        return False
    def collideBlock(self,Block):
        if Block.rect.colliderect(self.rect):
            return True
        return False
    def move(self):
        self.rect.y += self.speed
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), self.rect.center, 8)
class Border:
    def __init__(self, x):
        self.x = x
        self.top= 0
        self.bottom = ScreenHeight
    def draw(self, surface):
        pygame.draw.line(surface,(255,255,255),(self.x, self.top),(self.x, self.bottom), 1)
paddle1= Paddle(ScreenWidth/2, ScreenHeight-40)
ball1 = Ball(ScreenWidth/2, ScreenHeight-150)
border1 = Border(280)
border2 = Border(ScreenWidth-280)
coins=[]
for line, lineValue in enumerate(map1):
    for column, value in enumerate(lineValue):
        if value == 1:
            x = 280 + column * (BlockWidth + spacing)
            y = 50 + line * (BlockHeight + spacing)
            new_block = Block(x, y)
            new_block.rect = pygame.Rect(x, y, BlockWidth, BlockHeight)
            Blocks.add(new_block)
Running = True
while Running:

    Fps.tick(Clock)
    screen.fill((0,0,0))
    #COLLISION
    ball1.collide(paddle1)
    for block in list(Blocks):
        block.draw(screen)
        if block.collide(ball1):
            Blocks.remove(block)
            coin = Coin(block.rect.centerx, block.rect.centery)
            coins.append(coin)
    for coin in list(coins):
        coin.draw(screen)
        BlocksToCheck=Blocks.copy()
        if coin.coinStuck == False:
            for block in list(BlocksToCheck):
                if block.rect.bottom <= coin.rect.top:
                    BlocksToCheck.remove(block)
                if coin.collideBlock(block):
                    coin.coinStuck= True
                    coin.speed = 0
                else:
                    coin.coinStuck= False
            coin.move()
        if coin.collidePaddle(paddle1):
            coins.remove(coin)
            RightPoint+=1
            RenderRight = TextFont.render(str(RightPoint), True, (255, 0, 0))
        elif coin.rect.top >= ScreenHeight:
            coins.remove(coin)

    paddle1.move(pygame.K_d, pygame.K_a)

    paddle1.draw(screen)

    ball1.move()
    ball1.draw(screen)
    border1.draw(screen)
    border2.draw(screen)
    if ball1.LossDetection():
        Running = False
    screen.blit(RenderRight, (0 + 30, 0 + 30))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(RightPoint)
            Running = False
            pygame.quit()
