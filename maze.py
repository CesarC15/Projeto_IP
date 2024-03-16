import pygame
from Sprites import *
from Config import *

walls = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.image.load(".\img\parede2.png")
        self.image = pygame.transform.scale(self.original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * 40, y * 40)


def create_maze():
    maze = [
        "xxxxxxxxxxxxxxxxxxxx",
        "x              x   x",
        "x              x   x",
        "x        xxxxxxxxxxx",
        "x     x  x     x   x",
        "xxxxxxx  x     x   x",
        "x       x      x   x",
        "xxxxxx   xxxxx xxxxx",
        "x   x          x   x",
        "x   x          x   x",
        "x  xx          x   x",
        "x              x   x",
        "xxxxxxxxxxxxxxxxxxxx",
        "x          x       x",
        "xxxxxxxxxxxxxxxxxxxx",
    
    ]
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "x":
                wall = Wall(x, y)
                walls.add(wall)

def update(self):
        for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if self.change_x > 0:  # Movendo para a direita; colisão com a parede esquerda
                        self.rect.right = wall.rect.left
                    elif self.change_x < 0:  # Movendo para a esquerda; colisão com a parede direita
                        self.rect.left = wall.rect.right
                    elif self.change_y > 0:  # Movendo para baixo; colisão com a parede superior
                        self.rect.bottom = wall.rect.top
                    elif self.change_y < 0:  # Movendo para cima; colisão com a parede inferior
                        self.rect.top = wall.rect.bottom
