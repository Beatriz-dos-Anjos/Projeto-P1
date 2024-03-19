import pygame
from pygame.locals import *
from utilities.animacoes import formar_lista_animacao
import sys

# A imagem vai ser repartidada em imagens menores, no caso temos uma spritesheet com todos os movimentos
# A cada movimento a gente pega exatamente o ponto y, que vai ser onde vamos recortar a nossa imagem
# Spritesheet total: 
# Tamanho X --> 1351
# Tamanho Y --> 1743
# Quantiade de sprites dentro dessa spritesh5et --> 15
# Quantidade máxima de frames por sprite --> 25
# tamanho X de cada frame --> 54,04
# tamanho Y de cada frame --> 116,2 

# Para as sprites do idle:
idle_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/idle.png")  # sprite
idle_number_frames = 7 # quantidade de frames
idle_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
idle_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
idle_posicao_x_do_corte = 54.04# onde o corte vai começar de X
idle_posicao_y_do_corte = 0 # onde o corte vai começar de Y

idle = formar_lista_animacao(
    idle_spritesheet, idle_number_frames, idle_size_of_frame_x, idle_size_of_frame_y, idle_posicao_x_do_corte, idle_posicao_y_do_corte, 2)


# Para as sprites do walk:
walk_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
walk_number_frames = 8 # quantidade de frames
walk_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
walk_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
walk_posicao_x_do_corte = 0# onde o corte vai começar de X
walk_posicao_y_do_corte = 116.2 # onde o corte vai começar de Y

walk = formar_lista_animacao(
    walk_spritesheet, walk_number_frames, walk_size_of_frame_x, walk_size_of_frame_y, walk_posicao_x_do_corte, walk_posicao_y_do_corte, 2)



# Para as sprites do jump:
jump_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
jump_number_frames = 7 # quantidade de frames
jump_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
jump_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
jump_posicao_x_do_corte = 54.04# onde o corte vai começar de X
jump_posicao_y_do_corte = 0 # onde o corte vai começar de Y

walk = formar_lista_animacao(
    walk_spritesheet, walk_number_frames, walk_size_of_frame_x, walk_size_of_frame_y, walk_posicao_x_do_corte, walk_posicao_y_do_corte, 2)


# Para as sprites do punch:
punch_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
punch_number_frames = 7 # quantidade de frames
punch_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
punch_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
punch_posicao_x_do_corte = 54.04# onde o corte vai começar de X
punch_posicao_y_do_corte = 0 # onde o corte vai começar de Y

punch = formar_lista_animacao(
    punch_spritesheet, punch_number_frames, punch_size_of_frame_x, punch_size_of_frame_y, punch_posicao_x_do_corte, punch_posicao_y_do_corte, 2)


# Para as sprites do kick:
kick_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
kick_number_frames = 7 # quantidade de frames
kick_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
kick_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
kick_posicao_x_do_corte = 54.04# onde o corte vai começar de X
kick_posicao_y_do_corte = 0 # onde o corte vai começar de Y

kick = formar_lista_animacao(
    kick_spritesheet, kick_number_frames, kick_size_of_frame_x, kick_size_of_frame_y, kick_posicao_x_do_corte, kick_posicao_y_do_corte, 2)

# Para as sprites de animação de derrota:
derrota_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
derrota_number_frames = 7 # quantidade de frames
derrota_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
derrota_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
derrota_posicao_x_do_corte = 54.04# onde o corte vai começar de X
derrota_posicao_y_do_corte = 0 # onde o corte vai começar de Y

morte = formar_lista_animacao(
    derrota_spritesheet, derrota_number_frames, derrota_size_of_frame_x, derrota_size_of_frame_y, derrota_posicao_x_do_corte, derrota_posicao_y_do_corte, 2)


# Para as sprites de animação de vitória:
vitoria_spritesheet = pygame.image.load(
    "assets/images/personagens/taylor_sprites/walk.png")
vitoria_number_frames = 7 # quantidade de frames
vitoria_size_of_frame_x = 54.04  # tamanho horizontal de cada um dos frames
vitoria_size_of_frame_y = 116.2  # tamanho vertical de cada um dos frames
vitoria_posicao_x_do_corte = 54.04# onde o corte vai começar de X
vitoria_posicao_y_do_corte = 0 # onde o corte vai começar de Y

vitoria = formar_lista_animacao(
    vitoria_spritesheet, vitoria_number_frames, vitoria_size_of_frame_x, vitoria_size_of_frame_y, vitoria_posicao_x_do_corte, vitoria_posicao_y_do_corte, 2)

# special = pygame.image.load("assets/images/personagens/kanye_sprites/special.png")

