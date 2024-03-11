import pygame

def Movimento_vertical(objeto, vel_y):
    objeto.y += vel_y

def Colocando_img(trofeu):
    trofeu.tela.blit(trofeu.image, (trofeu.x, trofeu.y))

def Limite_tela(objeto, ALTURA):
    return objeto.y > ALTURA
