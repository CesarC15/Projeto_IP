#BANCO DE DADOS (STATS)
        #stats_herói = {coeficiente_de_balanceamento - soma dos stats(vida/100 e mana/10 para ser mais justo)
        #"vida" - quando chegar em 0, o jogo acaba, é perdida em combate e pode ser recuperada com moedas, uso de abilidades ou itens espalhados no mapa, o valor pode aumentar ao subir de nível
        #"mana" - consumida no uso de algumas abilidades, alguns golpes podem não ser utilizavéis se o personagem não tiver mana suficiente, pode ser recuperada com moedas ou itens espalhados no mapa, o valor pode aumentar ao subir de nível
        #"ataque" - usado no calculo de dano ao inimigo, o valor pode aumentar ao subir de nível
        #"defesa" - usado no calculo de dano ao personagem, o valor pode aumentar ao subir de nível 
        #"condição" - alguns ataques adicionam temporariamente uma condição ao personagem, pode alterar os eventos de um turno
        #"vida_total" - vida total do herói
        #}

stats_cavaleiro = {#17.0
    "vida" : 300,  
    "mana" : 30, 
    "ataque" : 4, 
    "defesa" : 7, 
    "condicao" : "", 
    "vida_total" : 300
}

stats_mago = { #19.5
    "vida" : 200,
    "mana" : 75,
    "ataque" : 7,
    "defesa" : 3,
    "condicao" : "",
    "vida_total" : 200
}

stats_arqueiro = { #17.25
    "vida" : 275, 
    "mana" : 45,
    "ataque" : 5,
    "defesa" : 5,
    "condicao" : "",
    "vida_total" : 275
}

stats_assassino = { #17.0
    "vida" : 250, 
    "mana" : 35,
    "ataque" : 8,
    "defesa" : 3,
    "condicao" : "",
    "vida_total" : 250
}


#BANCO DE DADOS (ATAQUES)
#ataque_heroi = {
#   "nome_ataque" : {
#   "dano" - usado juntamente com o stat de "ataque" do jogador e defesa do inimigo para calcular a perda de vida do inimigo ao receber o ataque
#   "precisão" - usado como porcentagem, chance do ataque acertar o inimigo
#   "custo" - número a ser subtraido do total de mana do jogador ao utilizar o golpe, o custo é aplicado mesmo se o golpe não acertar
#   "acertos" - número de vezes que o ataque será usado no mesmo turno, para cada uso deve ser calculado se o ataque acertou ou não usando a "precisão"
#   "efeito" - string de uma unica palavra, vai ser colocada no elemento "condição" do dicionario do inimigo por um turno e determinará algum efeito especial por um turno
#   }
# }

#TIPOS DE EFEITOS
# "vulnerável" - dobra a quantidade de HP que o inimigo perderá próximo turno(lembrar de não multiplicar o "dano" do ataque ou stat de "ataque" do personagem por 2, mas sim a quantidade de vida que será perdida)
# "espelhado" - quando o inimigo atacar, calcular o HP que o jogador perderia normalmente, mas aplique o valor no inimigo, o jogador não perderá HP
# "enfraquecido" - divide pela metade a quantidade de HP que o personagem perderá próximo turno (lembrar de não dividir o "dano" do ataque ou stat de "ataque" do inimigo por 2, mas sim a quantidade de vida que será perdida)
# "escondido" - reduz a precisão do ataque do personagem para 0 no próximo turno
# "fortalecido" - dobra a quantidade de HP que o personagem perderá próximo turno (lembrar de não multiplicar o "dano" do ataque ou stat de "ataque" do inimigo por 2, mas sim a quantidade de vida que será perdida)
# "distraído" - reduz o custo do próximo ataque do personagem para 0
# "abençoado" - antes de calcular o dano que o personagem receberá no turno do inimigo, aumentar a vida do jogador em 50%
# "observado" - aumenta a precisão do próximo golpe do personagem para 100
# "paralisado" - 50% de chance do inimigo não se mover próximo turno
# "cego" - reduz a precisão do próximo golpe do inimigo para 0
# "sangrando" - reduz a vida do inimigo por 25% do total de sua vida

ataques_iniciais_cavaleiro = {
    "Corte horizontal": {
        "dano": 60, 
        "precisão": 95,
        "custo": 0, 
        "acertos": 1,
        "efeito": ""
    },

    "Refletir": {
        "dano": 0, 
        "precisão": 50,
        "custo": 4,
        "acertos": 1,
        "efeito": "espelhado" 
    }
}

ataques_existentes_cavaleiro = {
    "Corte vertical": {
        "dano": 75, 
        "precisão": 75, 
        "custo": 0, 
        "acertos": 1, 
        "efeito": ""  
    },

    "Encantar lâmina": {
        "dano": 0, 
        "precisão": 100,
        "custo": 5, 
        "acertos": 1,
        "efeito": "vulnerável" 
    },

    "Cortes consecutivos": {
        "dano": 30, 
        "precisão": 85,
        "custo": 0, 
        "acertos": 2,
        "efeito": ""
    },

    "Golpe de escudo": {
        "dano": 25, 
        "precisão": 100,
        "custo": 0, 
        "acertos": 1,
        "efeito": "enfraquecido" 
    },

    "Arremesso de espada": {
        "dano": 150, 
        "precisão": 75,
        "custo": 0, 
        "acertos": 1,
        "efeito": "escondido" 
    },

    "Último corte": {
        "dano": 150, 
        "precisão": 100,
        "custo": 0, 
        "acertos": 1,
        "efeito": "fortalecido" 
    }
}

ataques_iniciais_mago = {
    "Concentrar": {
        "dano": 0, 
        "precisão": 100,
        "custo": 1, 
        "acertos": 1,
        "efeito": "distraído" 
    },

    "Orbs de luz": {
        "dano": 30, 
        "precisão": 75,
        "custo": 3, 
        "acertos": 3,
        "efeito": ""
    }
}

ataques_existentes_mago = {
    "Explosão descontrolada": {
        "dano": 150, 
        "precisão": 100,
        "custo": 20, 
        "acertos": 1,
        "efeito": ""
    },

    "Bola de fogo": {
        "dano": 75, 
        "precisão": 85,
        "custo": 3, 
        "acertos": 1,
        "efeito": ""
    },

    "Projétil guiado": {
        "dano": 55, 
        "precisão": 100,
        "custo": 2, 
        "acertos": 1,
        "efeito": ""
    },

    "Feitiço de cura": {
        "dano": 0, 
        "precisão": 100,
        "custo": 8, 
        "acertos": 1,
        "efeito": "abençoado" 
    },

    "Meditação": {
        "dano": 0, 
        "precisão": 100,
        "custo": 1, 
        "acertos": 1,
        "efeito": "vulnerável"
    },

    "Raio de luz": {
        "dano": 90, 
        "precisão": 75,
        "custo": 10, 
        "acertos": 1,
        "efeito": ""
    }
}

ataques_iniciais_arqueiro = {
    "Tiro certeiro": {
        "dano": 60, 
        "precisão": 85,
        "custo": 0, 
        "acertos": 1,
        "efeito": ""
    },

    "Mirar": {
        "dano": 0, 
        "precisão": 100,
        "custo": 3, 
        "acertos": 1,
        "efeito": "observado" 
    }
}

ataques_existentes_arqueiro = {
    "Tiro desesperado": {
        "dano": 250, 
        "precisão": 15,
        "custo": 0, 
        "acertos": 1,
        "efeito": ""
    },

    "Flecha paralisante": {
        "dano": 45, 
        "precisão": 85,
        "custo": 5, 
        "acertos": 1,
        "efeito": "paralisado" 
    },

    "Tiro duplo": {
        "dano": 45, 
        "precisão": 75,
        "custo": 0, 
        "acertos": 2,
        "efeito": ""
    },

    "Flecha guiada": {
        "dano": 55, 
        "precisão": 100,
        "custo": 2, 
        "acertos": 1,
        "efeito": ""
    },

    "Flecha envenenada": {
        "dano": 45, 
        "precisão": 85,
        "custo": 2, 
        "acertos": 1,
        "efeito": "enfraquecido"
    },

    "Acerto crítico": {
        "dano": 45, 
        "precisão": 85,
        "custo": 2, 
        "acertos": 1,
        "efeito": "vulnerável"
    }
}

ataques_iniciais_assassino = {
    "Esfaquear": {
        "dano": 60, 
        "precisão": 90,
        "custo": 0, 
        "acertos": 1,
        "efeito": ""
    },

    "Analisar": {
        "dano": 0, 
        "precisão": 100,
        "custo": 1, 
        "acertos": 1,
        "efeito": "vulnerável"
    }
}

ataques_existentes_assassino = {
    "Duplo corte": {
        "dano": 35, 
        "precisão": 85,
        "custo": 0, 
        "acertos": 2,
        "efeito": ""
    },

    "Faca envenenada": {
        "dano": 55, 
        "precisão": 90,
        "custo": 3, 
        "acertos": 1,
        "efeito": "paralisado"
    },

    "Esconder": {
        "dano": 0, 
        "precisão": 100,
        "custo": 1, 
        "acertos": 1,
        "efeito": "cego" 
    },

    "Ataque surpresa": {
        "dano": 100, 
        "precisão": 70,
        "custo": 0, 
        "acertos": 1,
        "efeito": ""
    },

    "Golpe fatal": {
        "dano": 0, 
        "precisão": 50,
        "custo": 3, 
        "acertos": 1,
        "efeito": "sangrando" 
    },

    "Múltiplos cortes": {
        "dano": 25, 
        "precisão": 60,
        "custo": 0, 
        "acertos": 5,
        "efeito": ""
    }
}