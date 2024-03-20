import pygame
from pygame.locals import *
from utilities.animacoes import formar_lista_animacao
import sys


# Para as sprites do idle:
idle_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/idle.png") # sprite
idle_number_frames = 12 # quantidade de frames
idle_size_of_frame_x = 77 # tamanho horizontal de cada um dos frames
idle_size_of_frame_y = 122 # tamanho vertical de cada um dos frames

idle_p1 = formar_lista_animacao(idle_spritesheet, idle_number_frames, idle_size_of_frame_x, idle_size_of_frame_y, 1)
idle_p2 = formar_lista_animacao(idle_spritesheet, idle_number_frames, idle_size_of_frame_x, idle_size_of_frame_y, 2)



# Para as sprites do walk:
walk_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/walk.png")
walk_number_frames = 8
walk_size_of_frame_x = 77
walk_size_of_frame_y = 120

walk_p1 = formar_lista_animacao(walk_spritesheet, walk_number_frames, walk_size_of_frame_x, walk_size_of_frame_y, 1)
walk_p2 = formar_lista_animacao(walk_spritesheet, walk_number_frames, walk_size_of_frame_x, walk_size_of_frame_y, 2)


# Para as sprites do jump:
jump_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/jump.png")
jump_number_frames = 17
jump_size_of_frame_x = 115
jump_size_of_frame_y = 184

jump_p1 = formar_lista_animacao(jump_spritesheet, jump_number_frames, jump_size_of_frame_x, jump_size_of_frame_y, 1)
jump_p2 = formar_lista_animacao(jump_spritesheet, jump_number_frames, jump_size_of_frame_x, jump_size_of_frame_y, 2)


# Para as sprites do punch:
punch_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/punch.png") 
punch_number_frames = 9
punch_size_of_frame_x = 149
punch_size_of_frame_y = 125

punch_p1 = formar_lista_animacao(punch_spritesheet, punch_number_frames, punch_size_of_frame_x, punch_size_of_frame_y, 1)
punch_p2 = formar_lista_animacao(punch_spritesheet, punch_number_frames, punch_size_of_frame_x, punch_size_of_frame_y, 2)


# Para as sprites do kick:
kick_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/kick.png")
kick_number_frames = 10
kick_size_of_frame_x = 149
kick_size_of_frame_y = 125

kick_p1 = formar_lista_animacao(kick_spritesheet, kick_number_frames, kick_size_of_frame_x, kick_size_of_frame_y, 1)
kick_p2 = formar_lista_animacao(kick_spritesheet, kick_number_frames, kick_size_of_frame_x, kick_size_of_frame_y, 2)


#special = pygame.image.load("assets/images/personagens/kanye_sprites/special.png")


# Para as sprites da defesa:
defesa_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/defesa.png")
defesa_number_frames = 1
defesa_size_of_frame_x = 80
defesa_size_of_frame_y = 125

defesa = formar_lista_animacao(defesa_spritesheet, defesa_number_frames, defesa_size_of_frame_x, defesa_size_of_frame_y, 1)
