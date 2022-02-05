import pygame

pygame.init()

screen = pygame.display.set_mode([500,700])

clock = pygame.time.Clock() # will limit to 60 frames per second

running = True

while running:
    screen.fill((0,0,255))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()