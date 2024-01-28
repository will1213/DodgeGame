
import pygame
import math
import constants

from gameObject import GameObject


class Player(GameObject):

    bullets = []

    def display(self, size):
        self.player_object = pygame.draw.circle(self.screen, "red", self.position, size)
        return

    def register_player_move(self):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keys[pygame.K_w]:
            dy += -constants.PLAYER_SPEED
        if keys[pygame.K_s]:
            dy += constants.PLAYER_SPEED
        if keys[pygame.K_a]:
            dx += -constants.PLAYER_SPEED
        if keys[pygame.K_d]:
            dx += constants.PLAYER_SPEED
        self.position.x += dx * self.dt
        self.position.y += dy * self.dt
        return
    
    def create_bullet(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.position.x
        dy = mouse_y - self.position.y
        distance = math.sqrt(dx*dx + dy*dy)
        bullet_x_speed = dx / distance
        bullet_y_speed = dy / distance
        self.bullets.append([self.position.x, self.position.y, bullet_x_speed, bullet_y_speed])
        return
    
    def display_bullet(self, screen):
        print('dispaly bullet')
        for bullet in self.bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            pygame.draw.circle(self.screen, "black", self.position, 5)
            # pygame.draw.line(screen, 'black', (bullet[0], bullet[1]), (bullet[0], bullet[1]), 10)

        return
        print(self.bullets)
        # self.move(dx * speed, dy * speed)
        # distance_x = mouse_x - self.position.x
        # distance_y = mouse_y - self.position.y
            
        # angle = math.atan2(distance_y, distance_x)
        
        # speed_x, speed_y can be `float` but I don't convert to `int` to get better position
        # speed_x = SPEED * math.cos(angle)
        # self.bullet.append([self.position.x, self.position.y, speed])
        # pygame.draw.line(screen, 'black', (self.position.x, self.position.y), (self.position.x, self.position.y))
        