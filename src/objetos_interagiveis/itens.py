import pygame
from pygame.locals import QUIT
import time

pygame.init()

pygame.display.set_caption("Aba")

LARGURA = 1000
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))

fps_relogio_inicio = pygame.time.get_ticks()
tempo_inicio_intervalo = 0

vel_y = 0.30   # A velocidade é uma só agora, pra todos os objetos

duracao_obj_1 = 0
duracao_obj_2 = 0
duracao_obj_3 = 0

y_retangulo_1 = 0
# Posicionado fora da tela
y_retangulo_2 = -1  
y_retangulo_3 = -1  

x_ret_1=LARGURA/2
x_ret_2= (LARGURA/2)-200
x_ret_3= x_ret_= (LARGURA/2)+200

objeto_lancado = False # Mesma coisa, um objeto só, pois vão ser armazenados em variáveis
esperando_intervalo = False  
prox_objeto = 1  
default_scale=(75,80)
grammy= pygame.image.load('git/grammy.png')
grammy_oficial = pygame.transform.scale(grammy,default_scale)
vma= pygame.image.load('git/vma.png')
vma_oficial= pygame.transform.scale(vma,default_scale)
jordan= pygame.image.load ('git/jordan.png')
jordan_oficial= pygame.transform.scale(jordan, default_scale)

while True:
    tela.fill((0, 0, 0))

    if esperando_intervalo:
        if pygame.time.get_ticks() - tempo_inicio_intervalo >= 10000:
            esperando_intervalo = False
            fps_relogio_inicio = pygame.time.get_ticks()  
    
    if not esperando_intervalo:
        tempo_atual = pygame.time.get_ticks() - fps_relogio_inicio
        if tempo_atual >= 10000 and not objeto_lancado:
            if prox_objeto == 1:
                duracao_obj_1 = pygame.time.get_ticks()
                objeto_lancado = True
                y_retangulo_1 = 0
                prox_objeto = 2
            elif prox_objeto == 2:
                duracao_obj_2 = pygame.time.get_ticks()
                objeto_lancado = True
                y_retangulo_2 = 0
                prox_objeto = 3
            elif prox_objeto == 3:
                duracao_obj_3 = pygame.time.get_ticks()
                objeto_lancado = True
                y_retangulo_3 = 0
                prox_objeto = 1

        if objeto_lancado:
            if prox_objeto == 1:
                tela.blit (grammy_oficial, (x_ret_1, y_retangulo_1))#.convert_alpha()
                y_retangulo_1 += vel_y
                hitbox_obj_1=pygame.draw.rect(tela,(0,255,0),(x_ret_1,y_retangulo_1,10,20))
                if y_retangulo_1 > ALTURA:
                    objeto_lancado = False
                    esperando_intervalo = True
            elif prox_objeto == 2:
                tela.blit(vma_oficial, (x_ret_2, y_retangulo_2))#.convert_alpha()
                y_retangulo_2 += vel_y
                hitbox_obj_2=pygame.draw.rect(tela,(0,255,0),(x_ret_2,y_retangulo_2,10,20))
                if y_retangulo_2 > ALTURA:
                    objeto_lancado = False
                    esperando_intervalo = True
            elif prox_objeto == 3:
                tela.blit(jordan_oficial,(x_ret_3, y_retangulo_3))#.convert_alpha()
                y_retangulo_3 += vel_y
                hitbox_obj_3=pygame.draw.rect(tela,(0,255,0),(x_ret_3,y_retangulo_3,10,20))
                if y_retangulo_3 > ALTURA:
                    objeto_lancado = False
                    esperando_intervalo = True

    pygame.display.update()  

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
