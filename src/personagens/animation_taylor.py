import pygame
from pygame.locals import *
from utilities.animacoes import formar_lista_animacao
import sys


# Para as sprites do idle:
idle_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/idle.png")  # sprite
idle_number_frames = 8  # quantidade de frames
idle_size_of_frame_x = 71  # tamanho horizontal de cada um dos frames
idle_size_of_frame_y = 130  # tamanho vertical de cada um dos frames

idle = formar_lista_animacao(
    idle_spritesheet, idle_number_frames, idle_size_of_frame_x, idle_size_of_frame_y)


# Para as sprites do walk:
walk_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
walk_number_frames = 8
walk_size_of_frame_x = 81
walk_size_of_frame_y = 134

walk = formar_lista_animacao(
    walk_spritesheet, walk_number_frames, walk_size_of_frame_x, walk_size_of_frame_y)


# Para as sprites do jump:
jump_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/jump.png")
jump_number_frames = 3
jump_size_of_frame_x = 136
jump_size_of_frame_y = 184

jump = formar_lista_animacao(
    jump_spritesheet, jump_number_frames, jump_size_of_frame_x, jump_size_of_frame_y)


# Para as sprites do punch:
punch_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/punch.png")
punch_number_frames = 6
punch_size_of_frame_x = 73
punch_size_of_frame_y = 125

punch = formar_lista_animacao(
    punch_spritesheet, punch_number_frames, punch_size_of_frame_x, punch_size_of_frame_y)


# Para as sprites do kick:
kick_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/kick.png")
kick_number_frames = 5
kick_size_of_frame_x = 159
kick_size_of_frame_y = 197

kick = formar_lista_animacao(
    kick_spritesheet, kick_number_frames, kick_size_of_frame_x, kick_size_of_frame_y)


# special = pygame.image.load("assets/images/personagens/kanye_sprites/special.png")
