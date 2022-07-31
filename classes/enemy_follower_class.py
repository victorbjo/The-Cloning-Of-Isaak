import pygame
from .stats_class import *
from .platform_class import *
from .base_enemy_class import *
vec = pygame.math.Vector2 
class enemy_follower(enemy_base):
    def __init__(self, platform, pos, path):
        super().__init__(platform, pos, path)
        self.stats.speed = 2
        self.rect.center = (200,200)
        self.pos.x = 200
        self.pos.y = 200
    def move(self):
        direction = self.getDirection()
        oldPos = vec(self.pos.x, self.pos.y)
        self.pos.x += direction[0]*self.stats.speed
        self.pos.y += direction[1]*self.stats.speed
        oldRect = self.rect.center
        self.rect.center = self.pos  
        for entity in self.platform.all_sprites:
            if entity == self:
                continue
            offset_x = self.rect.x - entity.rect.x
            offset_y = self.rect.y - entity.rect.y
            if(entity.mask.overlap(self.mask, (offset_x, offset_y))):
                print(self.pos)
                self.rect.center = oldRect
                self.pos = oldPos
        
    def follow(self):
        print(self.platform.player.rect.center)
    def getDirection(self):
        enemyLoc = self.platform.player.pos
        loc = self.rect.center
        dir = vec(enemyLoc[0]-loc[0], enemyLoc[1]-loc[1])
        #get unitvector of dir
        dir = dir.normalize()
        return dir