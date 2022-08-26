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
        self.rect.center = pos
        self.pos.x = pos[0]
        self.pos.y = pos[1]
        self.newDir = self.getDirection(self.platform.player.pos)
        self.lastDirection = [self.platform.get_node_from_pos(self.pos).id, self.platform.get_node_from_pos(self.pos).id]
        self.movementQueue = [vec(1,1)]
        self.direction = 0

    def move(self) -> None:
        if self.movementQueue:
            print("SUCCESS", self.platform.player.stats.health)
            self.direction = self.movementQueue.pop(0)
            print(self.direction)
            if not self.validMove(self.direction):
                print("FAIL")
                self.direction = self.getDirection(self.platform.player.pos) 
        else:
            self.direction = self.getDirection(self.platform.player.pos)
        moveBack = [vec(-1,-1), vec(1,-1), vec(-1,1), vec(1,1)]
        #self.movementQueue.append(vec(1,1))
        if not self.validMove(self.direction):
            self.direction = self.follow()
            if not self.validMove(self.direction):
                self.direction = self.lastDirection[0] #self.self.getDirectionFromPath(self.lastGrid[0],path[1])

        if self.validMove(self.direction):
            self.pos.x += self.direction[0]*self.stats.speed
            self.pos.y += self.direction[1]*self.stats.speed
            self.rect.center = self.pos.copy()
            collision = self.checkCollision()
            if collision == "Player":
                self.hitPlayer()
                for x in range(8):
                        self.movementQueue.append((-self.direction[0]*2,-self.direction[1]*2))
                    
                
            elif collision == True:
                print("WHAT THE FUCK")
            

        '''
        Structure of new movement system -> Always use movementQueue. 
        If movementQueue is empty, check if a straight line to player is possible.
        If not, use A* and insert one direction to next tile.
        Check if straight line or A* can now be used to find next direction.
        If this is not valid, use old direction

        Movement queue can also be used for other stuff, such as bounces when the player
        has been hit.
        '''
    def validMove(self, direction):
        oldPos = self.pos.copy()
        self.pos.x += direction[0]*self.stats.speed
        self.pos.y += direction[1]*self.stats.speed
        oldRect = self.rect.copy()
        self.rect.center = self.pos.copy()
        state = self.checkCollision()
        self.rect = oldRect.copy()
        self.pos = oldPos.copy()
        if state == "Player":
            return True
        return not state

    def checkCollision(self):
        for entity in self.platform.all_sprites:
            if entity == self:
                continue
            offset_x = self.rect.x - entity.rect.x
            offset_y = self.rect.y - entity.rect.y
            if(entity.mask.overlap(self.mask, (offset_x, offset_y))):
                if entity.__class__.__name__ == "Player":
                    return "Player"
                return True
    
    def hitPlayer(self):
        print("FUUUUCK")#, self.movementQueue)#Also print movement queue
        self.platform.player.take_damage(1)
        print("Player Health: ", self.platform.player.stats.health)
    def follow(self):
        enemyNode = self.platform.get_node_from_pos(self.pos)
        playerPos = vec(self.platform.player.pos[0], self.platform.player.pos[1])
        playerNode = self.platform.get_node_from_pos(playerPos)
        path = self.platform.get_path(enemyNode, playerNode)
        #print(enemyNode)
        #print(path[1])
        nextNodePos = self.platform.get_pos_from_node(path[1])
        #print(nextNodePos)
        newDir = self.getDirectionFromPath(enemyNode,path[1])
        if self.lastDirection[1] != newDir:
            self.lastDirection.pop(0)
            self.lastDirection.append(newDir)
        return newDir
        #print(playerNode)
        #print(enemyNode)
    def getDirectionFromPath(self,enemyNode, playerNode)-> vec: 
        if enemyNode.id[0] < playerNode.id[0]:
            print("going right", enemyNode.id, playerNode)
            return vec(1,0)
        elif enemyNode.id[0] > playerNode.id[0]:
            print("Going left")
            return vec(-1,0)
        elif enemyNode.id[1] < playerNode.id[1]:
            print("Going down")
            return vec(0,1)
        elif enemyNode.id[1] > playerNode.id[1]:
            print("Going up")
            return vec(0,-1)
    def getDirection(self, pos):
        enemyLoc = pos
        loc = self.rect.center
        dir = vec(enemyLoc[0]-loc[0], enemyLoc[1]-loc[1])
        #get unitvector of dir
        dir = dir.normalize()
        return dir
    def getGridLocation(self, pos = None):
        if not pos:
            pos = self.pos
        x = pos.x//self.platform.tileSize
        y = pos.y//self.platform.tileSize
        return vec(x,y)