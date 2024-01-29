
import pygame
import math
import constants

from gameObject import GameObject


class Player(GameObject):


    def move(self):
        """
        Move the player character based on user inputs.

        W -> up
        A -> left
        S -> down
        D -> right
        """
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

        self.prevent_out_of_screen(self.x + dx * self.dt, self.y + dy * self.dt)
        return

    def prevent_out_of_screen(self, x, y):
        """
        Prevents the object from moving outside the boundaries of the screen.
        """
        x = max(0, min(x, constants.SCREEN_WDITH))
        y = max(0, min(y, constants.SCREEN_HEIGHT))
        self.set_positions(x, y)
        return
