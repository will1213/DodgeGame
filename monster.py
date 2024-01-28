import pygame
import math
from gameObject import GameObject


class Monster(GameObject):

    def display(self, size):
        self.monster_object = pygame.draw.circle(self.screen, "black", self.position, size)
        return
    
    def move(self, speed, destination_x, destination_y):
        # Find direction vector (dx, dy) between enemy and player.
        dx = destination_x - self.position.x
        dy = destination_y - self.position.y
        distance = math.sqrt(dx*dx + dy*dy)
        dx = dx / distance
        dy = dy / distance
        
        self.position.x += dx * speed * self.dt
        self.position.y += dy * speed * self.dt
        return

