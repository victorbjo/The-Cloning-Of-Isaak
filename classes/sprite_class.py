import pygame
from .stats_class import *
from .platform_class import *
vec = pygame.math.Vector2 
class sprite_movable(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.surf = pygame.transform.scale(self.image, (HEIGHT/HEIGHT_BLOCKS*0.8, WIDTH/WIDTH_BLOCKS*0.8))
        self.rect = self.image.get_rect()
        self.stats = stats()
        direction ={"up": (0,-1) , "down": (0,1), "right":(1,0), "left":(-1,0), None:(0,0)}
        self.dir = direction[None]
        self.mask = pygame.mask.from_surface(self.surf)
        self.pos = vec(pos)
        self.rect.center = self.pos
    def move(self):
        self.pos.x += self.dir[0]*self.stats.speed
        self.pos.y += self.dir[1]*self.stats.speed
        self.rect.center = self.pos  