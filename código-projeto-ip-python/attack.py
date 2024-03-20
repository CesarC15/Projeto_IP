import pygame
from config import *

"NÃO TERMINEI O CÓDIGO (ALTA PRIORIDADE)"

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE

        self.animation_loop = 0

        self.image = self.game.attack_spritesheet.get_sprite()
        #continuar com o código