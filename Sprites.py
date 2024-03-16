from Config import *
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

        if select_character == "KNIGHT":
            self.image = pygame.image.load('.\img\cavaleiro.png')
        elif select_character == "MAGE":
            self.image = pygame.image.load('.\img\mago.png')
        elif select_character == "ARCHER":
            self.image = pygame.image.load('.\img\ arqueiro.png')
        elif select_character == "ASSASSIN":
            self.image = pygame.image.load('.\img\ assassino.png')

        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.change_x = 0
        self.change_y = 0

        self.facing = 'DOWN'

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.change_x -= PLAYER_SPEED
            self.facing = 'LEFT'
        if keys[pygame.K_RIGHT]:
            self.change_x += PLAYER_SPEED
            self.facing = 'LEFT'
        if keys[pygame.K_UP]:
            self.change_y -= PLAYER_SPEED
            self.facing = 'LEFT'
        if keys[pygame.K_DOWN]:
            self.change_y += PLAYER_SPEED
            self.facing = 'LEFT'

    def update(self):
        self.movement()

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.change_x = 0
        self.change_y = 0

    def attack(self):
        for event in pygame.event.get():
            move_attack = False
            if event.key == pygame.mouse.get_pressed()[0]:
                move_attack = True
        return move_attack

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

    # def is_above(self, pos):
    #     if self.rect.collidepoint(pos):
    #         return True
    #     return False

class Enemies:
    def __init__(self) -> None:
        pass