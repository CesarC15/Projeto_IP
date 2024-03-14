from config import *
import random
import math
import pygame

class Knight(pygame.sprite.Sprite):
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
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\cavaleiro.png')
        if self.select_character == "MAGE":
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\mago.png')
        if self.select_character == "ARCHER":
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\arqueiro.png')
        if self.select_character == "ASSASSIN":
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\assassino.png')

        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.change_x = 0
        self.change_y = 0

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y
    
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

class Button:
    def __init__(self, x, y, width, heigth, fg, bg, content, fontsize):
        self.font = pygame.font.Font('arial.ttf', fontsize)
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.heigth))
        self.image.fill(self.bg)        
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.heigth/2))

        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False