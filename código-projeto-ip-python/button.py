import pygame

"REVER O CÓDIGO, A FUNÇÃO DE GAME_OVER ESTRANHAMENTE NÃO FUNCIONA E AQUI É A ÚNICA RELAÇÃO COM A FUNÇÃO;" 
"REVER O QUE PODE ESTAR DE ERRADO POR AQUI (MÉDIA PRIORIDADE)"

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