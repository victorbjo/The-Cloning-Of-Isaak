import pygame
from .stats_class import *
from .platform_class import *
from .projectile_class import *
vec = pygame.math.Vector2
from pygame.locals import *
from .hpSprite_class import *
import time
class healthManager(pygame.sprite.Sprite):
    def __init__(self, player, platform) -> None:
        super().__init__()
        self.hp = []
        self.player = player
        self.lastHp = player.stats.health
        self.platform = platform
        self.__updateHp()
        #For every two health draw a append a full heart
    def __updateHp(self):
        for entity in self.hp:
            entity.kill()
        self.hp = []
        print(self.player.stats.health, " Health")
        spriteSrc = "normal_full"
        for i in range(self.player.stats.maxHealth//2):
            if self.player.stats.health >= (i+1)*2:
                spriteSrc = "normal_full"
            elif self.player.stats.health == (i+1)*2-1:
                spriteSrc = "normal_half"
            else:
                spriteSrc = "normal_empty"
            self.hp.append(healthSprite(self.platform, WIDTH/WIDTH_BLOCKS+WIDTH_BLOCKS+50*i, HEIGHT/HEIGHT_BLOCKS+HEIGHT_BLOCKS, spriteSrc))
        if self.player.stats.health == 0:
            self.player.kill()
    def update(self):
        if self.player.stats.health != self.lastHp:
            
            self.lastHp = self.player.stats.health
            self.__updateHp()