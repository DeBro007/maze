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

level = 1
game = True

while game: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if level == 1:
        window.blit(fon, (0, 0))
        
    clock.tick(FPS)
    pygame.display.update()