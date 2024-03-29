import random
import pygame
import constants
from player import Player
from enemy import Enemy
from bullet import Bullet
from text import Text


class Game:
    """
    A class to represent the game instance, which includes the logic of how the game works.
    """
    def __init__(self) -> None:
        """
        Init function
        """
        # Initialize the game
        pygame.init()

        # Set up screen
        pygame.display.set_caption(constants.GAME_NAME)
        self.screen = pygame.display.set_mode((constants.SCREEN_WDITH, constants.SCREEN_HEIGHT))

        # TODO: Allow user to adjust music
        # Set up the background music
        pygame.mixer.music.load(constants.BACKGROUND_MUSIC_PATH)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)

        # Set up clock
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(constants.FPS) / constants.SECOND_IN_MILLISECOND

        # Use this to spawn enemy on a interval
        self.last_enemies_spawn_time = pygame.time.get_ticks()

        # Set up the player character
        # Use sqaure for now
        # TODO: Find a good sprite to use or just load a image
        player_image = pygame.Surface((constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT))
        player_image.fill(constants.YELLOW)
        self.player = Player(
            image=player_image,
            x=constants.SCREEN_CENTER_X,
            y=constants.SCREEN_CENTER_Y,
            width=constants.PLAYER_WIDTH,
            height=constants.PLAYER_HEIGHT,
            dt=self.dt,)

        # Initialize the container for holding group of enemies/bullets
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # The font used in the game
        self.font = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE)  

        # The starting game button
        self.start_button = Text(
            x=constants.SCREEN_CENTER_X,
            y=constants.SCREEN_CENTER_Y,
            font=self.font,
            )
        self.start_button.update_text('Start')

        # The surival score label
        self.survival_score = Text(
            x=constants.SCREEN_CENTER_X,
            y=constants.FONT_SIZE,
            font=self.font,
            )

        # The elimination score label
        self.elimination_score = Text(
            x=constants.SCREEN_CENTER_X,
            y=self.screen.get_height() - constants.FONT_SIZE,
            font=self.font,
            )

        # The ending button
        self.game_over_button = Text(
            x=constants.SCREEN_CENTER_X,
            y=constants.SCREEN_CENTER_Y,
            font=self.font,
            )
        self.game_over_button.update_text('Game Over')

        # Game level
        self.elimination_count = 0
        self.level = 1

        # Game status
        self.run_starting = True
        self.run_game = False
        self.run_ending = False

        # Start the game
        self.run()
        return

    def run(self) -> None:
        """
        Start the game
        """
        self.starting_theme()
        self.main_game_theme()
        self.ending_theme()
        pygame.quit()
        return

    def main_game_theme(self) -> None:
        """
        Running the main game, this includes the logic of the game.
        """
        while self.run_game:
            player_position_x = self.player.x
            player_position_y = self.player.y

            # Detect different events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # When user click "x"
                    self.run_game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get cursor position when user shoots
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # TODO: Use other image to show the bullet
                    bullet_image = pygame.Surface((constants.BULLET_SIZE, constants.BULLET_SIZE))
                    bullet_image.fill(constants.GREEN)
                    new_bullet = Bullet(
                        image=bullet_image,
                        x=player_position_x,
                        y=player_position_y,
                        width=constants.BULLET_SIZE,
                        height=constants.BULLET_SIZE,
                        dt=self.dt,
                        destination_x=mouse_x,
                        destination_y=mouse_y,)
                    self.bullets.add(new_bullet)

            # Set the background color
            self.screen.fill(constants.GREY)

            # Draw the player and handle its movement
            self.player.draw(self.screen)
            self.player.move()

            # Create enemies based on a time interval
            current_time = pygame.time.get_ticks()
            time_since_last_enemy_spawn = current_time - self.last_enemies_spawn_time
            if time_since_last_enemy_spawn > constants.TIME_PER_LEVEL_IN_MILLISECOND:
                self.level += 1
                self.last_enemies_spawn_time = current_time
                self.create_enemies(self.level)

            # Draw the enemies and attack player
            for enemy in self.enemies.sprites():
                enemy.draw(self.screen)
                enemy.move(constants.ENEMY_SPEED, player_position_x, player_position_y)

            # Draw the bullest and go to its fire target
            for bullet in self.bullets.sprites():
                bullet.move()
                if bullet.is_destination():
                    bullet.kill()
                bullet.draw(self.screen)

            # Handle when player get hits by any enemy
            # Game over
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.run_game = False
                self.run_ending = True

            # Handle collision between bullets and enemies
            # If bullet hits an enemy, delete both of them
            killed_enemies = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

            # Update the elimination count
            self.elimination_count += len(killed_enemies)
            self.elimination_score.update_text(f"Kill Count: {self.elimination_count}")
            self.elimination_score.draw(self.screen)

            # Update the survival time
            self.survival_score.update_text(
                f"Survival Time: {(pygame.time.get_ticks() / constants.SECOND_IN_MILLISECOND):.3f} seconds"
                )
            self.survival_score.draw(self.screen)

            # Update the screen
            pygame.display.flip()

            # Set the constant FPS
            self.set_clock_tick(constants.FPS)
        return

    def starting_theme(self) -> None:
        """
        The starting menu theme, start the gameplay when user click play.
        """
        # Basic loop and wait for user's input
        while self.run_starting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_starting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if user click the start button, start the game if it's clicked.
                    if self.start_button.rect.collidepoint(event.pos):
                        self.run_starting = False
                        self.run_game = True
            self.screen.fill(constants.GREY)
            self.start_button.draw(self.screen)
            pygame.display.flip()
            self.set_clock_tick(constants.FPS)
        return

    def ending_theme(self) -> None:
        """
        The game over theme, also shows user's scores.
        """
        # Basic loop and wait for user's input
        while self.run_ending:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_ending = False
                # Check if user hits game over, end the game if it's clicked.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over_button.rect.collidepoint(event.pos):
                        self.run_ending = False
            self.screen.fill(constants.GREY)
            self.game_over_button.draw(self.screen)

            # Keep the scores on the screen
            self.elimination_score.draw(self.screen)
            self.survival_score.draw(self.screen)
            pygame.display.flip()
            self.set_clock_tick(constants.FPS)
        return

    def set_clock_tick(self, fps) -> None:
        """
        Set the clock tick based on fps, it should be called every frame.
        """
        self.clock.tick(fps)
        return

    def create_enemies(self, level) -> None:
        """
        Create enemies based on level, enemies should appear on 4 sides randomly.

        Args:
            level (int): The current game level.
        """
        sides = ["top", "bottom", "left", "right"]
        for _ in range(level):
            # Determine which side should spawn enemy
            choice = sides[random.randint(0, 3)]
            x = random.randint(0, self.screen.get_width())
            y = random.randint(0, self.screen.get_height())
            if choice == "top":
                y = 0
            elif choice == "bottom":
                y = self.screen.get_height()
            elif choice == "left":
                x = 0
            elif choice == "right":
                x = self.screen.get_width()

            # Create the new enemies and add to the group
            # TODO: Use other image for enemy
            enemy_image = pygame.Surface((constants.ENEMY_WIDTH, constants.ENEMY_HEIGHT))
            enemy_image.fill(constants.RED)
            enemy = Enemy(
                image=enemy_image,
                x=x,
                y=y,
                width=constants.ENEMY_WIDTH,
                height=constants.ENEMY_HEIGHT,
                dt=self.dt,)
            self.enemies.add(enemy)
        return
