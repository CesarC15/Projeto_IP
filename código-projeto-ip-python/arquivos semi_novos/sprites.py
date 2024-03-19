from config import *
from spritesheet import *
import math
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, select_character):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.heigth = TILESIZE
        self.select_character = select_character

        if self.select_character == "KNIGHT":
            self.image = self.game.character_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_1_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT)
        elif self.select_character == "MAGE":
            self.image = self.game.character_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_1_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT)
        elif self.select_character == "ARCHER":
            self.image = self.game.character_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_1_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT)
        elif self.select_character == "ASSASSIN":
            self.image = self.game.character_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_1_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.image.blit(self.image, self.rect)

        self.change_x = 0
        self.change_y = 0

        self.facing = 'DOWN'
        self.animation_loop = 1
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.change_x -= PLAYER_SPEED
            self.facing = 'LEFT'
        if keys[pygame.K_RIGHT]:
            self.change_x += PLAYER_SPEED
            self.facing = 'RIGHT'
        if keys[pygame.K_UP]:
            self.change_y -= PLAYER_SPEED
            self.facing = 'UP'
        if keys[pygame.K_DOWN]:
            self.change_y += PLAYER_SPEED
            self.facing = 'DOWN'
    
    def update(self):
        self.movement()
        self.animate()

        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x += self.change_x
        self.collide('x')
        self.rect.y += self.change_y
        self.collide('y')
        
        self.change_x = 0
        self.change_y = 0
    
    def attack(self):
        for event in pygame.event.get():
            move_attack = False
            if event.key == pygame.mouse.get_pressed()[0]:
                move_attack = True
        return move_attack
    
    def animate(self):
        if self.select_character == 'KNIGHT':
            down_animations = [
                            self.game.character_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_1_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT),
                            self.game.character_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_2_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_2_3_HEIGHT),
                            self.game.character_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_3_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_2_3_HEIGHT)
                            ]

        elif self.select_character == 'MAGE':
            down_animations = [
                            self.game.character_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_1_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT),
                            self.game.character_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_2_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT),
                            self.game.character_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_3_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT)
                            ]

        elif self.select_character == 'ARCHER':
            down_animations = [self.game.character_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_1_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT),
                            self.game.character_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_2_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_2_3_HEIGHT),
                            self.game.character_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_3_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_2_3_HEIGHT)]

        elif self.select_character == 'ASSASSIN':
            down_animations = [self.game.character_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_1_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT),
                            self.game.character_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_2_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_2_3_HEIGHT),
                            self.game.character_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_3_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_2_3_HEIGHT)]
        
        if self.facing == 'DOWN' or self.facing == 'UP' or self.facing == 'RIGHT' or self.facing == 'LEFT':
            if self.change_y == 0 and self.change_x == 0:
                if self.select_character == "KNIGHT":
                    self.image = self.game.character_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_1_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT)
                elif self.select_character == "MAGE":
                    self.image == self.game.character_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_1_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT)
                elif self.select_character == "ARCHER":
                    self.image = self.game.character_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_1_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT)
                elif self.select_character == "ASSASSIN":
                    self.image = self.game.character_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_1_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

    def collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.change_x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.change_x < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.change_y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.change_y < 0:
                    self.rect.y = hits[0].rect.bottom

class Enemies:
    def __init__(self) -> None:
        pass
