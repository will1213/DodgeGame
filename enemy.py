import math
from gameObject import GameObject


class Enemy(GameObject):
    """
    A class to represent the enemy.
    """
    def move(self, speed, destination_x, destination_y):
        """Move the bullet towards its destination."""
        dx = destination_x - self.x
        dy = destination_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        dx = dx / distance
        dy = dy / distance
        self.set_positions(self.x + dx * speed * self.dt, self.y + dy * speed * self.dt)
        return
