import pygame
vec = pygame.math.Vector2 
class sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        direction ={"up": (0,-speed) , "down": (0,speed), "right":(speed,0), "left":(-speed,0)}
        self.dir = direction[player.attack_dir]
        self.surf = pygame.Surface((40,40))
        self.surf.fill((255,100,0))
        self.rect = self.surf.get_rect()
        self.pos = vec(player.rect.midbottom)
    def move(self):
        self.pos.x += self.dir[0]
        self.pos.y += self.dir[1]
        self.rect.center = self.pos  