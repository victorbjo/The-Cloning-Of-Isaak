import pygame
from pygame.locals import *
import sys
import time
pygame.init()

FramePerSec = pygame.time.Clock()
from classes import *
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
    
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
friendly_projectiles = pygame.sprite.Group()
collisonable_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
PT1 = platform()
P1 = Player(friendly_projectiles, obstacles)
obs = obstacle((200,200))
#Projectile = projectile("right") 
all_sprites.add(PT1)
obstacles.add(obs)
all_sprites.add(P1)
collisonable_sprites.add(P1, obs)
#friendly_projectiles.add(Projectile)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            P1.attack0(event.key)
        elif event.type == KEYUP:
            P1.attack0(event.key, False)
    displaysurface.fill((0,0,0))
    P1.spawn_bullets()
    P1.move()
    #keys = pygame.key.get_pressed()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    for entity in friendly_projectiles:
        entity.move()
        displaysurface.blit(entity.surf, entity.rect)
    for entitiy in obstacles:
        displaysurface.blit(entitiy.surf, entitiy.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)