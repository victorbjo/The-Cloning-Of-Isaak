HEIGHT = 880
WIDTH = 1360
HEIGHT_BLOCKS = 11
WIDTH_BLOCKS = 17
ACC = 2
FRIC = -1
FPS = 60
import pygame
from .getWorkingDir import *
from .node_class import *
class platforms(pygame.sprite.Sprite):
    def __init__(self, map):
        super().__init__()
        self.player = None
        self.friendly_projectiles = pygame.sprite.Group()#Every moving projectile. Can be deleted
        self.collisionable_sprites = pygame.sprite.Group()#sprites that can collide with the player
        self.all_sprites = pygame.sprite.Group()#all sprites
        self.movable_sprites = pygame.sprite.Group()#All sprites that can move
        self.obstacles = pygame.sprite.Group()#For (?Pseudo?) static obstacle. Can be deleted
        self.platform = self.__nested_platform()
        self.relativeDir = getRelativePath()
        self.map = map
        self.nodeMap = grid_to_nodes(self.map)
    def get_node_from_pos(self, pos):
        posX = int(pos.x/(WIDTH/WIDTH_BLOCKS))
        posY = int(pos.y/(HEIGHT/HEIGHT_BLOCKS))
        for node in self.nodeMap:
            if node.id == (posX, posY):
                return node
    def get_path(self, start, end):
        try:
            path = aStar(end, start)
            return path
        except:
            return None
    class __nested_platform(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((WIDTH, 20))
            self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
