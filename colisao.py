import pygame

import sys


# Inicializar Pygame

pygame.init()


# Definir as dimensões da tela

SCREEN_WIDTH = 1920

SCREEN_HEIGHT = 1080

CELL_SIZE = 32


# Definir cores

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)


# Criar a classe do jogador

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("D:\\Users\\taf3\\Desktop\\jogo\\arqueiro.png")

        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()

        self.rect.topleft = (40, 40)


    def update(self, dx, dy):

        # Atualizar a posição do jogador-

        self.rect.x += dx

        self.rect.y += dy


        # Verificar colisão com as paredes

        for wall in walls:

            if self.rect.colliderect(wall.rect):

                if dx > 0:  # Movendo para a direita; colisão com a parede esquerda

                    self.rect.right = wall.rect.left

                elif dx < 0:  # Movendo para a esquerda; colisão com a parede direita

                    self.rect.left = wall.rect.right

                elif dy > 0:  # Movendo para baixo; colisão com a parede superior

                    self.rect.bottom = wall.rect.top

                elif dy < 0:  # Movendo para cima; colisão com a parede inferior

                    self.rect.top = wall.rect.bottom


# Criar a classe das paredes

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.original_image = pygame.image.load("D:\\Users\\taf3\\Desktop\\jogo\\parede.png")  # Carregar imagem da parede

        self.image = pygame.transform.scale(self.original_image, (40, 40))

        self.rect = self.image.get_rect()

        self.rect.topleft = (x * 40, y * 40)


# Criar o labirinto

def create_maze():

    maze = [

        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "x                                               x",
        "x                                               x",
        "x     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   xxxxxx",
        "x     x                  x       x    x        x",
        "xxxxxxx                  x            x        x",
        "x                        x            x        x",
        "x                        x       x    x        x",
        "x                        x       x    x        x",
        "x                        x       x    x        x",
        "x                        x       x    x        x",
        "x                        x       x    x        x",
        "x                        xxxxxxxxx    x        x",
        "x                                     x        x",
        "x                                              x",
        "x                                              x",
        "x                     x   xxxxxxxxx     xxxx   x",
        "x                     x   x       x        x   x",
        "x                     x   x       x        x   x",
        "x                     x   x       xxxxxxxxxx   x",
        "x                     x   x                    x",
        "x                     x   x                    x",
        "x                     x   xxxxxxxxxxxxxxxxxxxxxx",
        "x                     x                          x",
        "x                     x                          x",
        "x                     x                          x",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

    ]

    for y, row in enumerate(maze):

        for x, col in enumerate(row):

            if col == "x":

                wall = Wall(x, y)

                walls.add(wall)


# Inicializar a tela

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Labirinto")


# Criar grupos de sprites

all_sprites = pygame.sprite.Group()

walls = pygame.sprite.Group()


# Criar o jogador

player = Player()

all_sprites.add(player)


# Criar as paredes do labirinto

create_maze()

all_sprites.add(walls)


clock = pygame.time.Clock()


# Loop principal do jogo

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()


    keys = pygame.key.get_pressed()

    dx = 0

    dy = 0

    if keys[pygame.K_LEFT]:

        dx = -4

    elif keys[pygame.K_RIGHT]:

        dx = 4

    elif keys[pygame.K_UP]:

        dy = -4

    elif keys[pygame.K_DOWN]:

        dy = 4


    # Atualizar o jogador

    player.update(dx, dy)


    # Limpar a tela

    screen.fill(WHITE)


    # Desenhar os sprites

    all_sprites.draw(screen)


    # Atualizar a tela

    pygame.display.flip()


    clock.tick(60)

