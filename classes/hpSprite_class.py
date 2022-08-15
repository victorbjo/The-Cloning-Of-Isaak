import pygame
from .stats_class import *
from .platform_class import *
from .projectile_class import *
vec = pygame.math.Vector2
from pygame.locals import *

class healthSprite(pygame.sprite.Sprite):
    def __init__(self, platform, x, y, type: str = "normal_full") -> None:
        super().__init__()
        self.hp = []
        self.image = pygame.image.load(platform.relativeDir+"/Sprites/Hearts/"+type+".png")
        self.image = self.surf = pygame.transform.scale(self.image, (HEIGHT/HEIGHT_BLOCKS*0.5, WIDTH/WIDTH_BLOCKS*0.5))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x,y)
        self.mask = pygame.mask.from_surface(self.surf)
        platform.front_sprites.add(self)
