import pygame

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, (0,0,0), [0,0,width,height])

        self.rect = self.image.get_rect()
    