import pygame
from pygame.locals import *


class Barra_de_vida():
    def __init__(self, player, surface):
        self.player = player
        self.surface = surface
        self.rect_health = pygame.Rect(100, 70, 300, 33) if self.player == 1 else pygame.Rect(600, 40, 300, 33)
        self.rect_special = pygame.Rect(100, 108, 230, 17) if self.player == 1 else pygame.Rect(670, 78, 230, 17)
        self.life = 100
        self.alive = True
        self.special_attack = 0



    # desenha tanto a barra de vida quanto a barra de ataque especial especial
    def draw(self):
        pygame.draw.rect(self.surface, (0, 255, 0), self.rect_health)
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect_special)


    # função para a vida do personagem e a barra da vida ser atualizada
    def loose_health(self, quantidade):
        # deduz da vida a quantidade de vida que você perdeu
        # O funcionamento vai ser asim:
        # 1. A ação de combate vai comunicar uma hit box que vai ser dada como informação para uma função de colisão
        # 2. Ao mesmo tempo que qualquer evento de combate acontecer, o programa vai guardar a informação das posições x, y do personagem adversário
        # 3. A função de colisão vai verificar se a hit box do golpe está intersectando com a posição do adversário
        # 4. Se estiver intersectando, a quantidade de vida que vai ser deduzida do personagem vai ser usada como argumento dentro dessa função
        # que vai atualizar a vida do personagem, que está sendo guardada dentro do objeto dessa classe pertencente ao personagem
        self.life -= quantidade

        # garante que a vida do personagem permaneça até 0
        # comunica ao programa que o personagem morreu 
        if self.life <= 0:
            self.alive = False
            self.life = 0

        # Atualiza a largura da barra de vida proporcionalmente à vida restante
        nova_largura = (self.life / 100) * 300
        self.rect_health.width = nova_largura
        

        # o que foi feito até agora:
        # foi criada uma função para identificar colisão no arquivo functions, onde ela recebe como argumentos, a posição do jogador em que o golpe pode estar vindo,
        # recebe a posição da hitbox, a barra de vida do personagem e quanto o golpe tiraria da vida do personagem se o golpe acertasse
        # em caso de a função detectar que houve intersecção entre os retângulos, ele ativa a função loose_health
        # função ainda está em produção 
        


    # função para a vida do personagem e a barra da vida ser atualizada
    def gain_health(self, quantidade):
        # função especificamente para interagir com o gramy e o vma
        pass


    # função para a barra do especial ser atualizada 
    def loose_special(self, quantidade):
        # função para usar quando o especial for utilizado para zerar a barra de especial
        pass

    # função para a barra do especial ser atualizada 
    def gain_special(self, quantidade):
        # função que ao passo que você bate no oponente, a sua barra de especial sobre
        # guardar uma variável dentro do objeto de colisões, que indique quantas vezes você bateu no oponente, e a cada vez que subir uma vez, ela aumente na barra também
        # com uma quantidade x específica, o personagem vai ser capaz de usar o especial
        pass
