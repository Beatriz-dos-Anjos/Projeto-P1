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
vel_y = 0.30   


duracao_obj_1 = 0
duracao_obj_2 = 0
duracao_obj_3 = 0
y_retangulo_1 = 0


y_retangulo_2 = -1  # Posicionado fora da tela
y_retangulo_3 = -1  

x_ret_1 = LARGURA / 2
x_ret_2 = (LARGURA / 2) - 200
x_ret_3 = (LARGURA / 2) + 200

objeto_lancado = False  # Indica se um objeto está atualmente em movimento
esperando_intervalo = False  # Indica se o jogo está esperando um intervalo

prox_objeto = 1  
default_scale = (75, 80)  #ajudando na escala


grammy = pygame.image.load('assets/images/objetos_interagiveis/grammy.png')
grammy_oficial = pygame.transform.scale(grammy, default_scale)
vma = pygame.image.load('assets/images/objetos_interagiveis/vma.png')
vma_oficial = pygame.transform.scale(vma, default_scale)
jordan = pygame.image.load('assets/images/objetos_interagiveis/jordan.png')
jordan_oficial = pygame.transform.scale(jordan, default_scale)

# Loop principal do jogo
while True:
    tela.fill((0, 0, 0))  # Preenche a tela com cor preta

    # Verifica se o jogo está esperando um intervalo
    if esperando_intervalo:
        # Se o intervalo terminou, redefine a flag para False
        if pygame.time.get_ticks() - tempo_inicio_intervalo >= 10000:
            esperando_intervalo = False
            fps_relogio_inicio = pygame.time.get_ticks()  

    # Jogo iniciando e objetos caindo
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

        # Atualiza a posição dos objetos em movimento e ve se saem da tela
        if objeto_lancado:
            if prox_objeto == 1:
                tela.blit(grammy_oficial, (x_ret_1, y_retangulo_1))
                y_retangulo_1 += vel_y
                hitbox_obj_1 = pygame.draw.rect(tela, (0, 255, 0), (x_ret_1, y_retangulo_1, 10, 20))
                colisao_obj_pessoas(x_ret_1,y_retangulo_1,hitbox_obj_1)
                if y_retangulo_1 > ALTURA:
                    objeto_lancado = False
                    esperando_intervalo = True
            elif prox_objeto == 2:
                tela.blit(vma_oficial, (x_ret_2, y_retangulo_2))
                y_retangulo_2 += vel_y
                hitbox_obj_1 = pygame.draw.rect(tela, (0, 255, 0), (x_ret_2, y_retangulo_2, 10, 20))
                colisao_obj_pessoas(x_ret_2,y_retangulo_2,hitbox_obj_1)
                if y_retangulo_2 > ALTURA:
                    objeto_lancado = False
                    esperando_intervalo = True
            elif prox_objeto == 3:
                tela.blit(jordan_oficial, (x_ret_3, y_retangulo_3))
                y_retangulo_3 += vel_y
                hitbox_obj_2 = pygame.draw.rect(tela, (0, 255, 0), (x_ret_3, y_retangulo_3, 10, 20))
                colisao_obj_pessoas(x_ret_3,y_retangulo_3,hitbox_obj_2)

                if y_retangulo_3 > ALTURA:
                    objeto_lancado = False
                    esperando_intervalo = True

    pygame.display.update()  # Atualiza a tela

    # Lida com eventos do pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()  # Sai do programa
