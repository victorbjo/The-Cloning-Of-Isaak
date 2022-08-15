import pygame
from pygame.locals import *
import sys
import time
pygame.init()
FramePerSec = pygame.time.Clock()
from classes import *
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
        [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1]]
platform = platforms(map)
generate_map(platform, platform.map)
P1 = Player((WIDTH/2, HEIGHT/2), platform)
platform.player = P1
Enemy = enemy_base(platform, (WIDTH/2+50, HEIGHT/2+20),platform.relativeDir+"/Sprites/enemy.png")
Follower = enemy_follower(platform, (WIDTH/2+150, HEIGHT/2+20),platform.relativeDir+"/Sprites/enemy.png")

platform.movable_sprites.add(P1)
obs = obstacle((200,200))
displaysurface.blit(platform.platform.surf, platform.platform.rect)

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
    platform.front_sprites.draw(displaysurface)
    for entity in platform.movable_sprites:
        entity.move()
    pygame.display.update()
    FramePerSec.tick(FPS)