import pygame
from pygame.locals import *
import sys
import time
pygame.init()
FramePerSec = pygame.time.Clock()
from classes import *
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
platform = platforms()
P1 = Player(platform.friendly_projectiles, platform.obstacles, (WIDTH/2, HEIGHT/2), platform)
platform.all_sprites.add(P1)
platform.movable_sprites.add(P1)
obs = obstacle((200,200))
displaysurface.blit(platform.platform.surf, platform.platform.rect)
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
generate_map(platform, 17, 11, map)
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
    for entity in platform.all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    for entity in platform.movable_sprites:
        entity.move()
    pygame.display.update()
    FramePerSec.tick(FPS)