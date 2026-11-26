import pygame;
from aviao import *;
from fan import *;
import utils


screen = pygame.display.set_mode((1280, 720))
pygame.mouse.set_visible(False)
bg = pygame.Surface(screen.get_size()).convert()
bg.fill("white")

screen.blit(bg, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()
cursor = Fan()
aviao = Aviao(clock)
sprites = pygame.sprite.RenderPlain((cursor, aviao))
while True:
    clock.tick(60)
    print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    # graficos
    
    sprites.update()
    
    
    screen.blit(bg, (0, 0))
    sprites.draw(screen)
    pygame.display.flip();

pygame.quit()