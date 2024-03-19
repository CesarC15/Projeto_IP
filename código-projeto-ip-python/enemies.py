from config import *
import random
import math
import pygame

"FALTA COMPLETAR AS ANIMAÇÕES E IMPLEMENTAR ATAQUES DOS INIMIGOS (MÉDIA PRIORIDADE)"

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.change_x = 0
        self.change_y = 0

        self.facing = random.choice(['LEFT', 'RIGHT'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)

        self.number = random.randint(1,4)
        if self.number == 1:
            self.image = self.game.enemy_knight_spritesheet.get_sprite(62, 54, 179, 283)
        if self.number == 2:
            self.image = self.game.enemy_mage_spritesheet.get_sprite(54, 53, 204, 285)
        if self.number == 3:
            self.image = self.game.enemy_archer_spritesheet.get_sprite(62, 53, 164, 284)
        if self.number == 4:
            self.image = self.game.enemy_assassin_spritesheet.get_sprite(77, 53, 173, 285)

        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50)

    def update(self):
        self.movement()

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.change_x = 0
        self.change_y = 0

    def movement(self):
        if self.facing == 'LEFT':
            self.change_x -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'RIGHT'
        if self.facing == 'RIGHT':
            self.change_x += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'LEFT'   

    def animate(self): #está dando erro, se der tempo ajeitar
        if self.number == 1:
            animations = [
                        self.game.enemy_knight_spritesheet.get_sprite(62, 53, 180, 283),
                        self.game.enemy_knight_spritesheet.get_sprite(310, 45, 180, 293)
                    ]
            
        if self.number == 2:
            animations = [
                        self.game.enemy_mage_spritesheet.get_sprite(54, 53, 204, 285),
                        self.game.enemy_mage_spritesheet.get_sprite(302, 45, 204, 293)
                    ]
            
        if self.number == 3:
            animations = [
                        self.game.enemy_archer_spritesheet.get_sprite(62, 53, 164, 284),
                        self.game.enemy_archer_spritesheet.get_sprite(301, 45, 164, 293)
                    ]
            
        if self.number == 4:
            animations = [
                        self.game.enemy_assassin_spritesheet.get_sprite(77, 53, 174, 285),
                        self.game.enemy_assassin_spritesheet.get_sprite(309, 45, 174, 293)
                    ]
        
        if self.facing == 'DOWN' or self.facing == 'UP' or self.facing == 'RIGHT' or self.facing == 'LEFT':
            if self.change_y == 0 and self.change_x == 0:
                if self.number == 1:
                    self.image = self.game.enemy_knight_spritesheet.get_sprite(62, 54, 180, 283)
                if self.number == 2:
                    self.image = self.game.enemy_mage_spritesheet.get_sprite(54, 53, 204, 285)
                if self.number == 3:
                    self.image = self.game.enemy_archer_spritesheet.get_sprite(62, 53, 164, 284)
                if self.number == 4:
                    self.image = self.game.enemy_assassin_spritesheet.get_sprite(77, 53, 174, 285)
            else:
                self.image = animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1