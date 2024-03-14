import pygame
from sprites import *
from config import *
from herois import *
from banco_de_dados import *
from Inimigo import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32)
        self.intro_background = pygame.image.load('./img/parede2.png')
        self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGTH))
    
    def new(self):
        self.select = True
        self.playing = True
        self.spawn = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.parede = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit the game
                self.running = False
                self.playing = False

            #move the player
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.jogador.change_speed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.jogador.change_speed(3, 0)
                elif event.key == pygame.K_UP:
                    self.jogador.change_speed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.jogador.change_speed(0, 3)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.jogador.change_speed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.jogador.change_speed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.jogador.change_speed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.jogador.change_speed(0, -3)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def game_over(self):
        pass
    
    def intro_screen(self):
        intro = True

        title = self.font.render('Jogo', True, BLACK)
        title_rect = title.get_rect(x=290, y=25)

        play_button = Button(250, 75, 150, 50, WHITE, BLACK, "JOGAR", 32)

        exit_button = Button(250, 150, 150, 50, WHITE, BLACK, "SAIR", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if exit_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self.running = False
                pygame.quit
                sys.exit()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def select_screen(self):
        select = True

        select_title = self.font.render('ESCOLHA SEU PERSONAGEM', True, 32)
        select_title_rect = select_title.get_rect(x=110, y=25)

        knight_button = Button(100, 75, 150, 50, WHITE, BLACK, "KNIGHT", 24)
        mage_button = Button(300, 75, 150, 50, WHITE, BLACK, "MAGE", 24)
        archer_button = Button(100, 275, 150, 50, WHITE, BLACK, "ARCHER", 24)
        assassin_button = Button(300, 275, 150, 50, WHITE, BLACK, "ASSASSIN", 24)

        while select:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    select = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if knight_button.is_pressed(mouse_pos, mouse_pressed):
                self.jogador = Knight(self, 1, 2)
                select = False

            if mage_button.is_pressed(mouse_pos, mouse_pressed):
                self.jogador = Mage(self, 1, 2)
                select = False
            
            if archer_button.is_pressed(mouse_pos, mouse_pressed):
                select = False
            
            if assassin_button.is_pressed(mouse_pos, mouse_pressed):
                select = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(select_title, select_title_rect)
            self.screen.blit(knight_button.image, knight_button.rect)
            self.screen.blit(mage_button.image, mage_button.rect)
            self.screen.blit(archer_button.image, archer_button.rect)
            self.screen.blit(assassin_button.image, knight_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
g = Game()
g.intro_screen()

g.new()
g.select_screen()

while g.running:
    g.main()
    g.game_over()

pygame.quit
sys.exit()