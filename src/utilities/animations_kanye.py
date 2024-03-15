import pygame
from pygame.locals import *
import os


# isso aqui dá load na iamgem por completo -- mas não serve, pois preciso de uma lista com as imagens
idle_full_image = pygame.image.load("assets/images/personagens/kanye_sprites/idle.png")
walk_full_image = pygame.image.load("assets/images/personagens/kanye_sprites/walk.png")
jump_full_image = pygame.image.load("assets/images/personagens/kanye_sprites/jump.png")
punch_full_image = pygame.image.load("assets/images/personagens/kanye_sprites/punch.png") 
kick_full_image = pygame.image.load("assets/images/personagens/kanye_sprites/kick.png")
#special = pygame.image.load("assets/images/personagens/kanye_sprites/special.png")


# Para as sprites do idle:
idle = []
idle_number_frames = 12
idle_size_of_frame_x = _
idle_size_of_frame_y = _

# loop para pegar cada uma das imagens individualmente
for i in range(idle_number_frames):
    corte_da_imagem = i * idle_size_of_frame_x
    imagem = idle_full_image.subsurface(pygame.Rect(corte_da_imagem, 0, idle_size_of_frame_x, idle_size_of_frame_y))
    idle.append(imagem)


# Para as sprites do walk:
walk = []
walk_number_frames = _
walk_size_of_frame_x = _
walk_size_of_frame_y = _

# loop para pegar cada uma das imagens individualmente
for i in range(walk_number_frames):
    corte_da_imagem = i * walk_size_of_frame_x
    imagem = walk_full_image.subsurface(pygame.Rect(corte_da_imagem, 0, walk_size_of_frame_x, walk_size_of_frame_y))
    walk.append(imagem)


# Para as sprites do jump:
jump = []
jump_number_frames = _
jump_size_of_frame_x = _
jump_size_of_frame_y = _

# loop para pegar cada uma das imagens individualmente
for i in range(jump_number_frames):
    corte_da_imagem = i * jump_size_of_frame_x
    imagem = jump_full_image.subsurface(pygame.Rect(corte_da_imagem, 0, jump_size_of_frame_x, jump_size_of_frame_y))
    jump.append(imagem)


# Para as sprites do punch:
punch = []
punch_number_frames = _
punch_size_of_frame_x = _
punch_size_of_frame_y = _

# loop para pegar cada uma das imagens individualmente
for i in range(punch_number_frames):
    corte_da_imagem = i * punch_size_of_frame_x
    imagem = punch_full_image.subsurface(pygame.Rect(corte_da_imagem, 0, punch_size_of_frame_x, punch_size_of_frame_y))
    punch.append(imagem)


# Para as sprites do kick:
kick = []
kick_number_frames = _
kick_size_of_frame_x = _
kick_size_of_frame_y = _

# loop para pegar cada uma das imagens individualmente
for i in range(kick_number_frames):
    corte_da_imagem = i * kick_size_of_frame_x
    imagem = kick_full_image.subsurface(pygame.Rect(corte_da_imagem, 0, kick_size_of_frame_x, kick_size_of_frame_y))
    kick.append(imagem)