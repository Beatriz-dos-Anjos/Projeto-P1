import pygame
from pygame.locals import *


# função de colisão entre hitbox do ataque e hitbox do inimigo --- usada para identificar colisão dos movimentos de ataque
def colisao(hitbox, player, golpe, barra_de_vida):

    # se o retângulo equivalente a hitbox e o retângulo equivalente a hitbox do personagem, vai ativar a função de loose_health
    if hitbox.colliderect(player):
        barra_de_vida.loose_health(golpe)


# função que testa para verificar se os players estão colidindo um com o outro --- usada para identificar colisão entre os personagens durante a movimentação
def is_colliding_left(hit_box_player, hit_box_opponent):

    if hit_box_opponent.colliderect(hit_box_player): # se os oponentes estiverem colidindo 

        if hit_box_player.x < hit_box_opponent.x: # se a posição x do persongem for menor que a posição x do oponente, a colisão está acontecendo à direita do personagem
            return False
        
        return True # se não, a colisão está acontecendo à direita
    
    return None