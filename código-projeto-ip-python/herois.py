import random

class Personagem:
    def __init__(self, stats, ataques_obtidos, ataques_disponiveis):
        self.stats = stats
        self.ataques_obtidos = ataques_obtidos
        self.ataques_disponiveis = ataques_disponiveis

    #falta criar funções de se movimentar, atacar, etc.
        
class Inimigo:

    def __init__(self, stats, ataques) -> None:
        self.stats = stats
        self.ataques = ataques

        #tentativa de implementar a função de atualizar os stats por POO, não consegui ainda

        # @property
        # def stats(self):
        #     return self._stats
        
        # @stats.setter
        # def stats(self, vida_min, vida_max, ataque_min, defesa_min, range_min, range_max):
        #     total = random.randrange(range_min, range_max)
            
        #     vida = vida_min 
        #     ataque = ataque_min 
        #     defesa = defesa_min     

        #     for _ in range(total): #distribui aleatoriamente o total de pontos definido anteriormente entre os stats de "vida", "ataque" e "defesa" 
        #         indicador = random.randrange(1,3)

        #         if vida >= vida_max: #4 
        #             indicador = random.randrange(2,3)

        #         if indicador:
        #             vida += 1
        #         if indicador == 2:
        #             ataque += 1
        #         if indicador == 3:
        #             defesa += 1

        #         self._stats = {
        #             "vida": vida*50,
        #             "ataque": ataque,
        #             "defesa": defesa,
        #             "condicao": ""
        #         }
    
        #falta criar funções de se movimentar, atacar, etc. 