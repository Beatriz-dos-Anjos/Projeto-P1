import pygame
from pygame.locals import QUIT  #verificar se apertou o X
from sys import exit  # se sim, == saiu
import time

# depois olhar as medidas pra verificar  se o tamanho da janela estabelecida é suficiente

#lembrar que só começará a ser chamada quando a pessoa tiver sido atingida pelo soco.

pygame.init()

pygame.display.set_caption("Aba")

fps_relogio_inicio=pygame.time.get_ticks()

objeto1_lancado=False

LARGURA=800
ALTURA=600

x_retangulo_1=LARGURA/2
y_retangulo_1=0

x_retangulo_2=(LARGURA/2)+200
y_retangulo_2=0
objeto2_lancado=False

x_retangulo_3=(LARGURA/2)-200
y_retangulo_3=0

tela = pygame.display.set_mode((LARGURA,ALTURA))
vel_y1=0.49
vel_y2=0.60
vel_y3=0.63


while True: #DENTRO DO LOOP INFINITO
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type== QUIT :
            pygame.quit()
            exit()

    trofeu_1= pygame.draw.rect(tela,(255,100,0),(x_retangulo_1,y_retangulo_1,75,80))  #GRAMMY
    objeto1_lancado=True


    fps_relogio_meio=pygame.time.get_ticks()
    diferenca_ticks= fps_relogio_meio-fps_relogio_inicio

    if diferenca_ticks>=5000 and objeto1_lancado==True:  #VMA
        trofeu_2=pygame.draw.rect(tela,(0,255,0),(x_retangulo_2,y_retangulo_2,75,80))
        objeto2_lancado=True
    
        diferenca_ticks_2=pygame.time.get_ticks()-diferenca_ticks
            
        if diferenca_ticks_2>=20 and objeto2_lancado==True:
            trofeu_3=pygame.draw.rect(tela,(0,0,255),(x_retangulo_3,y_retangulo_3,70,80))
            y_retangulo_3=y_retangulo_3+vel_y3


        
    y_retangulo_1=y_retangulo_1+vel_y1 
    y_retangulo_2=y_retangulo_2+vel_y2



    if y_retangulo_1>ALTURA:
        y_retangulo_1=0

    if y_retangulo_2>ALTURA:
        y_retangulo_2=0
    
    if y_retangulo_3>ALTURA:
        y_retangulo_3=0
    
    pygame.display.update()