import pygame
class stats():
    def __init__(self) -> None:
        self.speed = -1
        self.fire_rate = 0.5
        self.projectile_speed = 4
        self.projectile_damage = 2
        self.health = 7
        self.maxHealth = self.health
    def takeDamage(self, damage = 1):
        self.health -= damage
        