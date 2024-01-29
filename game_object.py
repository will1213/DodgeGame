import pygame


class GameObject(pygame.sprite.Sprite):
    """
    A base class inherit from pygame sprite.
    """
    def __init__(self, image=None, x=0, y=0, width=0, height=0, dt=0) -> None:
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
        self.dt = dt
        self.x = x
        self.y = y
        if image:
            self.set_image(image, width, height)
            self.set_positions(x, y)
        return

    def set_image(self, image, width=None, height=None):
        """
        Set new image to the object, and scale if needed. Main use case for text objects.
        """
        self.image = image
        # Only scale if provided desired size
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        return

    def get_positions(self):
        return self.x, self.y

    def set_positions(self, x, y):
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        return

    def draw(self, screen):
        """
        Draw the object on the given screen.

        Args:
            screen (pygame.Surface): The screen to be drawn.
        """
        screen.blit(self.image, self.rect)
        return
