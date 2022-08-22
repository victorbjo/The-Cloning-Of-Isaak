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
        self.lastDirection = None
        self.lastGrid = [self.platform.get_node_from_pos(self.pos).id, self.platform.get_node_from_pos(self.pos).id]
        self.movementQueue = [vec(1,1)]


    def move(self) -> None:
        if self.movementQueue:
            direction = self.movementQueue.pop(0)
            if not self.validMove(direction):
                direction = self.getDirection(self.platform.player.pos) 
        else:
            direction = self.getDirection(self.platform.player.pos)
        moveBack = [vec(-1,-1), vec(1,-1), vec(-1,1), vec(1,1)]
        #self.movementQueue.append(vec(1,1))
        if not self.validMove(direction):
            lastFollow = self.lastDirection
            direction = self.follow()
            self.lastDirection = vec(0,1)
            if not self.validMove(direction):
                print(self.validMove(vec(1,1)))
                print("Collison", self.checkCollision())
                #playerPos = vec(self.platform.player.pos[0], self.platform.player.pos[1])
                #playerNode = self.platform.get_node_from_pos(playerPos)
                #gridNode = self.lastGrid[0]
                #print(self.lastGrid, "gridNode")
                #path = self.platform.get_path(self.lastGrid[0], playerNode)
                #print(path, " path")
                #rint(playerNode, " playerNode")
                #print(self.lastGrid[0], " lastGrid")
                direction = self.lastGrid[0] #self.self.getDirectionFromPath(self.lastGrid[0],path[1])
                
            #return
        #self.lastDirection = direction.copy()
        if self.validMove(direction):
            self.pos.x += direction[0]*self.stats.speed
            self.pos.y += direction[1]*self.stats.speed
            self.rect.center = self.pos.copy()
            collision = self.checkCollision()
            if collision == "Player":
                self.movementQueue = []
                #for x in range(8):
                    #self.movementQueue.append(vec(-1,-1))
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
        return not state
    def moveOld(self): #This needs to be redone. Make move Queue.
        #Move queue should be a list of directions to move in. Eg if following a*
        # path, the move queue should be a list of directions to move in to get to
        # the player. If the player moves, the move queue should be recalculated.
        # if move queue is empty, the enemy should go straight towards the player.
        # if the enemy is in the same node as the player, the enemy should bounce back using move queue.
        if self.movementQueue:
            direction = self.movementQueue[0]
        else:
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
                if entity.__class__.__name__ == "Player":
                    entity.take_damage(1)
                    print("Player Health: ", entity.stats.health)
                    return "Player"
                return True
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
        if self.lastGrid[1] != newDir:
            self.lastGrid.pop(0)
            self.lastGrid.append(newDir)
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