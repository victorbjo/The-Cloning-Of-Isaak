import pygame
from .stats_class import *
from .platform_class import *
from .sprite_class import *
vec = pygame.math.Vector2 
class enemy_base(sprite_movable):
    def __init__(self, platform, pos, path):
        super().__init__(pos, path)
        self.platform = platform
        self.platform.movable_sprites.add(self)
        self.platform.all_sprites.add(self)
        self.platform.obstacles.add(self)
        self.health = 10
    def update_state():
        pass
    def take_damage(self, damage):
        self.health -= damage
        if self.health <=0:
            self.kill()