import pygame
from config import *
from spritesheet import *

"ACHO QUE ESTÁ TUDO CERTO, FALTA COLOCAR OS NÚMEROS SOLTOS COMO VARIÁVEIS EM CONFIG (MÉDIA PRIORIDADE)"
"POUCO PROVÁVEL, MAS TALVEZ O PROBLEMA DE COLISÃO COM A PAREDE POSSA ESTAR AQUI"

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # self.image = self.game.block_sprite.get_sprite(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)  
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y