import pygame
from pygame.locals import *
from sys import exit
from personagens.taylor import Taylor_fighter
from personagens.kanye import Kanye_fighter
from utilities.bars import Barra_de_vida
from utilities.telainicial import *



pygame.init()

# musica de fundo

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load(
    'assets/images/sounds/ReadyForIt.mp3')

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
fundo = pygame.image.load('assets/images/background/cenario2.jpeg')

#variaveis seleçao perso
var_selecao = pygame.image.load('assets/images/background/selecao/antes_de_escolher.png').convert()

fonte = pygame.font.Font(None, 36)
branco = (255, 255, 255)

personagem_1 = fonte.render("Pressione 1 para selecionar", True, branco)
personagem_2 = fonte.render("Pressione 2 para selecionar", True, branco)


# Função para desenhar o background
# Essa parte do código é essencial para ser chamada no loop, pois sem ela os personagens não se movimentam, a imagem deles é desenhada



class Fundo_do_jogo():
    def __init__(self, tela, altura, largura):
        self.frame_atual = 0
        self.frame_1 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_1.jpg')
        self.frame_2 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_2.jpg')
        self.frame_3 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_3.jpg')
        self.frame_4 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_4.jpg')
        self.frame_5 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_5.jpg')
        self.frame_6 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_6.jpg')
        self.frame_7 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_7.jpg')
        self.frame_8 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_8.jpg')
        self.frame_9 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_9.jpg')
        self.frame_10 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_10.jpg')
        self.frame_11 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_11.jpg')
        self.frame_12 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_12.jpg')
        self.frame_13 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_12.jpg')
        self.frame_14 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_11.jpg')
        self.frame_15 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_10.jpg')
        self.frame_16 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_9.jpg')
        self.frame_17 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_8.jpg')
        self.frame_18 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_7.jpg')
        self.frame_19 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_6.jpg')
        self.frame_20 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_5.jpg')
        self.frame_21 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_4.jpg')
        self.frame_22 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_3.jpg')
        self.frame_23 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_2.jpg')
        self.frame_24 = pygame.image.load(
            'assets/images/backgrounds/cenario_movimento_1.jpg')
        self.frames = [self.frame_1, self.frame_2, self.frame_3, self.frame_4, self.frame_5, self.frame_6, self.frame_7, self.frame_8,
                       self.frame_9, self.frame_10, self.frame_11, self.frame_12, self.frame_13, self.frame_14, self.frame_15, self.frame_16,
                       self.frame_17, self.frame_18, self.frame_19, self.frame_20, self.frame_21, self.frame_22, self.frame_23, self.frame_24]
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

        escala = pygame.transform.scale(
            self.frames[self.frame_atual], (self.largura, self.altura))
        self.tela.blit(escala, (0, 0))


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

Taylor_Swift = Taylor_fighter(2, 700, 310)  # alterei para executar teste
Kanye_West = Kanye_fighter(1, 200, 310)


#remover linha pois vai ser definido na tela de selaçao

# criando as barras de vida e as barras de especial dos personagens

Taylor_Swift_Bars = Barra_de_vida(2, tela)
Kanye_West_Bars = Barra_de_vida(1, tela)


#remover linha pois vai ser definido na tela de selaçao
    
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
    # bg()
    pygame.mixer.music.play(-1)
    tela_do_jogo.battlegorund_print()
    while game == True:
        relogio.tick(FPS)
        # bg()
        tela_do_jogo.battlegorund_print()
        game = alive_or_die(Taylor_Swift, Taylor_Swift_Bars,
                            Kanye_West, Kanye_West_Bars)
        # Interação de Combate
        Taylor_Swift.combate(tela, localizacao_kanye_x, localizacao_kanye_y,
                             Kanye_West_Bars, Taylor_Swift_Bars, Kanye_West.is_defendendo_ou_nao())
        Kanye_West.combate(tela, localizacao_taylor_x, localizacao_taylor_y,
                           Taylor_Swift_Bars, Kanye_West_Bars, False)

        # Movimento dos personagens
        localizacao_taylor_x, localizacao_taylor_y = Taylor_Swift.return_x_y()
        # o problema deve estar aqui
        localizacao_kanye_x, localizacao_kanye_y = Kanye_West.return_x_y()
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



#sprites da tela inicial
logo = Logo()
start = Start()
sprites.add(logo)
sprites.add(start)

#tupla para auxilinar na seleçao de personagem
personagems = ()


#variavel para controlar as cenas
cena = "menu"

# loop
while True:
    relogio.tick(FPS)
    if cena == "menu":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'selecao'
        
        tela.blit(tela_inicial, (0,0))


        sprites.draw(tela)
        sprites.update()

    elif cena == "selecao":

        tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if 'Kanye' not in personagems:
                        var_selecao = pygame.image.load('assets/images/background/selecao/p1_kanye.png').convert()
                        tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))
                        Kanye_West = Kanye_fighter(1, 700, 310)
                        Kanye_West_Bars = Barra_de_vida(1, tela)
                        list_personagem = list(personagems)
                        list_personagem.append('Kanye')
                        personagems = tuple(list_personagem)

                elif event.key == pygame.K_2:
                    if 'Taylor' not in personagems:
                        var_selecao = pygame.image.load('assets/images/background/selecao/p2_taylor.png').convert()
                        tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))
                        Taylor_Swift = Taylor_fighter(2, 200, 310)
                        Taylor_Swift_Bars = Barra_de_vida(2, tela)
                        list_personagem = list(personagems)
                        list_personagem.append('Taylor')
                        personagems = tuple(list_personagem)

        if len(personagems) == 2:
            var_selecao = pygame.image.load('assets/images/background/selecao/escolhidos.png').convert()
            tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))
            sprites.remove(logo)
            sprites.draw(tela_selecao)
            sprites.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'jogo'

                
        
                    
        tela.blit(tela_selecao, (0,0))
        if 'Kanye' not in personagems:
            tela.blit(personagem_1, [50, 500])
        if 'Taylor' not in personagems:
            tela.blit(personagem_2, [650, 500])

    elif cena == "jogo":
        bg()
        # Interação de Combate
        Taylor_Swift.combate(tela, localizacao_kanye_x, localizacao_kanye_y, Kanye_West_Bars)
        Kanye_West.combate(tela, localizacao_taylor_x, localizacao_taylor_y, Taylor_Swift_Bars)
        # Movimento dos personagens
        localizacao_taylor_x, localizacao_taylor_y = Taylor_Swift.return_x_y()
        localizacao_kanye_x, localizacao_kanye_y = Kanye_West.return_x_y() # o problema deve estar aqui
        Taylor_Swift.move(largura, altura) 
        Kanye_West.move(largura, altura)
        # Desenhar os personagens
        Taylor_Swift.draw(tela)
        Kanye_West.draw(tela)
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

    #pygame.display.update()  # ESTUDAR MUDAR PARA O FLIP

    pygame.display.flip()  # ESTUDAR MUDAR PARA O FLIP  

