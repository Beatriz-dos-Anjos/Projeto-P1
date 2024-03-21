import pygame
from pygame.locals import *
from sys import exit
from personagens.taylor import Taylor_fighter
from personagens.kanye import Kanye_fighter
from utilities.bars import Barra_de_vida
from telas.cenario import Fundo_do_jogo
from telas.telainicial import *

#inicia o pygame
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

# variaveis seleçao perso
var_selecao = pygame.image.load(
    'assets/images/background/selecao/antes_de_escolher.png').convert()

fonte = pygame.font.Font(None, 36)
branco = (255, 255, 255)

personagem_1 = fonte.render("Pressione 1 para selecionar", True, branco)
personagem_2 = fonte.render("Pressione 2 para selecionar", True, branco)

# função para testar se o player está vivo ou morto
def alive_or_die(player1_class, player1_bar, player2_class, player2_bar):
    if player1_bar.get_life() == 0:
        print("MORREU")
        player1_class.die()
        personagem_morto = player1_class
        return personagem_morto
    elif player2_bar.get_life() == 0:
        print("MORREU")
        player2_class.die()
        personagem_morto = player2_class
        return personagem_morto
    return True

tela_do_jogo = Fundo_do_jogo(tela, altura, largura)

# Criando os personagens
Taylor_Swift = Taylor_fighter(2, 700, 310)  # alterei para executar teste
Kanye_West = Kanye_fighter(1, 200, 310)

# criando as barras de vida e as barras de especial dos personagens
Taylor_Swift_Bars = Barra_de_vida(2, tela)
Kanye_West_Bars = Barra_de_vida(1, tela)

#setando umas variavel util para o jogo
localizacao_kanye_x, localizacao_kanye_y = 0, 0
localizacao_taylor_x, localizacao_taylor_y = 0, 0

# criando os backgrounds para as telas
logo = Logo()
start = Start()
end = End()
sprites.add(logo)
sprites.add(start)
sprites.add(end)

# tupla para auxilinar na seleçao de personagem
personagems = ()


# variavel para controlar as cenas
cena = "menu"

hit_box_taylor = 0
hit_box_kanye = 0
game = True
personagem_morto = None
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

        tela.blit(tela_inicial, (0, 0))
        sprites.remove(end)
        sprites.draw(tela)
        sprites.update()

    elif cena == "selecao":

        tela_selecao = pygame.transform.scale(var_selecao, (largura, altura))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if 'Kanye' not in personagems:
                        var_selecao = pygame.image.load(
                            'assets/images/background/selecao/p1_kanye.png').convert()
                        tela_selecao = pygame.transform.scale(
                            var_selecao, (largura, altura))
                        Kanye_West = Kanye_fighter(1, 200, 310)
                        Kanye_West_Bars = Barra_de_vida(1, tela)
                        list_personagem = list(personagems)
                        list_personagem.append('Kanye')
                        personagems = tuple(list_personagem)

                elif event.key == pygame.K_2:
                    if 'Taylor' not in personagems:
                        var_selecao = pygame.image.load(
                            'assets/images/background/selecao/p2_taylor.png').convert()
                        tela_selecao = pygame.transform.scale(
                            var_selecao, (largura, altura))
                        Taylor_Swift = Taylor_fighter(2, 700, 310)
                        Taylor_Swift_Bars = Barra_de_vida(2, tela)
                        list_personagem = list(personagems)
                        list_personagem.append('Taylor')
                        personagems = tuple(list_personagem)

        if len(personagems) == 2:
            var_selecao = pygame.image.load(
                'assets/images/background/selecao/escolhidos.png').convert()
            tela_selecao = pygame.transform.scale(
                var_selecao, (largura, altura))
            sprites.remove(logo)

            sprites.draw(tela_selecao)
            sprites.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'jogo'

        tela.blit(tela_selecao, (0, 0))
        if 'Kanye' not in personagems:
            tela.blit(personagem_1, [50, 500])
        if 'Taylor' not in personagems:
            tela.blit(personagem_2, [650, 500])

    elif cena == "jogo":
        pygame.mixer.music.play(-1)
        tela_do_jogo.battlegorund_print()
        while game == True:
            relogio.tick(FPS)
            # bg()
            tela_do_jogo.battlegorund_print()
            Taylor_Swift_Bars.objetos(Taylor_Swift.rect, Kanye_West.rect, Taylor_Swift_Bars, Kanye_West_Bars) # encaixar dentro de combate
            Kanye_West_Bars.objetos(Taylor_Swift.rect, Kanye_West.rect, Taylor_Swift_Bars, Kanye_West_Bars) # encaixar dentro de combate
            game = alive_or_die(Kanye_West, Kanye_West_Bars,
                                Taylor_Swift, Taylor_Swift_Bars)
            if game == Kanye_West:
                cena = 'taylor_wins'

            elif game == Taylor_Swift:
                cena = 'kanye_wins'

            

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

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()  # ESTUDAR MUDAR PARA O FLIP

    
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
    elif cena == 'kanye_wins':
        tela_final = pygame.image.load(
                'assets/images/background/end/kanye.png').convert()
        tela_end = pygame.transform.scale(
                tela_final, (largura, altura))
        sprites.remove(start)
        sprites.add(end)
        sprites.draw(tela_end)
        sprites.update()
        Taylor_Swift_Bars.default()
        Kanye_West_Bars.default()
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'menu'
                    sprites.add(logo)
                    sprites.add(start)
                    personagems = ()       
                    var_selecao = pygame.image.load(
                        'assets/images/background/selecao/antes_de_escolher.png').convert()
                    game = True
        
        tela.blit(tela_end, (0, 0))



    elif cena == 'taylor_wins':
        tela_final = pygame.image.load(
                'assets/images/background/end/swift.png').convert()
        tela_end = pygame.transform.scale(
                tela_final, (largura, altura))
        sprites.remove(start)
        sprites.add(end)
        sprites.draw(tela_end)
        sprites.update()
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'menu'
                    sprites.add(logo)
                    sprites.add(start)
                    personagems = ()     
                    var_selecao = pygame.image.load(
                        'assets/images/background/selecao/antes_de_escolher.png').convert()

                    game = True
        
        tela.blit(tela_end, (0, 0))



    pygame.display.flip()  # ESTUDAR MUDAR PARA O FLIP
    # bg()
