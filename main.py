from os import curdir

import pygame;
from aviao import *;
from fan import *;
import utils
import functools


def checar_colisoes(objs):
    # ordena com base do canto esquerdo
    objs.sort(key=lambda obj: obj.rect.left)
    # print(objs)
    colisoes = []
    
    for i in range(len(objs)):
        for j in range(i + 1, len(objs)):
            if(objs[j].rect.left > objs[i].rect.right):
                break 
            if(objs[i].rect.y < objs[j].rect.bottom and objs[i].rect.bottom > objs[j].rect.y):
                colisoes.append( (objs[i], objs[j]) )
    return colisoes

screen = pygame.display.set_mode((1280, 720))
pygame.mouse.set_visible(False)
bg = pygame.Surface(screen.get_size()).convert()
bg.fill("white")

screen.blit(bg, (0,0))
pygame.display.flip()

# clock = pygame.time.Clock()
cursor = Fan()
aviao = Aviao(utils.clock)
sprites = pygame.sprite.RenderPlain((cursor, aviao))
lista_arestas = [cursor, aviao]

while True:
    utils.dt = utils.clock.tick(utils.TARGET_FPS) / 1000
    # print(utils.clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        aviao.mouse_pressed = pygame.mouse.get_pressed()[0]
        
    screen.blit(bg, (0, 0))
    
    # graficos
    pygame.draw.line(screen, pygame.Color(255, 0, 0), (aviao.rect.x, aviao.rect.y), (cursor.rect.x, cursor.rect.y), 1)
    sprites.update()
    cols = checar_colisoes(lista_arestas)
    
    if((aviao, cursor) in cols or (cursor, aviao) in cols):
        aviao.kill()
    
    bg.fill("white")
    sprites.draw(screen)
    pygame.display.flip();

pygame.quit()