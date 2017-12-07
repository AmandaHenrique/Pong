"""Pong game simples para 2 PLAYERS

Feito por Amanda Henrique
Para a matéria de Programação 2º Semestre

Use W,S para controlar o player 1 (vermelho)
Use UP,DOWN para controlar o player 2 (verde)

"""

import pygame
from pygame.locals import *
from pygame.constants import *
from time import sleep
from pygame.time import Clock
from pygame.mixer import Sound

largura = 700
altura = 600

pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((largura,altura))
tela
pygame.display.set_caption("Pong Game")
updateRelogio = Clock()

retCima = pygame.Rect(0,-3,700,3)
retBaixo = pygame.Rect(0,600,700,4)
retEsquerda = pygame.Rect(-3,0,3,600)
retDireita = pygame.Rect(700, 0, 4, 600)
player_verde = pygame.Rect(670,300,15,100)
player_vermelho = pygame.Rect(15,300,15,100)

fundo = pygame.image.load("background.jpg")

verdeWins1 = pygame.image.load("verdeWins1.jpg")
verdeWins2 = pygame.image.load("verdeWins2.jpg")

vermelhoWins1 = pygame.image.load("vermelhoWins1.jpg")
vermelhoWins2 = pygame.image.load("vermelhoWins2.jpg")


bolinha = pygame.Rect(largura/2,altura/2,20,20)

velocidade_bolinhaX = 4
velocidade_bolinhaY = 3

minhaFonte = pygame.font.Font("KGRedHands.ttf",50)
pontuaçao_verde = 0
pontuaçao_vermelho = 0

verde = 159,205,179
vermelho = 230,102,99

somBolinha = pygame.mixer.Sound("SomBolinha.wav")


jogando = False

def telaInical():
    alterna1 = pygame.image.load("alterna1.jpg")
    alterna2 = pygame.image.load("alterna2.jpg")
    enter = pygame.image.load("enter.jpg")

    tela.blit(alterna1, (0, 0))

    global jogando
    pisca = 1



    while jogando == False :
        tela.blit(alterna1,(0,0))
        if pisca == 1:
            tela.blit(alterna1,(0,0))
            sleep(0.5)
            pisca = 0

        elif pisca == 0:
            tela.blit(alterna2,(0,0))
            sleep(0.5)
            pisca = 1

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    jogando = True

                if jogando == True:
                    tela.blit(enter,(0,0))



            if event.type == QUIT:
                exit()

                if event.key == K_ESCAPE:
                    exit()


        pygame.display.update()


telaInical()



piscaVerde = 0
piscaVermelho = 0

while jogando == True:

    top_verde = player_verde.top
    top_vermelho = player_vermelho.top

    key = pygame.key.get_pressed()
    tela.blit(fundo,(0,0))
    textoPlayer_verde = minhaFonte.render("{}".format(pontuaçao_verde), 1, (255, 255, 255))
    textoPlayer_vermelho = minhaFonte.render("{}".format(pontuaçao_vermelho),1,(255,255,255))

    tela.blit(textoPlayer_vermelho,(240,40))
    tela.blit(textoPlayer_verde,(420,40))


    pygame.draw.rect(tela,(0,0,0),retEsquerda)
    pygame.draw.rect(tela,(0,0,0),retDireita)
    pygame.draw.rect(tela,(0,0,0),retCima)
    pygame.draw.rect(tela,(0,0,0),retBaixo)
    pygame.draw.rect(tela,(verde),player_verde)
    pygame.draw.rect(tela,(vermelho),player_vermelho)
    pygame.draw.ellipse(tela,(255,255,255),bolinha)

    bolinha.move_ip(velocidade_bolinhaX,velocidade_bolinhaY)


    if key[pygame.K_DOWN]:
        player_verde.move_ip(0,6)
    if key[pygame.K_UP]:
        player_verde.move_ip(0,-6)
    if key[pygame.K_w]:
        player_vermelho.move_ip(0,-6)
    if key[pygame.K_s]:
        player_vermelho.move_ip(0,6)



    if bolinha.colliderect(retBaixo):
        velocidade_bolinhaY = velocidade_bolinhaY * -1
    if bolinha.colliderect(retCima):
        velocidade_bolinhaY = velocidade_bolinhaY * -1


    if bolinha.colliderect(player_verde):
        velocidade_bolinhaX = velocidade_bolinhaX * -1

    if bolinha.colliderect(player_vermelho):
        velocidade_bolinhaX = velocidade_bolinhaX * -1


    if player_verde.colliderect(retCima):
        player_verde.top = top_verde
    if player_verde.colliderect(retBaixo):
        player_verde.top = top_verde
    if player_vermelho.colliderect(retCima):
        player_vermelho.top = top_vermelho
    if player_vermelho.colliderect(retBaixo):
        player_vermelho.top = top_vermelho


    if bolinha.colliderect(retEsquerda):
        pontuaçao_verde += 1
        velocidade_bolinhaX = 0
        velocidade_bolinhaY = 0
        bolinha = pygame.Rect(100,altura/2,20,20)
        velocidade_bolinhaX = 4
        velocidade_bolinhaY = 3


    if bolinha.colliderect(retDireita):
        pontuaçao_vermelho += 1
        velocidade_bolinhaX = 0
        velocidade_bolinhaY = 0
        bolinha = pygame.Rect(200,400,20,20)
        velocidade_bolinhaX = 4
        velocidade_bolinhaY = 3


    if  pontuaçao_verde == 6:
        tela.blit(verdeWins1,(0,0))
        velocidade_bolinhaX,velocidade_bolinhaY = 0,0
        if piscaVerde == 0 :
            tela.blit(verdeWins1,(0,0))
            sleep(0.5)
            piscaVerde = 1
        elif piscaVerde == 1:
            tela.blit(verdeWins2,(0,0))
            sleep(0.5)
            piscaVerde = 0


    if pontuaçao_vermelho == 6:
        tela.blit(vermelhoWins1,(0,0))
        velocidade_bolinhaX,velocidade_bolinhaY = 0,0
        if piscaVermelho == 0:
            tela.blit(vermelhoWins1,(0,0))
            sleep(0.5)
            piscaVermelho = 1
        elif piscaVermelho == 1:
            tela.blit(vermelhoWins2,(0,0))
            sleep(0.5)
            piscaVermelho = 0



    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    updateRelogio.tick(100)
    pygame.display.update()