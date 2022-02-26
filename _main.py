import pygame
from paddle import Paddle

# initialize pygame
pygame.init()

screen_width = 500
screen_height = 700
# create the screen
screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock() # define the frame per second


paddle = Paddle((255,255,255), 100,10)
paddle.rect.x = (screen_width / 2) - (paddle.rect.width/2) # hard coded value we need to avoid this
paddle.rect.y = screen_height - 100

sprites = pygame.sprite.Group()
sprites.add(paddle)
# to indicate that we are playing the game
playing = True

while playing:

    # fill the screen with col  or
    screen.fill((255,0,0))
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            playing = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5, screen_width)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5, screen_width)

    sprites.update()
    sprites.draw(screen)
    # flip function to render the screen
    pygame.display.flip()

    # set the frames per second
    clock.tick(60)

pygame.quit()