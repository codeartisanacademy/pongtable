import pygame
from paddle import Paddle
from ball import Ball
# initialize pygame
pygame.init()

# create the screen
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock() # define the frame per second

# create a paddle object from Paddle class
paddle = Paddle((0,0,0), 100, 10)
paddle.rect.x = (screen_width / 2) - (paddle.rect.width/2) # hard coded value we need to avoid this
paddle.rect.y = screen_height - 100

# create a ball 
ball = Ball((255,255,255), 10, 10)
ball.rect.x = (screen_width / 2) - (ball.rect.width/2)
ball.rect.y = 100

sprites = pygame.sprite.Group()
sprites.add(paddle)
sprites.add(ball)

# to indicate that we are playing the game
playing = True

# score variable
score = 0

while playing:

    # fill the screen with color
    screen.fill((255,0,0))

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            playing = False
        
    keys = pygame.key.get_pressed()
       
    if keys[pygame.K_LEFT]:
        paddle.move_left(5, 0)
        
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5, screen_width)

    # if the ball collides with the paddle
    if pygame.sprite.collide_mask(ball, paddle):
        
        ball.bounce()

    # if the ball hit the right wall
    if ball.rect.x >= screen.get_width():
        ball.velocity[0] = -ball.velocity[0]

    # if the ball hit the right wall
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]

    # if the ball hit top wall
    if ball.rect.y <= 0:
        score = score + 1
        print(score)
        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y >= screen_height:
        ball.stop()

    sprites.update()
    sprites.draw(screen)
    # flip function to render the screen
    

    font = pygame.font.Font(None, 60)
    text = font.render(str(score),1,(255,255,255))
    screen.blit(text, (350, 10))

    pygame.display.flip()

    # set the frames per second
    clock.tick(60)

pygame.quit()