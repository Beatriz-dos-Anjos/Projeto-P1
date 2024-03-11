import pygame

def movimento_vertical(objeto, vel_y):
    objeto.y += vel_y

def colocando_img(trofeu):
    trofeu.tela.blit(trofeu.image, (trofeu.x, trofeu.y))

def limite_tela(objeto, ALTURA):
    return objeto.y > ALTURA
