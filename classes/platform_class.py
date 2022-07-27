HEIGHT = 800
WIDTH = 800
ACC = 2
FRIC = -1
FPS = 60
import pygame
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))