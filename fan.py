import pygame
import os
import utils


class Fan(pygame.sprite.Sprite):
    
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utils.loadImage("fan.png", -1, 0.1)
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos