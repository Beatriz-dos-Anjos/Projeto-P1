import pygame
from pygame.locals import *
from utilities.fight_commands import combate
from utilities.movimentacao import move
from personagens.animation_taylor import idle


class Taylor_fighter():
    def __init__(self, player, x, y):
        self.player = player
        self.rect = pygame.Rect(x, y, 80, 180)
        self.animations = [idle, walk, jump, punch, kick]
        self.current_animation = 0
        self.current_animation_frame = 0
        self.is_attacking_or_jumping = False
        self.attacking_type = None
        self.is_moving = False
        self.is_performming_attack = False
        self.time_animation = 50
        self.last_time_animation = 0
        self.speed = 0
        self.ground = True
        self.last_attack_time = 0
        self.facing_left = True if self.player == 2 else False

    def combate(self, surface, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente, barra_de_vida_player):
        attacking_countdown = 2000
        # Temporizador para o personagem só poder atacar de 2 em 2 segundos
        # confere se o tempo de execução do jogo subtraindo o tempo do último ataque realizado é maior ou igual ao countdown especulado
        if pygame.time.get_ticks() - self.last_attack_time >= attacking_countdown:
            self.last_attack_time, self.attacking_type = combate(
                self.rect, self.player, surface, self.facing_left, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente, barra_de_vida_player, self.attacking_type)

    def move(self, largura, altura, inimigo):
        self.facing_left, self.ground, self.speed, self.is_moving = move(
            self.rect, self.player, self.facing_left, self.ground, self.speed, largura, altura, inimigo, self.is_moving)

    def return_x_y(self):
        return (self.rect.x, self.rect.y)

    def return_rect(self):
        return self.rect

    def draw(self, surface):

        self.atualizar_animacao()
        surface.blit(self.animations[self.current_animation]
                     [self.current_animation_frame], self.rect.topleft)

        # pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def atualizar_animacao(self):

        # feita para fazer com que os frames passem após um cooldown de tempo entre cada uma das animações
        if pygame.time.get_ticks() - self.last_time_animation >= self.time_animation:

            # guarda o momento do último frame
            self.last_time_animation = pygame.time.get_ticks()

            # Troca para a animação de soco
            if self.attacking_type == 1 and self.is_performming_attack == False:
                self.current_animation = 3  # punch
                self.current_animation_frame = 0
                self.is_moving = False
                self.is_performming_attack = True

            if self.attacking_type == 2 and self.is_performming_attack == False:
                self.current_animation = 4  # kick
                self.current_animation_frame = 0
                self.is_moving = False
                self.is_performming_attack = True

            # se o botão de andar for pressionado a animação passa a ser a de
            elif self.is_moving == True and self.is_performming_attack == False and self.current_animation != 1:
                self.current_animation = 1  # walk
                self.current_animation_frame = 0
                self.is_moving = True

            elif self.is_moving == False and self.is_performming_attack == False and self.current_animation != 0:
                self.current_animation = 0  # idle
                self.current_animation_frame = 0

            # confere se a última animação acabou
            if self.current_animation_frame >= len(self.animations[self.current_animation]) - 1:

                # confere se o botão de andar continua sendo pressionado:: se continuar --> o movimento continua
                if self.is_moving == True:
                    self.current_animation = 1
                    self.current_animation_frame = 0

                # se não a animação volta ao IDLE
                else:
                    self.current_animation = 0
                    self.current_animation_frame = 0

                self.attacking_type = 0
                self.is_performming_attack = False

            # se não tiver acabado passa para o próximo fram da animação
            else:

                # confere se o botão de andar parou de ser pressionado:: se parar --> o movimento de andar para
                if self.is_moving == False and self.is_performming_attack == False and self.current_animation != 0:
                    self.current_animation = 0
                    self.current_animation_frame = 0

                # Pula para o próximo quadro de frame da animação
                else:
                    self.current_animation_frame = self.current_animation_frame + 1
