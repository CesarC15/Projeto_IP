from herois import Personagem
from Inimigo import Inimigos
from banco_de_dados import *
import random

escolha = input()
nome = input()
vez = "jogador"

if escolha == 'cavaleiro':
    jogador = Personagem(stats_cavaleiro, ataques_iniciais_cavaleiro, ataques_existentes_cavaleiro)
elif escolha == 'mago':
    jogador = Personagem(stats_mago, ataques_iniciais_mago, ataques_existentes_mago) 
elif escolha == 'arqueiro':
    jogador = Personagem(stats_arqueiro, ataques_iniciais_arqueiro, ataques_existentes_arqueiro)
elif escolha == 'assassino':
    jogador = Personagem(stats_assassino, ataques_iniciais_assassino, ataques_existentes_assassino)

inimigo = Inimigos(Inimigos.montar_dic_inim(2, 4, 1, 1, 5, 8), Inimigos.ataques_inimigo(ataques_inimigo_1, Inimigos.ataque_inimigo)) #falta definir os stats e os ataques do inimigo

def combate(dic_jogador, dic_inimigo, dic_ataques_jogador, dic_ataques_inimigo, vez): #exige os dicionários contendo os stats do jogador e do inimigo, os dicionários contendo seus ataques e vez(quem atacará esse turno, o primeiro turno será de quem iniciar o combate)
    ataque_acertou = False

    if vez == "jogador":
        ataque_escolhido = input() #mudar para função do pygame que leia o ataque escolhido
        dano = 0

        if (dic_jogador.get("mana") >= dic_ataques_jogador.get(ataque_escolhido).get("custo")) or dic_inimigo.get("condicao") == "distraído":
            if dic_inimigo.get("condicao") != "distraído": #padrão, consumo de mana
                dic_jogador["mana"] = dic_jogador.get("mana") - dic_ataques_jogador.get(ataque_escolhido).get("custo") #atualiza o total de mana do personagem
            else:
                dic_jogador["condicao"] = "" #atualiza a condição do jogador

            for i in range(dic_ataques_jogador.get(ataque_escolhido).get("acertos")): #calcula quantas vezes um ataque é utilizado com base no atributo "acertos"
                if ((random.randrange(0,99) < dic_ataques_jogador.get(ataque_escolhido).get("precisão")) or (dic_inimigo.get("condicao") == "observado")) and (dic_inimigo.get("condicao") != "escondido") and (dic_jogador.get("condicao") != "cego"): #verifica se o ataque acertou o inimigo e se existem condições que afetam a precisão de golpes
                    ataque_acertou = True #necessário mais a frente para decidir se o inimigo deve receber os efeitos do golpe utilizado nesse turno

                    dano += ((dic_jogador.get("ataque")/dic_inimigo.get("defesa")) * dic_ataques_jogador.get(ataque_escolhido).get("dano")) #calcula o dano com base na razão entre ataque do jogador e defesa do oponente e atributo "dano" do ataque utilizado

            if dic_jogador.get("condicao") == "paralisado": #calcula se o jogador poderá se mover nesse turno
                if random.randrange(1,2) == 1:
                    ataque_acertou = False
                    dano = 0
                    print("Você está paralisado!") #mudar no pygame para uma caixa de dialogo

            elif dic_jogador.get("condicao") == "enfraquecido":
                dano /= 2

            elif dic_jogador.get("condicao") == "fortalecido":
                dano *= 2

            elif dic_jogador.get("condicao") == "abençoado": #um pouco confuso, mas aqui quem deve ser curado é o inimigo mesmo, já que ninguém não consegue aplicar uma condição a sí mesmo, o efeito de cura é aplicado no oponente para que no turno seguinte a cura tenha efeito antes do calculo de perda de vida
                dic_inimigo["vida"] = round(dic_inimigo.get("vida") + (dic_inimigo.get("vida total") / 2))

            elif dic_jogador.get("condicao") == "sangrando": #retira 25% do total de vida
                dic_jogador["vida"] = round(dic_jogador.get("vida") - (dic_jogador.get("vida total") / 4))

            if dic_inimigo.get("condicao") == "vulnerável":
                dano *= 2

            if dic_jogador.get("condicao") != "espelhado" and ataque_acertou: #padrão, calculo normal de perda de vida
                dic_inimigo["vida"] = round(dic_inimigo.get("vida") - dano)

                dic_inimigo["condicao"] = dic_ataques_jogador.get(ataque_escolhido).get("efeito") #novo efeito aplicado, se o ultimo golpe não tinha efeito ele é atualizado para ""

            elif ataque_acertou: #o ataque foi espelhado, logo, o personagem sofre o dano que ele dario no inimigo nesse turno, o inimigo não sofre dano
                dic_jogador["vida"] = round(dic_jogador.get("vida") - dano)

                dic_jogador["condicao"] = ""
                dic_inimigo["condicao"] = ""
 
            else: #o ataque não acertou
                dic_inimigo["condicao"] = ""
                print("O inimigo desviou!") #mudar no pygame para uma caixa de dialogo


        else: #falta de mana para utilizar o golpe escolhido
            print("Você não tem mana suficiente para usar esse golpe!") #mudar no pygame para uma caixa de dialogo
            dic_inimigo["condicao"] = ""

        if dic_inimigo.get("vida") > 0 and dic_jogador.get("vida") > 0: #recursão, próximo turno
            dic_jogador = combate(dic_jogador, dic_inimigo, dic_ataques_jogador, dic_ataques_inimigo, "inimigo")

    else: #vez do inimigo
        ataque_escolhido = input() #na versão final será escolhido aleatoriamente
        dano = 0

        for i in range(dic_ataques_inimigo.get(ataque_escolhido).get("acertos")): 
                if ((random.randrange(0,99) < dic_ataques_inimigo.get(ataque_escolhido).get("precisão")) or (dic_jogador.get("condicao") == "observado")) and (dic_jogador.get("condicao") != "escondido") and (dic_inimigo.get("condicao") != "cego"):
                    ataque_acertou = True

                    dano += ((dic_inimigo.get("ataque")/dic_jogador.get("defesa")) * dic_ataques_inimigo.get(ataque_escolhido).get("dano")) 

        if dic_inimigo.get("condicao") == "paralisado": 
            if random.randrange(1,2) == 1:
                ataque_acertou = False
                dano = 0
                print("O inimigo está paralisado!") #mudar no pygame para uma caixa de dialogo

        elif dic_inimigo.get("condicao") == "enfraquecido":
            dano /= 2

        elif dic_inimigo.get("condicao") == "fortalecido":
            dano *= 2

        elif dic_inimigo.get("condicao") == "abençoado": 
            dic_jogador["vida"] = round(dic_jogador.get("vida") + (dic_jogador.get("vida total") / 2))

        elif dic_inimigo.get("condicao") == "sangrando": #retira 25% do total de vida
            dic_inimigo["vida"] = round(dic_inimigo.get("vida") - (dic_inimigo.get("vida total") / 4))

        if dic_jogador.get("condicao") == "vulnerável":
            dano *= 2

        if dic_inimigo.get("condicao") != "espelhado" and ataque_acertou: 
            dic_jogador["vida"] = round(dic_jogador.get("vida") - dano)

            dic_jogador["condicao"] = dic_ataques_inimigo.get(ataque_escolhido).get("efeito") 

        elif ataque_acertou: #ataque espelhado
            dic_inimigo["vida"] = round(dic_inimigo.get("vida") - dano)

            dic_jogador["condicao"] = ""
            dic_inimigo["condicao"] = ""

        else: #o ataque não acertou
            dic_jogador["condicao"] = ""
            print("Você desviou!") #mudar no pygame para uma caixa de dialogo

        if dic_inimigo.get("vida") > 0 and dic_jogador.get("vida") > 0: #recursão, próximo turno
            dic_jogador = combate(dic_jogador, dic_inimigo, dic_ataques_jogador, dic_ataques_inimigo, "jogador")

    return dic_jogador