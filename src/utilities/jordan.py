import pygame


default_scale = (75, 80) 
LARGURA = 1000
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
x_ret_3 = (LARGURA / 2) + 200
y_retangulo_3=-1
hitbox_obj= pygame.draw.rect(tela, (0, 255, 0), (x_ret_3, y_retangulo_3, 10, 20))
class Jordan:
    def __init__(self, tela, x, y, barra_de_vida, barra_de_vida_2):
        self.tela = tela
        self.rect = pygame.Rect(x, y, 75, 80) 
        self.barra_de_vida = barra_de_vida
        self.barra_de_vida = barra_de_vida
        self.barra_de_vida_2 = barra_de_vida_2
        self.image = pygame.image.load('assets/images/objetos_interagiveis/jordan.png')
        self.default_scale = (75, 80)
        self.image = pygame.transform.scale(self.image, self.default_scale)

    def colisao(self, player_rect):
        if self.rect.colliderect(player_rect):
            self.barra_de_vida.loose_health(15)

    def movimento_vertical(self, vel_y):
       self.rect.y += vel_y

    #def colocando_img(self):
     #   self.tela.blit(self.image, self.rect.topleft)  # Usando topleft para posicionar a imagem

    def limite_tela(self, ALTURA):
        return self.rect.y > ALTURA

    def object_move (self,jordan_oficial,x_ret_3,y_retangulo_3,hitbox_obj,player_rect):
        tela.blit(jordan_oficial, (x_ret_3, y_retangulo_3))  #desenho
        if hitbox_obj.colliderect(player_rect):
            self.colisao(player_rect)
        


        
 