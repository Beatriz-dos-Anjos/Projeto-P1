import pygame
import random

class Grammy():
   def __init__(self,tela):
      self.tela=tela
      self.rect=pygame.Rect(250,0,75,80) #ajudar na colisão
      self.image_raw =  pygame.image.load('assets/images/objetos_interagiveis/grammyprincipal.png') 
      self.default_scale= (75,80)
      self.image = pygame.transform.scale(self.image_raw, self.default_scale)
      self.velocidade = 5

   def colisao (self,rect, player_rect, barra_de_vida):
        if rect.colliderect(player_rect):
            barra_de_vida.loose_health(-10)
            self.lancar_objeto()

   def movimento_vertical (self,vel_y):
        self.rect.y += vel_y

   def draw(self, rect_taylor, rect_kanye, barra_de_vida_taylor, barra_de_vida_kanye):  # a de desenhar o jordan
        self.movimento_vertical(self.velocidade)
        self.tela.blit(self.image, self.rect)
        self.colisao(self.rect, rect_kanye, barra_de_vida_kanye) # 
        self.colisao(self.rect, rect_taylor, barra_de_vida_taylor)
        self.restart_objeto()

   def limite_tela(self,ALTURA):
       return self.rect.y> ALTURA
   
   def restart_objeto(self):
       if self.rect.y > 800:
          self.rect.y = 0
          self.rect.x = random.randint(100, 900)

   def lancar_objeto(self):
       self.rect.y = 0
       self.rect.x = random.randint(100, 900)
              
                
   