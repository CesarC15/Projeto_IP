import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32)
        self.intro_background = pygame.image.load('./img/intro_image.jpg')
        self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.select_screen_background = pygame.image.load('./img/parede2.png')
        self.select_screen_background = pygame.transform.scale(self.select_screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.enemy_spritesheet = pygame.image.load('./img/inimigo_front.png')
        self.enemy_spritesheet = pygame.transform.scale(self.enemy_spritesheet, (SCREEN_WIDTH, SCREEN_HEIGHT))
    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.parede = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        if self.select_screen() == "KNIGHT":
            self.character_spritesheet = Spritesheet('./img/cavaleiro_front.png')
            self.jogador = Player(self, 1, 2, "KNIGHT")
        if self.select_screen() == "MAGE":
            self.character_spritesheet = Spritesheet('./img/mago_front.png')
            self.jogador = Player(self, 1, 2, "MAGE")
        if self.select_screen() == "ARCHER":
            self.character_spritesheet = Spritesheet('./img/arqueiro_front.png')
            self.jogador = Player(self, 1, 2, "ARCHER")
        if self.select_screen() == "ASSASSIN":
            self.character_spritesheet = Spritesheet('./img/assassino_front.png')
            self.jogador = Player(self, 1, 2, "ASSASSIN")
        Enemy(self, 10, 10)

    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit the game
                self.running = False
                self.playing = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        qnts_keys = 0

        collectable_1 = Button(500, 435, 70, 35, WHITE, BLACK, f"CHAVES: {qnts_keys}", 12)
        self.screen.blit(collectable_1.image, collectable_1.rect)

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

        title = self.font.render('ESCAPE OUT', True, BLACK, WHITE)
        title_rect = title.get_rect(x=225, y=25)

        play_button = Button(PLAY_BUTTON_X, PLAY_BUTTON_Y, INTRO_BUTTON_WIDTH, INTRO_BUTTON_HEIGHT, WHITE, BLACK, "JOGAR", FONT_SIZE_INTRO_SCREEN)

        exit_button = Button(EXIT_BUTTON_X, EXIT_BUTTON_Y, INTRO_BUTTON_WIDTH, INTRO_BUTTON_HEIGHT, WHITE, BLACK, "SAIR", FONT_SIZE_INTRO_SCREEN)

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
        if self.running:
            select = True

            select_title = self.font.render('ESCOLHA SEU PERSONAGEM', True, FONT_SIZE_INTRO_SCREEN, WHITE)
            select_title_rect = select_title.get_rect(x = TITLE_SELECT_SCREEN_X, y = TITLE_SELECT_SCREEN_Y)

            knight_button = Button(KNIGHT_BUTTON_X, KNIGHT_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "KNIGHT", FONT_SIZE_SELECT_SCREEN)
            mage_button = Button(MAGE_BUTTON_X, MAGE_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "MAGE", FONT_SIZE_SELECT_SCREEN)
            archer_button = Button(ARCHER_BUTTON_X, ARCHER_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "ARCHER", FONT_SIZE_SELECT_SCREEN)
            assassin_button = Button(ASSASSIN_BUTTON_X, ASSASSIN_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "ASSASSIN", FONT_SIZE_SELECT_SCREEN)
            back_button = Button(BACK_BUTTON_X, BACK_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "VOLTAR", FONT_SIZE_SELECT_SCREEN)

            while select:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        select = False

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if knight_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "KNIGHT"

                if mage_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "MAGE"
                
                if archer_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "ARCHER"
                
                if assassin_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "ASSASSIN"
                
                if back_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    self.intro_screen()

                self.screen.blit(self.select_screen_background, (0,0))
                self.screen.blit(select_title, select_title_rect)
                self.screen.blit(knight_button.image, knight_button.rect)
                self.screen.blit(mage_button.image, mage_button.rect)
                self.screen.blit(archer_button.image, archer_button.rect)
                self.screen.blit(assassin_button.image, assassin_button.rect)
                self.screen.blit(back_button.image, back_button.rect)
                self.clock.tick(FPS)
                self.playing = True

                pygame.display.update()

g = Game()
g.intro_screen()
g.select_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit
sys.exit()