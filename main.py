import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((500,700))

clock = pygame.time.Clock() # define the frame per second

# to indicate that we are playing the game
playing = True

while playing:

    # fill the screen with color
    screen.fill((255,0,0))

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            playing = False

    # flip function to render the screen
    pygame.display.flip()

    # set the frames per second
    clock.tick(60)

pygame.quit()