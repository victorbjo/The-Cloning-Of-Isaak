import pygame
vec = pygame.math.Vector2 
class projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        speed = player.stats.projectile_speed
        self.platform = player.platform
        direction ={"up": (0,-speed) , "down": (0,speed), "right":(speed,0), "left":(-speed,0)}
        self.dir = direction[player.attack_dir]
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255,100,0))
        self.rect = self.surf.get_rect()
        self.pos = vec(player.rect.center)
        self.rect.center = self.pos
        self.obstacles = self.platform.obstacles
        self.mask = pygame.mask.from_surface(self.surf)
    def move(self):
        oldPos = self.pos
        oldCenter = self.rect.center
        self.pos.x += self.dir[0]
        self.pos.y += self.dir[1]
        self.rect.center = self.pos
        if self.check_collision():
            self.kill()
    #Check for mask collisions
    def check_collision(self):
        for entity in self.obstacles:
            offset_x = self.rect.x - entity.rect.x
            offset_y = self.rect.y - entity.rect.y
            if(entity.mask.overlap(self.mask, (offset_x, offset_y))):
                return True
        return False