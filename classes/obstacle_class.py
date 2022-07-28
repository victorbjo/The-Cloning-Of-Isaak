import pygame
from .platform_class import *
class obstacle(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.surf = pygame.Surface((HEIGHT/HEIGHT_BLOCKS, WIDTH/WIDTH_BLOCKS))
        self.surf.fill((100,100,110))
        self.rect = self.surf.get_rect()
        self.rect.topleft = pos
        self.mask = pygame.mask.from_surface(self.surf)