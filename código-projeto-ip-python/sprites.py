from config import *
import math
import pygame

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(WHITE)

        return sprite

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
            self.image = self.game.character_spritesheet.get_sprite(422, 46, 195, 298)
        elif self.select_character == "MAGE":
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\mago.png')
        elif self.select_character == "ARCHER":
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\arqueiro.png')
        elif self.select_character == "ASSASSIN":
            self.image = pygame.image.load(r'C:\Users\João Pedro\OneDrive\Documentos\código-projeto-ip-python\img\assassino.png')

        

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.change_x = 0
        self.change_y = 0

        self.facing = 'DOWN'
        self.animation_loop = 1

        self.image.blit(self.image, self.rect)

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
        self.rect.y += self.change_y
        
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
            down_animations = [self.game.character_spritesheet.get_sprite(422, 46, 195, 298),
                            self.game.character_spritesheet.get_sprite(175, 46, 195, 315),
                            self.game.character_spritesheet.get_sprite(669, 46, 195, 315)]

            # up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

            # left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

            # right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.select_character == 'MAGE':
            down_animations = [self.game.character_spritesheet.get_sprite(422, 46, 195, 298),
                            self.game.character_spritesheet.get_sprite(175, 46, 195, 315),
                            self.game.character_spritesheet.get_sprite(669, 46, 195, 315)]

            # up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

            # left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

            # right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.select_character == 'ARCHER':
            down_animations = [self.game.character_spritesheet.get_sprite(422, 46, 195, 298),
                            self.game.character_spritesheet.get_sprite(175, 46, 195, 315),
                            self.game.character_spritesheet.get_sprite(669, 46, 195, 315)]

            # up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

            # left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

            # right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.select_character == 'ASSASSIN':
            down_animations = [self.game.character_spritesheet.get_sprite(422, 46, 195, 298),
                            self.game.character_spritesheet.get_sprite(175, 46, 195, 315),
                            self.game.character_spritesheet.get_sprite(669, 46, 195, 315)]

            # up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
            #                  self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

            # left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
            #                    self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

            # right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
            #                     self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]
        
        if self.facing == 'DOWN' or self.facing == 'UP' or self.facing == 'RIGHT' or self.facing == 'LEFT':
            if self.change_y == 0 and self.change_x == 0:
                self.image = self.game.character_spritesheet.get_sprite(422, 46, 195, 298)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

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