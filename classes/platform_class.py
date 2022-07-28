HEIGHT = 550
WIDTH = 850
ACC = 2
FRIC = -1
FPS = 60
import pygame
class platforms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.friendly_projectiles = pygame.sprite.Group()#Every moving projectile. Can be deleted
        self.collisonable_sprites = pygame.sprite.Group()#sprites that can collide with the player
        self.all_sprites = pygame.sprite.Group()#all sprites
        self.movable_sprites = pygame.sprite.Group()#All sprites that can move
        self.obstacles = pygame.sprite.Group()#For (?Pseudo?) static obstacle. Can be deleted
        self.platform = self.__nested_platform()
    class __nested_platform(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((WIDTH, 20))
            self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
