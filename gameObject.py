import pygame

class GameObject:

    def __init__(self, screen, xPosition, yPosition, dt) -> None:
        self.screen = screen
        self.position = pygame.Vector2(xPosition, yPosition)
        self.dt = dt
        return
    
    def display(self) -> None:
        pass

    def move(self) -> None:
        pass
