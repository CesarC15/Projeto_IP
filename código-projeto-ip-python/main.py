import pygame
from player import *
from config import *
from button import *
from wall import *
from ground import *
from spritesheet import *
from enemies import *
import sys

"REVER O CÓDIGO, ACHO QUE TODAS AS FUNÇÕES ESTÃ FUNCIONANDO CORRETAMENTE EXCETO A FUNÇÃO DE GAME OVER (MÉDIA PRIORIDADE)" 
"A FUNÇÃO DE GAME_OVER NÃO ESTÁ FUNCIONANDO POR ALGUM MOTIVO QUALQUER COISA RETIRAMOS ELA"
"VALE RESSALTAR QUE NÃO UTILIZEI O BACKGROUND QUE CESAR FEZ POIS ESTAVA" 
"DANDO UNS ERROS ESTRANHOS COM ELA (ACHO QUE POR CONTA DO TAMANHO)"
"MAS ASSIM QUE DESCOBRIRMOS ESTE PROBLEMA MUDAMOS PARA OS SPRITES QUE CÉSAR FEZ"

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill(WHITE)
        pygame.display.set_caption("CAÇA-RATO")
        self.clock = pygame.time.Clock()

        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32)

        self.intro_background = pygame.image.load('./img/intro_image.jpg')
        self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.select_screen_background = pygame.image.load('./img/parede2.png')
        self.select_screen_background = pygame.transform.scale(self.select_screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameover_background = pygame.image.load('./img/gameover.png')

        # self.block_sprite = Spritesheet('img/select.png')
        # self.terrain_background = Spritesheet('img/parede2.png')
        self.terrain_spritesheet = Spritesheet('./img/terrain.png')
        self.enemy_knight_spritesheet = Spritesheet('./img/enemy_knight.png')

    def create_maze(self):
        for i, row in enumerate(maze):
            for j, column in enumerate(row):
                Ground(self, j, i)

                if column == 'B':
                    Wall(self, j, i)

                if column == 'E':
                    Enemy(self, j, i)

                if column == 'P':
                    if self.select_screen() == "KNIGHT":
                        self.character_spritesheet = Spritesheet('./img/cavaleiro_front.png')
                        Player(self, j, i, "KNIGHT")
                        self.attack_spritesheet = Spritesheet('./img/knight_assassin_attack.png')

                    if self.select_screen() == "MAGE":
                        self.character_spritesheet = Spritesheet('./img/mago_front.png')
                        Player(self, j, i, "MAGE")
                        self.attack_spritesheet = Spritesheet('./img/mage_attack.png')

                    if self.select_screen() == "ARCHER":
                        self.character_spritesheet = Spritesheet('./img/arqueiro_front.png')
                        Player(self, j, i, "ARCHER")
                        self.attack_spritesheet = Spritesheet('./img/archer_attack.png')

                    if self.select_screen() == "ASSASSIN":
                        self.character_spritesheet = Spritesheet('./img/assassino_front.png')
                        Player(self, j, i, "ASSASSIN")
                        self.attack_spritesheet = Spritesheet('./img/knight_assassin_attack.png')
    
    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.create_maze()
    
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
    
    def game_over(self): #algo de errado nesta função, não consegui encontrar
        game_over_screen = True
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        restart_button = Button(10, SCREEN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while game_over_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over_screen = False
                    self.running == False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                game_over_screen = False
                self.select_screen()
                self.new()
                self.main()

            self.screen.blit(self.gameover_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
    
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
