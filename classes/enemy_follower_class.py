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
        self.newDir = self.getDirection(self.platform.player.pos)
        self.lastDirections = [None]
    def move(self): #This needs to be redone. Make move Queue.
        #Move queue should be a list of directions to move in. Eg if following a*
        # path, the move queue should be a list of directions to move in to get to
        # the player. If the player moves, the move queue should be recalculated.
        # if move queue is empty, the enemy should go straight towards the player.
        # if the enemy is in the same node as the player, the enemy should bounce back using move queue.
        
        direction = self.getDirection(self.platform.player.pos)
        oldPos = vec(float(self.pos.x), float(self.pos.y)).copy()
        self.pos.x += direction[0]*self.stats.speed
        self.pos.y += direction[1]*self.stats.speed
        oldRect = self.rect.center
        self.rect.center = self.pos
        if self.checkCollision():
            self.rect.center = oldRect
            self.pos = oldPos.copy()
            self.newDir = self.follow()
            self.lastDirections.insert(0,self.newDir.copy())
            self.pos.x += self.newDir[0]*self.stats.speed
            self.pos.y += self.newDir[1]*self.stats.speed
            self.rect.center = self.pos
            if self.checkCollision():
                #print(self.pos)
                self.lastDirections.pop(0)
                self.pos = oldPos
                self.pos.x += self.lastDirections[0][0]*self.stats.speed
                self.pos.y += self.lastDirections[0][1]*self.stats.speed
                self.rect.center = self.pos
                print("FUCK")
                print(self.lastDirections)
            else:
                pass #self.lastDirections = self.newDir.copy()
            #self.lastDirection = self.newDir
            #Check again for collision. If collision follow same path as before
    def checkCollision(self):
        for entity in self.platform.all_sprites:
            if entity == self:
                continue
            offset_x = self.rect.x - entity.rect.x
            offset_y = self.rect.y - entity.rect.y
            if(entity.mask.overlap(self.mask, (offset_x, offset_y))):
                return True
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