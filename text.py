import constants
from gameObject import GameObject


class Text(GameObject):
    """
    A class to display texts.
    """
    def __init__(self, image, x, y, width, height, dt, font) -> None:
        """
        Init function

        Args:
            image (pygame.Surface): The text box.
            x (float): X coordinate position.
            y (float): Y coordinate position.
            width (float): Text box width.
            height (float): Text box height.
            dt (float): The time step for movement calculation.
            font (pygame.font.Font): The font object used to create the text.

        """
        super().__init__(image, x, y, width, height, dt)
        self.font = font
        return

    def update_text(self, text):
        """ Update the score """
        self.set_image(self.font.render(
            f"{text}",
            True,
            constants.WHITE))
        return
