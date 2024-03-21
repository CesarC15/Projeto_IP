import pygame
from config import *
from spritesheet import *

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

        self.image = self.game.terrain_spritesheet.get_sprite(WALL_X, WALL_Y, self.width, self.height)  
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)