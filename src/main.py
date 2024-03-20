import pygame
from pygame.locals import *
from sys import exit
from personagens.taylor import Taylor_fighter
from personagens.kanye import Kanye_fighter
from utilities.bars import Barra_de_vida


pygame.init()

# dimensões cenário
largura = 1000
altura = 600

# janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Swift of Fightwest")

# framerate do jogo
relogio = pygame.time.Clock()
FPS = 45

# acrescentando o background
fundo = pygame.image.load('assets/images/backgrounds/cenario2.jpeg')

# Função para desenhar o background
# Essa parte do código é essencial para ser chamada no loop, pois sem ela os personagens não se movimentam, a imagem deles é desenhada


class Fundo_do_jogo():
    def __init__(self, tela, altura, largura):
        self.frame_atual = 0
        self.frame_1 = pygame.image.load('assets/images/backgrounds/cenario_movimento_1.jpg')
        self.frame_2 = pygame.image.load('assets/images/backgrounds/cenario_movimento_2.jpg')
        self.frame_3 = pygame.image.load('assets/images/backgrounds/cenario_movimento_3.jpg')
        self.frame_4 = pygame.image.load('assets/images/backgrounds/cenario_movimento_4.jpg')
        self.frame_5 = pygame.image.load('assets/images/backgrounds/cenario_movimento_5.jpg')
        self.frame_6 = pygame.image.load('assets/images/backgrounds/cenario_movimento_6.jpg')
        self.frame_7 = pygame.image.load('assets/images/backgrounds/cenario_movimento_7.jpg')
        self.frame_8 = pygame.image.load('assets/images/backgrounds/cenario_movimento_8.jpg')
        self.frame_9 = pygame.image.load('assets/images/backgrounds/cenario_movimento_9.jpg')
        self.frame_10 = pygame.image.load('assets/images/backgrounds/cenario_movimento_10.jpg')
        self.frame_11 = pygame.image.load('assets/images/backgrounds/cenario_movimento_11.jpg')
        self.frame_12 = pygame.image.load('assets/images/backgrounds/cenario_movimento_12.jpg')
        self.frame_13 = pygame.image.load('assets/images/backgrounds/cenario_movimento_12.jpg')
        self.frame_14 = pygame.image.load('assets/images/backgrounds/cenario_movimento_11.jpg')
        self.frame_15 = pygame.image.load('assets/images/backgrounds/cenario_movimento_10.jpg')
        self.frame_16= pygame.image.load('assets/images/backgrounds/cenario_movimento_9.jpg')
        self.frame_17 = pygame.image.load('assets/images/backgrounds/cenario_movimento_8.jpg')
        self.frame_18 = pygame.image.load('assets/images/backgrounds/cenario_movimento_7.jpg')
        self.frame_19 = pygame.image.load('assets/images/backgrounds/cenario_movimento_6.jpg')
        self.frame_20 = pygame.image.load('assets/images/backgrounds/cenario_movimento_5.jpg')
        self.frame_21 = pygame.image.load('assets/images/backgrounds/cenario_movimento_4.jpg')
        self.frame_22 = pygame.image.load('assets/images/backgrounds/cenario_movimento_3.jpg')
        self.frame_23 = pygame.image.load('assets/images/backgrounds/cenario_movimento_2.jpg')
        self.frame_24 = pygame.image.load('assets/images/backgrounds/cenario_movimento_1.jpg')
        self.frames = [self.frame_1,self.frame_2,self.frame_3,self.frame_4,self.frame_5,self.frame_6,self.frame_7,self.frame_8,
                       self.frame_9,self.frame_10,self.frame_11,self.frame_12,self.frame_13,self.frame_14,self.frame_15,self.frame_16,
                       self.frame_17,self.frame_18,self.frame_19,self.frame_20,self.frame_21,self.frame_22,self.frame_23,self.frame_24]
        self.time = 125
        self.last_frame_time = 0
        self.largura = largura
        self.altura = altura
        self.tela = tela

    def atualizar_frame(self):
        if pygame.time.get_ticks() - self.last_frame_time >= self.time:
            self.last_frame_time = pygame.time.get_ticks()
            if self.frame_atual < len(self.frames) - 1:
                self.frame_atual += 1
            else:
                self.frame_atual = 0

            
    def battlegorund_print(self):
        self.atualizar_frame()

        escala = pygame.transform.scale(self.frames[self.frame_atual], (self.largura, self.altura))
        self.tela.blit(escala, (0,0))


# função para testar se o player está vivo ou morto
def alive_or_die(player1_class, player1_bar, player2_class, player2_bar):
    if player1_bar.get_life() == 0:
        print("MORREU")
        player1_class.die()
        return False
    elif player2_bar.get_life() == 0:
        print("MORREU")
        player2_class.die()
        return False
    return True


def bg():
    escala = pygame.transform.scale(fundo, (largura, altura))
    tela.blit(escala, (0, 0))

tela_do_jogo = Fundo_do_jogo(tela, altura, largura)

# Criando os personagens
Taylor_Swift = Taylor_fighter(2, 700, 310) # alterei para executar teste
Kanye_West = Kanye_fighter(1, 200, 310)


# criando as barras de vida e as barras de especial dos personagens
Taylor_Swift_Bars = Barra_de_vida(2, tela)
Kanye_West_Bars = Barra_de_vida(1, tela)

#
localizacao_kanye_x, localizacao_kanye_y = 0, 0
localizacao_taylor_x, localizacao_taylor_y = 0, 0
hit_box_taylor = 0
hit_box_kanye = 0
game = True
personagem_morto = None
# loop
while True:
    relogio.tick(FPS)
    #bg()
    tela_do_jogo.battlegorund_print()
    while game == True:
        relogio.tick(FPS)
        #bg()
        tela_do_jogo.battlegorund_print()
        game = alive_or_die(Taylor_Swift, Taylor_Swift_Bars, Kanye_West, Kanye_West_Bars)
        # Interação de Combate
        Taylor_Swift.combate(tela, localizacao_kanye_x, localizacao_kanye_y, Kanye_West_Bars, Taylor_Swift_Bars, Kanye_West.is_defendendo_ou_nao())
        Kanye_West.combate(tela, localizacao_taylor_x, localizacao_taylor_y, Taylor_Swift_Bars, Kanye_West_Bars, False)

        # Movimento dos personagens
        localizacao_taylor_x, localizacao_taylor_y = Taylor_Swift.return_x_y()
        localizacao_kanye_x, localizacao_kanye_y = Kanye_West.return_x_y() # o problema deve estar aqui
        hit_box_taylor = Taylor_Swift.return_rect()
        hit_box_kanye = Kanye_West.return_rect()
        Taylor_Swift.move(largura, altura, hit_box_kanye) 
        Kanye_West.move(largura, altura, hit_box_taylor)
            # Desenhar os personagens
        Kanye_West.draw(tela)
        Taylor_Swift.draw(tela)
        # Desenhar as barras de vida
        Taylor_Swift_Bars.draw()
        Kanye_West_Bars.draw()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()  # ESTUDAR MUDAR PARA O FLIP 

    #
    #

    # Desenhar os personagens
    Kanye_West.draw(tela)
    Taylor_Swift.draw(tela)
    # Desenhar as barras de vida
    Taylor_Swift_Bars.draw() 
    Kanye_West_Bars.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()  # ESTUDAR MUDAR PARA O FLIP 
