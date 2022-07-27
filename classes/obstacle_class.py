import pygame
class obstacle(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.surf = pygame.Surface((40,40))
        self.surf.fill((100,100,110))
        self.rect = self.surf.get_rect()
        self.rect.center = pos
        self.mask = pygame.mask.from_surface(self.surf)