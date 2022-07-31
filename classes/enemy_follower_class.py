from platform import platform
import pygame
from .stats_class import *
from .platform_class import *
from .base_enemy_class import *
vec = pygame.math.Vector2 
class enemy_follower(enemy_base):
    def __init__(self, platform, pos, path):
        super().__init__(platform, pos, path)
        self.stats.speed = 1
        self.rect.center = (200,200)
        self.pos.x = 200
        self.pos.y = 200
    def move(self): #This needs to be redone
        direction = self.getDirection(self.platform.player.pos)
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
                self.rect.center = oldRect
                self.pos = oldPos
                newDir = self.follow()
                self.pos.x += newDir[0]*self.stats.speed
                self.pos.y += newDir[1]*self.stats.speed
                self.rect.center = self.pos  
                #Check again for collision. If collision follow same path as before
    def follow(self):
        enemyNode = self.platform.get_node_from_pos(self.pos)
        playerPos = vec(self.platform.player.pos[0], self.platform.player.pos[1])
        playerNode = self.platform.get_node_from_pos(playerPos)
        
        path = self.platform.get_path(enemyNode, playerNode)
        print(enemyNode)
        print(path[1])
        nextNodePos = self.platform.get_pos_from_node(path[1])
        print(nextNodePos)
        return self.getDirectionFromPath(enemyNode,path[1])
        #print(playerNode)
        #print(enemyNode)
    def getDirectionFromPath(self,enemyNode, playerNode):
        if enemyNode.id[0] < playerNode.id[0]:
            print("going right", enemyNode.id, playerNode)
            return vec(1,0)
        elif enemyNode.id[0] > playerNode.id[0]:
            print("Going left")
            return vec(-1,0)
        elif enemyNode.id[1] < playerNode.id[1]:
            print("Going up")
            return vec(0,1)
        elif enemyNode.id[1] > playerNode.id[1]:
            print("Going down")
            return vec(0,-1)
    def getDirection(self, pos):
        enemyLoc = pos
        loc = self.rect.center
        dir = vec(enemyLoc[0]-loc[0], enemyLoc[1]-loc[1])
        #get unitvector of dir
        dir = dir.normalize()
        return dir