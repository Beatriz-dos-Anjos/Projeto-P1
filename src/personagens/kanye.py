import pygame
from pygame.locals import *
from utilities.fight_commands import combate
from utilities.movimentacao import move
#from utilities.animations_kanye import
from personagens.animations_kanye import idle_p1, idle_p2, walk_p1, walk_p2, jump_p1, jump_p2, punch_p1, punch_p2, kick_p1, kick_p2, defesa



class Kanye_fighter():
    def __init__(self, player, x, y):
        self.player = player
        self.rect = pygame.Rect(x, y, 145, 240)
        self.animations = [idle_p1, walk_p1, jump_p1, punch_p1, kick_p1] if self.player == 1 else [idle_p2, walk_p2, jump_p2, punch_p2, kick_p2]
        self.animation_defending = pygame.transform.scale(pygame.image.load("assets/images/personagens/kanye_sprites/defesa.png"), (80 * 2, 125 * 2))
        self.current_animation = 0
        self.current_animation_frame = 0
        self.is_attacking_or_jumping = False
        self.attacking_type = None
        self.is_moving = False
        self.is_performming_attack = False
        self.time_animation = 75
        self.last_time_animation = 0
        self.speed = 0
        self.attacking = False
        self.block = False # flag para travar execução do player ao executar qualquer movimento de combate
        self.is_defending = False
        self.ground = True
        self.facing_left = True if self.player == 2 else False


    def combate(self, surface, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente, barra_de_vida_player, defendendo_ou_nao):
        # Temporizador para o personagem só poder atacar quando ele não estiver executando outro movimento de ataque
        if self.is_performming_attack == False and self.attacking == False: 
            self.attacking, self.attacking_type, self.is_defending = combate(self.rect, self.player, surface, posicao_oponente_x, posicao_oponente_y, barra_de_vida_oponente, barra_de_vida_player, defendendo_ou_nao) 
            

    def move(self, largura, altura, inimigo):
        self.ground, self.speed, self.is_moving = move(self.rect, self.player, self.ground, self.speed, largura, altura, inimigo, self.is_moving, self.block)


    def return_x_y(self):
        return (self.rect.x, self.rect.y)


    def return_rect(self):
        return self.rect


    def draw(self, surface):

        self.atualizar_animacao()
        if self.is_defending == True:
            surface.blit(self.animation_defending, self.rect.topleft)
            self.is_moving = False
            self.block = True
        else:
            surface.blit(self.animations[self.current_animation][self.current_animation_frame], self.rect.topleft)

        #pygame.draw.rect(surface, (255, 0, 0), self.rect)


    def atualizar_animacao(self):

        # feita para fazer com que os frames passem após um cooldown de tempo entre cada uma das animações
        if pygame.time.get_ticks() - self.last_time_animation >= self.time_animation:

            self.last_time_animation = pygame.time.get_ticks() # guarda o momento do último frame
            
            # Troca para a animação de soco
            if self.attacking_type == 1 and self.is_performming_attack == False and self.is_defending == False:
                self.current_animation = 3 # punch
                self.current_animation_frame = 0
                self.is_moving = False
                self.is_performming_attack = True
                self.block = True
                # execução será travada

            if self.attacking_type == 2 and self.is_performming_attack == False and self.is_defending == False:
                self.current_animation = 4 # kick
                self.current_animation_frame = 0
                self.is_moving = False
                self.is_performming_attack = True
                self.block = True
                # execução será travada

            # se o botão de andar for pressionado a animação passa a ser a de 
            elif self.is_moving == True and self.is_performming_attack == False and self.current_animation != 1:
                self.current_animation = 1 # walk
                self.current_animation_frame = 0
                self.is_moving = True
            
            elif self.is_moving == False and self.is_performming_attack == False and self.current_animation != 0:
                self.current_animation = 0 #idle
                self.current_animation_frame = 0
                self.block = False

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
                self.attacking = False
                self.block = False
                # execução vai destravar aqui

            # se não tiver acabado passa para o próximo fram da animação 
            else:

                # confere se o botão de andar parou de ser pressionado:: se parar --> o movimento de andar para
                if self.is_moving == False and self.is_performming_attack == False and self.current_animation != 0:
                    self.current_animation = 0
                    self.current_animation_frame = 0
                
                # Pula para o próximo quadro de frame da animação
                else:
                    self.current_animation_frame = self.current_animation_frame + 1
    

    def is_defendendo_ou_nao(self):
        return self.is_defending
    

    def die(self): # animação usada quando o personagem perde
        pass
    # vai passar uma animação que o personagem perde, ele vai animar e mover o personagem correndo para fora da tela
    # vai comunicar assim:
    # No main vai puxar o get_life()
    # O código de luta acontece enquanto get_life() de ambos os jogadores forem diferentes de 0
    # Quando bater 0 quebra o laço de repetição e manda a animação de perder 
    # (essa animação aqui) --> personagem correndo para fora da tela
    # depois o outro comemora de alguma forma
    # mostra uma tela de configuração porque acabou o jogo
    # aúdio que vai ter que indica fim do combate
            
        


                