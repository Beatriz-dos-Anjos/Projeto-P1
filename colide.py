import pygame
from pygame.locals import *
def colisao_obj_pessoas (player, rect, barra_de_vida,hitbox_obj_1,hitbox_obj_2,posicao,posicao_oponente_x,posicao_oponente_y):
    qtd_ganha=5
    quantidade=-15
    colisao_obj_p=False
    if player==1:
        #oponente
        if hitbox_obj_1.colliderect(posicao_oponente_x) and hitbox_obj_1.colliderect(posicao_oponente_y):  #ganha vida
            barra_de_vida.gaining_health(qtd_ganha)
            colisao_obj_p=True
        if hitbox_obj_2.colliderect(posicao_oponente_x) and hitbox_obj_1.colliderect(posicao_oponente_y): #perde vida
            barra_de_vida.loose_health(quantidade) 
            colisao_obj_p=True

        
        #ele

        if hitbox_obj_1.colliderect(rect.x):  
            barra_de_vida.gaining_health(qtd_ganha)
            colisao_obj_p=True
             #adiciona vida
        if hitbox_obj_2.colliderect(rect.y):
            barra_de_vida.loose_health(quantidade)
            colisao_obj_p=True
 
        
    if player==2:
        #oponente
        if hitbox_obj_1.colliderect(posicao_oponente_x) and hitbox_obj_1.colliderect(posicao_oponente_y):
            barra_de_vida.gaining_health(qtd_ganha)
            colisao_obj_p=True

        if hitbox_obj_2.colliderect(posicao_oponente_x) and hitbox_obj_1.colliderect(posicao_oponente_y):
            barra_de_vida.loose_health(quantidade)
            colisao_obj_p=True
        

        #ele

        if hitbox_obj_1.colliderect(rect.x):  
            barra_de_vida.gaining_health(qtd_ganha)
            colisao_obj_p=True

            #adiciona vida
        if hitbox_obj_2.colliderect(rect.y): 
            barra_de_vida.gaining_health(quantidade)
            colisao_obj_p=True 

        return colisao_obj_p