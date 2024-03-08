#stats aleatórios para o inimigo

from banco_de_dados import ataques_inimigo_1
import random
ataque_inimigo = {}

def montar_dic_inim(vida_min, vida_max, ataque_min, defesa_min, range_min, range_max): #exige o valor mínimo de vida(e máximo, para evitar batalhas que durem muito tempo), ataque e defesa do inimigo a ser gerado, além dos valores máximos e mínimos da soma de seus stats, desconsiderando mana, já que inimigos não consomem mana  
    total = random.randrange(range_min, range_max) #define aleatoriamente o total dos stats do inimigo com base nos valores máximos e mínimos exigidos na função
                                #5          #8
    vida = vida_min #2
    ataque = ataque_min #1
    defesa = defesa_min #1

    for _ in range(total): #distribui aleatoriamente o total de pontos definido anteriormente entre os stats de "vida", "ataque" e "defesa" 
        indicador = random.randrange(1,3)

        if vida >= vida_max: #4 
            indicador = random.randrange(2,3)

        if indicador == 1:
            vida += 1
        if indicador == 2:
            ataque += 1
        if indicador == 3:
            defesa += 1

    stats_inimigo = {
        "vida": vida*50,
        "ataque": ataque,
        "defesa": defesa,
        "condicao": ""
    }

    return stats_inimigo #retorna o dicionário contendo os stats do inimigo que será utilizado para o combate em turnos

def ataques_inimigo(ataques_inimigo_1, ataque_inimigo):
    for j in range(4):
        arma = random.randint(0, (len(ataques_inimigo_1) - 1))
        numero = 0
        for i in ataques_inimigo_1:
            if numero == arma:
                if i not in ataque_inimigo:
                    ataque_inimigo.update({i : ataques_inimigo_1[i]})
                else:
                    arma = (arma + 1) % len(ataques_inimigo_1)
            numero += 1
    return ataque_inimigo