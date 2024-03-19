import pygame

class Vma:
    def __init__(self, tela, x, y, barra_de_vida, barra_de_vida_2):
        self.tela = tela
        self.rect = pygame.Rect(x, y, 75, 80)  
        self.barra_de_vida = barra_de_vida
        self.barra_de_vida_2 = barra_de_vida_2
        self.image = pygame.image.load('assets/images/objetos_interagiveis/vma.png')
        self.default_scale = (75, 80)
        self.image = pygame.transform.scale(self.image, self.default_scale)

    def colisao(self, player_rect):
        if self.rect.colliderect(player_rect):
            self.barra_de_vida.gaining_health(5)

    def movimento_vertical(self, vel_y):
        self.rect.y += vel_y

    def colocando_img(self):
        self.tela.blit(self.image, self.rect.topleft)  # Usando topleft para posicionar a imagem

    def limite_tela(self, ALTURA):
        return self.rect.y > ALTURA

        