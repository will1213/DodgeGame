import math
import constants
from game_object import GameObject


class Bullet(GameObject):
    """
    A class to represent the bullet instance.
    """

    def __init__(self, image, x, y, width, height, dt, destination_x, destination_y) -> None:
        """
        Init function

        Args:
            image (pygame.Surface): The image for the bullet.
            x (float): Bullet's current x coordinate position.
            y (float): Bullet's current y coordinate position.
            width (float): Bullet's width.
            height (float): Bullet's height.
            dt (float): The time step for movement calculation.
            destination_x: The x coordinate of the bullet's destination.
            destination_y: The y coordinate of the bullet's destination.

        """
        super().__init__(image, x, y, width, height, dt)
        self.destination_x = destination_x
        self.destination_y = destination_y
        return

    def move(self) -> None:
        """
        Move the bullet towards its destination.
        """
        dx = self.destination_x - self.x
        dy = self.destination_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        # Normalized for calculating how much needs to move on x/y coordinate
        dx = dx / distance
        dy = dy / distance
        self.set_positions(self.x + dx * constants.BULLET_SPEED * self.dt, 
                           self.y + dy * constants.BULLET_SPEED * self.dt)
        return

    def is_destination(self) -> bool:
        """
        Checks if the bullet has reached its destination.
        """
        dx = self.destination_x - self.x
        dy = self.destination_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        if distance <= constants.BULLET_SIZE:
            return True
        return False
