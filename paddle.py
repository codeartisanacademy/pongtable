import pygame

# our paddle inhertis from the Sprite module of pygame
class Paddle(pygame.sprite.Sprite):
        
        # __init__ is a constructor method, it will be run everytime you create an object
        # self is a required parameter if your method is inside a class
        # parameters color, width, height are the parameter we need to make our paddle
        def __init__(self, color, width, height):
            super().__init__()

            self.image = pygame.Surface([width, height])
            pygame.draw.rect(self.image, (0,0,0), [0,0, width, height] )

            self.rect = self.image.get_rect()

        
    
    