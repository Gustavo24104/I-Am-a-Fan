from typing import overload

import pygame
from pygame.event import get
import utils
import math

class Aviao(pygame.sprite.Sprite):
    def __init__(self, clock) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = utils.loadImage("aviao.png", -1, 0.1)
        self.rect.x = 600
        self.rect.y = 300
        self.GRAVIDADE_CONST = 900;
        self.MAX_SPEED = [1000, 1000]; # (x, y) ?
        self.MIN_SPEED = [-1000, -1000]; # (x, y) ?
        self.ATRITO = [0.8, 0.35] # fiz uns testes e pareceu mais legal aplicar menos atrito na horizontal
        self.mouse_pressed = False
        self.currSpeed = [0, 0]; # (x, y)
        self.accel = [0, 0]; # (x, y)
        self.forces = [0, 0]
        self.clock = clock

    # encontra a direcao ate outro ponto, retorna ela (normalizada) e a distancia
    def get_dir(self, x, y):
        vecX = x - self.rect.x
        vecY = y - self.rect.y
        mag = math.sqrt((vecX**2 + vecY**2))
        return vecX / mag, vecY / mag, mag
    
    # nao normaliza, ai normaliza no final pra decidir a direcao
    # cada vetor aqui eh a componente (x, y)
    def calcula_aceleracao(self, lista_forcas):
        sumX = 0
        sumY = 0
        for forca in lista_forcas:
            sumX += forca[0]
            sumY += forca[1]
        mag = (sumX**2 + sumY**2)**(-0.5)
        self.accel[0], self.accel[1] = sumX * mag, sumY * mag

    def check_collision(self):
        pass

    def update(self):
        dt = utils.dt
        # self.accel[1] = self.GRAVIDADE_CONST
        # self.accel[0] = 450
        
        if(self.mouse_pressed):
            mouseDirX, mouseDirY, dist = self.get_dir(*pygame.mouse.get_pos())
            print("distancia: " + str(dist))
            # mouseDirX, mouseDirY = self.get_dir(*pygame.mouse.get_pos())
            self.accel[0], self.accel[1] = mouseDirX * (-600 * (200/dist)), \
                (mouseDirY * (-1700 * (200/dist)) + self.GRAVIDADE_CONST)
        else:
            self.accel = [0, self.GRAVIDADE_CONST]
        
        self.currSpeed[0] += self.accel[0] * dt
        self.currSpeed[1] += self.accel[1] * dt

        self.currSpeed[0] -= self.ATRITO[0] * self.currSpeed[0] * dt
        self.currSpeed[1] -= self.ATRITO[1] * self.currSpeed[1] * dt

        print("velocidade x: " + str(self.currSpeed[0] * dt))
        print("velocidade y: " + str(self.currSpeed[1] * dt))
        
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
        self.check_collision()
