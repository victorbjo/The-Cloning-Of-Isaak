import pygame
from .stats_class import *
from .platform_class import *
from .projectile_class import *
from .healthManager_class import *
vec = pygame.math.Vector2
from pygame.locals import *
import time
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, platform = None):
        self.stats = stats()
        super().__init__()
        platform.all_sprites.add(self)
        self.healthManager = healthManager(self, platform)
        self.image = pygame.image.load(platform.relativeDir+"/Sprites/Isakk.png")
        self.image = self.surf = pygame.transform.scale(self.image, (HEIGHT/HEIGHT_BLOCKS*0.8, WIDTH/WIDTH_BLOCKS*0.8))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.pos = pos
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.projectiles = platform.friendly_projectiles
        self.lastShot = 0
        self.movePressed = False
        self.attack_in_progress = False
        self.attack_dir = None
        self.attack_keys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
        self.mask = pygame.mask.from_surface(self.surf)
        self.oldPos = self.rect.center
        self.platform = platform
    def move(self):
        self.healthManager.update()
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC
        if pressed_keys[K_w]:
            self.acc.y = -ACC
        if pressed_keys[K_s]:
            self.acc.y = ACC
        self.acc.x += self.vel.x * self.stats.speed
        self.acc.y += self.vel.y * self.stats.speed
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        elif self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        elif self.pos.y < 20:
            self.pos.y = 20           
        oldCenter = self.rect.center
        self.platform.get_node_from_pos(self.pos)
        for entity in self.platform.obstacles:
            offset_x = self.rect.x - entity.rect.x
            offset_y = self.rect.y - entity.rect.y
            if(entity.mask.overlap(self.mask, (offset_x, offset_y))):
                self.acc = vec(0,0)
                self.rect.center = self.oldPos
                self.pos = self.rect.center
                return
        self.oldPos = self.rect.center
        self.rect.center = self.pos
    def attack0(self, event, press = True):
        if press:
            if event == K_DOWN or event == K_UP or event == K_RIGHT or event == K_LEFT:
                if event == K_DOWN:
                    self.attack_dir = "down"
                if event == K_UP:
                    self.attack_dir = "up"
                if event == K_RIGHT:
                    self.attack_dir = "right"
                if event == K_LEFT:
                    self.attack_dir = "left"
                self.attack_in_progress = True
        else:
            if event == K_DOWN or event == K_UP or event == K_RIGHT or event == K_LEFT:
                pressedKeys = pygame.key.get_pressed()
                if not pressedKeys[K_DOWN] and not pressedKeys[K_UP] and not pressedKeys[K_LEFT] and not pressedKeys[K_RIGHT]:
                    self.attack_in_progress = False
            
    def spawn_bullets(self):
        if time.time() - self.lastShot < self.stats.fire_rate or not self.attack_in_progress:
            return 0
        self.lastShot = time.time()
        Projectile = projectile(self)
        #Projectile = projectile(self.attack_dir, self.rect.midbottom)
        self.projectiles.add(Projectile)
        self.platform.all_sprites.add(Projectile)
        self.platform.movable_sprites.add(Projectile)
    def take_damage(self, damage):
        self.stats.takeDamage(damage)
        if self.stats.health <=0:
            self.kill()