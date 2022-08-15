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
        for i in range(self.player.stats.health//2):
            self.hp.append(healthSprite(self.platform, WIDTH/WIDTH_BLOCKS+WIDTH_BLOCKS+50*i, HEIGHT/HEIGHT_BLOCKS+HEIGHT_BLOCKS))
        #If the health is odd, draw a half heart
        if(self.player.stats.health%2 == 1):
            self.hp.append(healthSprite(self.platform, WIDTH/WIDTH_BLOCKS+WIDTH_BLOCKS+50*len(self.hp), HEIGHT/HEIGHT_BLOCKS+HEIGHT_BLOCKS, "normal_half"))
        #If the health is 0, draw a empty heart
        if(self.player.stats.health == 0):
            self.hp.append(healthSprite(self.platform, WIDTH/WIDTH_BLOCKS+WIDTH_BLOCKS+50*len(self.hp), HEIGHT/HEIGHT_BLOCKS+HEIGHT_BLOCKS, "normal_empty"))
            self.player.kill()
    def update(self):
        if self.player.stats.health != self.lastHp:
            
            self.lastHp = self.player.stats.health
            self.__updateHp()