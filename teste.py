import pygame
from pygame.locals import *
from src.utilities.animacoes import formar_lista_animacao
import sys

# Inicializa o Pygame
pygame.init()

# Para as sprites do idle:
idle_spritesheet = pygame.image.load("assets/images/personagens/kanye_sprites/idle.png") # sprite
idle_number_frames = 12 # quantidade de frames
idle_size_of_frame_x = 77 # tamanho horizontal de cada um dos frames
idle_size_of_frame_y = 122 # tamanho vertical de cada um dos frames

idle = formar_lista_animacao(idle_spritesheet, idle_number_frames, idle_size_of_frame_x, idle_size_of_frame_y)

# Definições da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Exemplo de Animação')

# Definições da animação
frames_animacao = []  # Substitua esta lista pelos seus próprios frames
frame_atual = 0
tempo_frame = 100  # Tempo em milissegundos entre cada frame
tempo_anterior = pygame.time.get_ticks()

# Função principal do jogo
def main():
    # Loop principal do jogo
    while True:
        # Tratamento de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Atualiza a animação
        atualizar_animacao()

        # Desenha a tela
        tela.fill((0, 0, 0))
        desenhar_animacao()
        pygame.display.flip()

# Função para atualizar a animação
def atualizar_animacao():
    global frame_atual, tempo_anterior

    # Verifica se é hora de mudar para o próximo frame
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_anterior >= tempo_frame:
        frame_atual = (frame_atual + 1) % len(idle)
        tempo_anterior = tempo_atual

# Função para desenhar a animação na tela
def desenhar_animacao():
    frame = idle[frame_atual]
    tela.blit(frame, (100, 100))  # Posição onde a animação será desenhada

# Executa o jogo
if __name__ == '__main__':
    main()
