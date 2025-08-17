





#Essa parte é só o código do jogo, Pode fechar essa janela se quiser.

#Use o Console em tela cheia para a melhor experiência!





















import os
import sys
import readchar
import random
import json
from colorama import Fore, Style

GG = False
jaGG = False
GO = False
LP = 3
ResultadoDia = 0
eventoDia = 0
eventoPossivel = False
PEventoPossivel = True
PeventoAtivo = False
eventoAtivo = False
dia = 0
hospedes = 12
quartos = 50
estrelas = "Seu hotel ainda não tem estrelas."
dinheiro = 10000
conf = 9
maxConf = 50
hosp = f"{hospedes}/{quartos}"
index = 0
Prespond = 0
opcoes = []
Mdinh = []
Mconf = []
eventos = ["> OK"]
diaria = 0
hospedesConf = 0
ComprarQuartos = ["Sim [-15000]", "Não"]
fimDia = False
eventoCancelado = False
cooldown = False



def recurso_caminho(rel_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)


with open(recurso_caminho('perguntas.json'), 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

perguntaEscolida = random.choice(dados)
pergunta = perguntaEscolida['Feedback']

with open(recurso_caminho('prelu_eventos.json'), 'r', encoding='utf-8') as arquivo2:
    dadosPE = json.load(arquivo2)

with open(recurso_caminho('eventos.json'), 'r', encoding='utf-8') as arquivo1:
    dadosE = json.load(arquivo1)

def sortPEvento():
    global dinheiro, conf, eventoAtivo, PEventoEscolhido, tipoPE, PEvento

    tipoPE = random.randint(0,10)


    if tipoE <= 7:
        PEventoEscolhido = random.choice(dadosPE["Ruins"])
    else:
        PEventoEscolhido = random.choice(dadosPE["Bons"])
    PEvento = PEventoEscolhido['texto']
    return tipoPE, PEventoEscolhido, PEvento

def sortEvento():
    global dinheiro, conf, eventoAtivo, EventoEscolhido, tipoE, Evento

    tipoE = random.randint(0,10)


    if tipoE <= 7:
        EventoEscolhido = random.choice(dadosE["Ruins"])
    else:
        EventoEscolhido = random.choice(dadosE["Bons"])
    Evento = EventoEscolhido['texto']
    return tipoE, EventoEscolhido, Evento






def atualizar_tela():
    global opcoes, Mdinh, Mconf, hosp, dinheiro, eventoAtivo, PeventoAtivo, LP, ResultadoDia, GO, maxConf

    os.system("clear")
    print(f"{nomeHotel}")
    print("-------------------------------")

    if GG:
        os.system("clear")
        print("TERM-INN-AL")
        print("-------------------------------")
        print(f"{Fore.GREEN}VOCÊ GANHOU!{Fore.RESET}")
        print(f"\nParabéns! {nomeHotel} chegou a 5 estrelas! Você passou por desafios, superou eventos e chegou a um patamar incrível!")
        return

    if GO:
        os.system("clear")
        print("TERM-INN-AL")
        print("-------------------------------")
        print(f"{Fore.RED}Você Perdeu!{Fore.RESET}")
        print("\nO hotel faliu. Você pode ter perdido por zerar Pontos de Liderança ou zerar conforto e hóspedes.")
        print(f"{Fore.YELLOW}Clique em STOP e RUN{Fore.RESET} para recomeçar.")
        return

    if PeventoAtivo == True:
        print("EVENTO:")
        print()
        print(PEvento)
        print()
        print(f"> {Fore.YELLOW}OK{Style.RESET_ALL}")
        return

    if eventoAtivo:
        print("EVENTO:")
        print()
        print(Evento)
        print()
        print(f"> {Fore.YELLOW}OK{Style.RESET_ALL}")
        return

    if fimDia:
        print(f"FIM DO DIA {dia - 1}")
        print("-------------------------------")
        print(f"Você ganhou ${renda}")
        print("Deseja construir mais quartos?")
        print()
        for i, x in enumerate(ComprarQuartos):
            cor = Fore.YELLOW
            print(f"{'> ' if i == index else ' '}{cor}{x}{Style.RESET_ALL}")
        if ResultadoDia == 0:
            print(f"\n{Fore.RED}VOCÊ PERDEU 1 PONTO DE LIDERANÇA POR NÃO FAZER NADA O DIA INTEIRO{Fore.RESET}")
        return


    print(f"FEEDBACK ATUAL: ({Prespond + 1} de {perguntasDia})")
    print()
    print(pergunta)
    print()

    opcoes = [opcao["Texto"] for opcao in perguntaEscolida["Opcoes"]]
    Mdinh = [opcao["Mdinh"] for opcao in perguntaEscolida["Opcoes"]]
    Mconf = [opcao["Mconf"] for opcao in perguntaEscolida["Opcoes"]]

    for i, opcao in enumerate(perguntaEscolida["Opcoes"]):
        cor = Fore.RED if dinheiro + Mdinh[i] < 0 else Fore.GREEN
        texto = opcao["Texto"]
        print(f"{ '>' if i == index else ' '} {cor}{texto}{Style.RESET_ALL}")

    print("-------------------------------")
    print("STATUS:")
    print(f"Estrelas: {estrelas}")
    print(f"Dinheiro: ${dinheiro}")
    print(f"Hóspedes: {hosp}")
    print(f"Conforto: {conf} (Máx. {maxConf})")
    print(f"Pontos de Liderança: {LP}")
    print(f"Dia: {dia}")
    hosp = f"{hospedes}/{quartos}"





def atualizar_pergunta():
    global dinheiro, conf, pergunta, perguntaEscolida, opcoes, ResultadoDia, GG
    dinheiro = dinheiro + Mdinh[index]
    conf = conf + Mconf[index]
    ResultadoDia += Mdinh[index]
    perguntaEscolida = random.choice(dados)
    pergunta = perguntaEscolida['Feedback']
    for i, opcao in enumerate(perguntaEscolida["Opcoes"]):
        texto = opcao["Texto"]
        opcoes = [texto for opcao in perguntaEscolida["Opcoes"]]

    check()
    atualizar_tela()

def atualizar_posdia():
    global dinheiro, conf, pergunta, perguntaEscolida, opcoes
    perguntaEscolida = random.choice(dados)
    pergunta = perguntaEscolida['Feedback']

def tecla_pressionada(event):
    global index, Prespond, conf, fimDia, dinheiro, Mdinh, quartos, ComprarQuartos, eventoDia, PerguntaEscolida, pergunta, opcoes, PEventoEscolhido, PeventoDia, PeventoAtivo, ResultadoDia, GG, GO
    if event == readchar.key.UP:
        if fimDia == False:
            index = (index - 1) % len(opcoes)
            atualizar_tela()
        if fimDia == True:
            index = (index - 1) % len(ComprarQuartos)
            atualizar_tela()
    elif event == readchar.key.DOWN:
        if fimDia == False:
            index = (index + 1) % len(opcoes)
            atualizar_tela()
        if fimDia == True:
            index = (index + 1) % len(ComprarQuartos)
            atualizar_tela()
    elif event == readchar.key.ENTER:

        if GO:
            os.system("clear")
            print("TERM-INN-AL")
            print("-------------------------------")
            print(f"{Fore.RED}Você Perdeu!{Fore.RESET}")
            print("\nO hotel faliu. Você pode ter perdido por zerar Pontos de Liderança ou zerar conforto e hóspedes.")
            print(f"{Fore.YELLOW}Clique em STOP e RUN{Fore.RESET} para recomeçar.")
            return

        if GG:
            GG = False
            dinheiro += 1000000
            atualizar_tela()
            return

        if PeventoAtivo:
            aplicar_evento()
            atualizar_tela()
            return

        if eventoAtivo:
            aplicar_evento()
            atualizar_tela()
            return

        if fimDia:

            if index == 0 and dinheiro >= 15000:
                dinheiro -= 15000
                quartos += 10

                fimDia = False
                check()
                atualizar_posdia()
                ResultadoDia = 0
                atualizar_tela()
            elif index == 0 and dinheiro <= 15000:
                print("\nVocê não consegue pagar isso.")
            else:

                fimDia = False
                check()
                atualizar_posdia()
                ResultadoDia = 0
                atualizar_tela()
            return

        if dinheiro + Mdinh[index] < 0:
            print("\nVocê não consegue pagar isso.")
            return


        Prespond += 1

        if Prespond >= perguntasDia:
            if eventoDia == 1:
                atualizar_pergunta()
                evento()
            elif PeventoDia == 1:
                atualizar_pergunta()
                Pevento()
            else:
                atualizar_pergunta()
                check()
                NovoDia()
                FimDiaTela()
        else:
            atualizar_pergunta()




def check():
    global estrelas, diaria, hospedesConf, hosp, conf, hospedes, quartos, dinheiro, eventoDia, eventoPossivel, PEventoPossivel, GO, GG, maxConf, jaGG


    if conf >= 90 and hospedes >= 250:
        estrelas = "* * * * *"
        diaria = 500
        eventoPossivel = True
        PEventoPossivel = False
        if jaGG:
            GG = False
        else:
            GG = True
            jaGG = True
        maxConf = 100
    elif conf >= 80 and hospedes >= 150:
        estrelas = "* * * *"
        diaria = 350
        eventoPossivel = True
        PEventoPossivel = False
        maxConf = 100
    elif conf >= 60 and hospedes >= 100:
        estrelas = "* * *"
        diaria = 300
        eventoPossivel = True
        PEventoPossivel = False
        maxConf = 75
    elif conf >= 40 and hospedes >= 50:
        estrelas = "* *"
        eventoPossivel = True
        PEventoPossivel = False
        diaria = 250
        maxConf = 60
    elif conf >= 10 and hospedes >= 10:
        estrelas = "*"
        diaria = 200
        PEventoPossivel = True
        maxConf = 50
    else:
        estrelas = "Seu hotel ainda não tem estrelas."
        diaria = 150
        PEventoPossivel = True


    hospedesConf = min(conf // 10, 10)

    if conf > maxConf:
        conf = maxConf
    if hospedes < 0:
        hospedes = 0
    if hospedes > quartos:
        hospedes = quartos

    hosp = f"{hospedes}/{quartos}"

    if dinheiro < 0:
        dinheiro = 0
    if conf < 0:
        conf = 0

    if LP <= 0:
        GO = True
        gameOver()
    if conf == 0 and hospedes == 0:
        GO = True
        gameOver()







def NovoDia():
    global perguntasDia, Prespond, eventoDia, dia, renda, dinheiro, hospedes, fim, hospedesConf, eventoCancelado, PeventoDia
    Prespond = 0
    perguntasDia = random.randint(4,6)
    if eventoPossivel == True:
        eventoDia = random.randint(0,1)
    else:
        eventoDia = 0
    if PEventoPossivel == True:
        PeventoDia = random.randint(0,1)
    else:
        PeventoDia = 0
    dia += 1
    renda = hospedes * diaria
    dinheiro = dinheiro + renda
    hospedesEntrando = random.randint(0,3) + hospedesConf
    hospedesSaindo = random.randint(0, 5)
    hospedes = hospedes + hospedesEntrando - hospedesSaindo
    fim = True
    eventoCancelado = False


def FimDiaTela():
    global Prespond, fimDia, index, ResultadoDia, LP
    os.system("clear")
    print(f"{nomeHotel}")
    print("-------------------------------")
    print(f"FIM DO DIA {dia - 1}")
    print("-------------------------------")
    print(f"Você ganhou ${renda}")
    print("Deseja construir mais quartos?")
    index = 0
    Prespond = 0
    print(" ")
    for i, x in enumerate(ComprarQuartos):
        cor = Fore.YELLOW
        print(f"{'> ' if i == index else ' '}{cor}{x}{Fore.RESET}")
    if ResultadoDia == 0:
        print(f"\n{Fore.RED}VOCÊ PERDEU 1 PONTO DE LIDERANÇA POR NÃO FAZER NADA O DIA INTEIRO{Fore.RESET}")
        LP -= 1
    fimDia = True







def evento():
    global eventoAtivo, opcoes, index, Mdinh, Mconf, hosp, dinheiro, tipoE, dinheiro, conf, hospedes, quartos, eventoDia

    eventoAtivo = True
    index = 0

    os.system("clear")
    print(f"{nomeHotel}")
    print("-------------------------------")
    print("EVENTO:")
    print("  ")
    print(Evento)
    print("  ")
    print(f"> {Fore.YELLOW}OK{Style.RESET_ALL}")
    dinheiro += EventoEscolhido["Mdinh"]
    conf += EventoEscolhido["Mconf"]
    hospedes += EventoEscolhido["hospedes"]
    quartos += EventoEscolhido["quartos"]

def Pevento():
    global PeventoAtivo, opcoes, index, Mdinh, Mconf, hosp, dinheiro, tipoPE, dinheiro, conf, hospedes, quartos, PeventoDia, PEventoEscolhido, PEvento

    PeventoAtivo = True
    index = 0

    os.system("clear")
    print(f"{nomeHotel}")
    print("-------------------------------")
    print("EVENTO:")
    print("  ")
    print(PEvento)
    print("  ")
    print(f"> {Fore.YELLOW}OK{Style.RESET_ALL}")
    dinheiro += PEventoEscolhido["Mdinh"]
    conf += PEventoEscolhido["Mconf"]
    hospedes += PEventoEscolhido["hospedes"]
    quartos += PEventoEscolhido["quartos"]


def aplicar_evento():
    global dinheiro, conf, eventoAtivo, EventoEscolhido, PeventoAtivo
    eventoAtivo = False
    PeventoAtivo = False

    sortEvento()
    sortPEvento()
    check()
    NovoDia()
    FimDiaTela()

def gameOver():
    global nomeHotel
    os.system("clear")
    print("TERM-INN-AL")
    print("-------------------------------")
    print(f"{Fore.RED}Você Perdeu!{Fore.RESET}")
    print("\nO hotel faliu. Você pode ter perdido por zerar Pontos de Liderança ou Zerar conforto e hóspedes.")
    print(f"{Fore.YELLOW}Clique em STOP e RUN{Fore.RESET} para recomeçar.")




os.system("clear")
print("TERM-INN-AL")
print()
nomeHotel = str(input("Seja bem-vindo(a) ao Term-Inn-al! Qual será o nome do seu hotel?   "))

NovoDia()
sortEvento()
sortPEvento()
check()
atualizar_tela()

while True:
    tecla = readchar.readkey()
    tecla_pressionada(tecla)
    if tecla == readchar.key.ESC:
        break
