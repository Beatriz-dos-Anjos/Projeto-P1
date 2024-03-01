# import the biblio's and the other files
import pygame

# initiate the game 
pygame.init()

# size of the screen, Width x Height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# framerate 
FPS = 60

screen = pygame.display.set_mode(((SCREEN_WIDTH, SCREEN_HEIGHT))) # defines the size and inicialize the screen
pygame.display.set_caption("Swift of Figthye") 

# game loop
game_is_running = True

while game_is_running:
    # handle the events during the process of running the game
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_is_running = False

    # updates the screen
    pygame.display.update()

# end the game
pygame.quit