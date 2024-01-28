import pygame
import constants
import math
from gameObject import GameObject


class Bullet(GameObject):

    def create_bullet(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.position.x
        dy = mouse_y - self.position.y
        distance = math.sqrt(dx*dx + dy*dy)
        bullet_x_speed = dx / distance
        bullet_y_speed = dy / distance
        return [self.position.x, self.position.y, bullet_x_speed, bullet_y_speed]
        self.bullets.append([self.position.x, self.position.y, bullet_x_speed, bullet_y_speed])
        return
    
    def display(self):
        pygame.draw.circle(self.screen, "black", self.position, constants.BULLET_SIZE)
        return
    
    def move(self, destination_x, destination_y) -> bool:
        dx = destination_x - self.position.x
        dy = destination_y - self.position.y
        distance = math.sqrt(dx*dx + dy*dy)
        if distance <= constants.BULLET_SIZE:
            return True
        dx = dx / distance
        dy = dy / distance
        self.position.x += dx * constants.BULLET_SPEED * self.dt
        self.position.y += dy * constants.BULLET_SPEED * self.dt
        return False

    # def is_finished(self):
    #     if 
