import pygame
import os
pygame.init()

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path

WIN_WIDTH = 960
WIN_HEIGHT = 540
FPS = 60 

fon = pygame.image.load(file_path(r"images\backgraund.png"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, x, y, width, height, image, speedx, speedy):
        super().__init__(x, y, width, height, image)
        self.speedx = speedx
        self.speedy = speedy
        self.direction = "right"
        self.image_r = self.image 
        self.image_l = pygame.transform.flip(self.image, True, False)


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


player = Player(40, 420, 55, 90, r"images\player.png", 0, 0)
enemy = GameSprite(825, 100, 81, 90, r"images\ghost.png")
finish = GameSprite(825, 420, 88, 56, r"images\prize.png") 

walls = pygame.sprite.Group()
wall1 = GameSprite(174, 516, 576, 24, r"images\wall.png")
walls.add(wall1)
wall2 = GameSprite(174, 0, 576, 24, r"images\wall.png")
walls.add(wall2)
wall3 = GameSprite(174, 24, 24, 384, r"images\wall2.png")
walls.add(wall3)
wall4 = GameSprite(726, 132, 24, 384, r"images\wall2.png")
walls.add(wall4)
wall5 = GameSprite(470, 132, 256, 24, r"images\wall.png")
walls.add(wall5)
wall6 = GameSprite(305, 388, 24, 128, r"images\wall2.png")
walls.add(wall6)
wall7 = GameSprite(198, 250, 256, 24, r"images\wall.png")
walls.add(wall7)
wall8 = GameSprite(430, 274, 24, 128, r"images\wall2.png")
walls.add(wall8)
wall9 = GameSprite(305, 24, 24, 128, r"images\wall2.png")
walls.add(wall9)
wall10 = GameSprite(598, 378, 128, 24, r"images\wall.png")
walls.add(wall10)
wall11 = GameSprite(454, 250, 128, 24, r"images\wall.png")
walls.add(wall11)


level = 1
game = True

while game: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.speedx = 4
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_a:
                    player.speedx = -4
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_w:
                    player.speedy = -4
                if event.key == pygame.K_s:
                    player.speedy = 4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.speedx = 0
                if event.key == pygame.K_a:
                    player.speedx = 0
                if event.key == pygame.K_w:
                    player.speedy = 0
                if event.key == pygame.K_s:
                    player.speedy = 0

    if level == 1:
        window.blit(fon, (0, 0))
        player.show()
        player.update()
        enemy.show()
        finish.show()
        walls.draw(window)

    clock.tick(FPS)
    pygame.display.update()