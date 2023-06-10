import pygame
import os
pygame.init

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path

WIN_WIDTH = 960
WIN_HEIGHT = 540
FPS = 40 

fon = pygame.image.load(file_path(r"images\backgraund.png"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite(40, 420, 55, 90, r"images\player.png")
enemy = GameSprite(324, 420, 81, 90, r"images\ghost.png")
finish = GameSprite(123, 420, 88, 56, r"images\prize.png")

level = 1
game = True

while game: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if level == 1:
        window.blit(fon, (0, 0))
        player.show()
        enemy.show()
        finish.show()

    clock.tick(FPS)
    pygame.display.update()