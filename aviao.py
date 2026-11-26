import pygame
import utils

class Aviao(pygame.sprite.Sprite):
    def __init__(self, clock) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utils.loadImage("aviao.png", -1, 0.1)
        self.GRAVIDADE_CONST = 900;
        self.MAX_SPEED = [1000, 1000]; # (x, y) ?
        self.MIN_SPEED = [-1000, -1000]; # (x, y) ?
        self.currSpeed = [0, 0]; # (x, y)
        self.accel = [0, 0]; # (x, y)
        self.forces = [0, 0]
        self.clock = clock

    def update(self):
        dt = self.clock.tick(60) / 1000
        
        self.accel[1] = self.GRAVIDADE_CONST
        
        self.currSpeed[0] += self.accel[0] * dt
        self.currSpeed[1] += self.accel[1] * dt
        
        if(self.currSpeed[0] > self.MAX_SPEED[0]):
            self.currSpeed[0] = self.MAX_SPEED[0]
        if(self.currSpeed[1] > self.MAX_SPEED[1]):
            self.currSpeed[1] = self.MAX_SPEED[1]
        
        if(self.currSpeed[0] < self.MIN_SPEED[0]):
            self.currSpeed[0] = self.MIN_SPEED[0]
        if(self.currSpeed[1] < self.MIN_SPEED[1]):
            self.currSpeed[1] = self.MIN_SPEED[1]
        
        # print("Minha velocidade: " + str(self.currSpeed))
        self.rect.x += self.currSpeed[0] * dt
        self.rect.y += self.currSpeed[1] * dt
