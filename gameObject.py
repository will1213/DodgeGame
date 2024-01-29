import pygame


class GameObject(pygame.sprite.Sprite):
    """
    A base class inherit from pygame sprite
    """
    def __init__(self, image, x, y, width, height, dt) -> None:
        """
        Init function

        Args:
            image (pygame.Surface): The image for the object.
            x (float): Object's x position.
            y (float): Object's y position.
            width (float): Object's width.
            height (float): Object's height.
            dt (float): The time step for movement calculation.
        """
        super().__init__()

        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.dt = dt
        self.set_positions(x, y)
        return

    def get_positions(self):
        return self.x, self.y

    def set_positions(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        return

    def draw(self, screen):
        """
            Draw the object on the given screen.
        Args:
            screen (pygame.Surface): The screen to be drawn.
        """
        screen.blit(self.image, self.rect)
        return
