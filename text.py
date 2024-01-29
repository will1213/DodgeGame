import constants
from game_object import GameObject


class Text(GameObject):
    """
    A class to display texts.
    """
    def __init__(self, x, y, font) -> None:
        """
        Init function

        Args:
            x (float): X coordinate position.
            y (float): Y coordinate position.
            font (pygame.font.Font): The font object used to create the text.

        """
        super().__init__(x=x, y=y)
        self.font = font
        return

    def update_text(self, text):
        """ Update the score """
        self.set_image(self.font.render(
            f"{text}",
            True,
            constants.WHITE))
        return
