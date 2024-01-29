import random
import pygame
import constants
from player import Player
from enemy import Enemy
from bullet import Bullet


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

        # Set up clock
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(constants.FPS) / constants.SECOND_IN_MILLISECOND

        # Use this to spawn enemy on a interval
        self.last_enemies_spawn_time = pygame.time.get_ticks()

        # Set up the player character
        # Use sqaure for now
        # TODO: Find a good sprite to use
        player_image = pygame.Surface((300, 60))
        player_image.fill('red')
        self.player = Player(
            image=player_image,
            x=self.screen.get_width() / 2,
            y=self.screen.get_height() / 2,
            width=constants.PLAYER_WIDTH,
            height=constants.PLAYER_HEIGHT,
            dt=self.dt)
        
        # Initialize the container for holding group of enemies/bullets
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # The game level/score
        self.score = 0
        self.level = 1

        self.running = True
        self.run()
        return

    def run(self) -> None:
        """
        Running the game, this includes the logic of the game.
        """
        while self.running:
            player_position_x = self.player.x
            player_position_y = self.player.y

            # Detect different events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # When user click "x"
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # When user click on mouse aka shooting 
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # TODO: Use other image to show the bullet
                    new_bullet = Bullet(
                        image=pygame.Surface((5, 5)),
                        x=player_position_x,
                        y=player_position_y,
                        width=5,
                        height=5,
                        dt=self.dt,
                        destination_x=mouse_x,
                        destination_y=mouse_y)

                    self.bullets.add(new_bullet)

            # Set the background color
            self.screen.fill(constants.GREY)

            # Draw the player and handle its movement
            self.player.draw(self.screen)
            self.player.move()

            # Create enemies based on a time interval 
            current_time = pygame.time.get_ticks()
            time_lapsed = current_time - self.last_enemies_spawn_time
            if time_lapsed > constants.TIME_PER_LEVEL_IN_MILLISECOND:
                self.level += 1
                self.last_enemies_spawn_time = current_time
                self.create_enemies(self.level)

            # Draw the enemies and attack player
            for enemy in self.enemies.sprites():
                enemy.draw(self.screen)
                enemy.move(250, player_position_x, player_position_y)

            # Draw the bullest and go to its fire target
            for bullet in self.bullets.sprites():
                bullet.move()
                if bullet.is_destination():
                    bullet.kill()
                bullet.draw(self.screen)

            # Handle when player get hit by any enemy
            # Game over
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.running = False

            # Handle collision between bullets and enemies 
            # If bullet hits an enemy, delete both of them
            pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

            # Update the screen
            pygame.display.flip()

            # Set the constant FPS
            self.set_clock_tick(constants.FPS)

        pygame.quit()
        return

    def set_clock_tick(self, fps) -> None:
        self.clock.tick(fps)
        return

    def create_enemies(self, level) -> None:
        """
        Create enemies based on level, enemies should appear on 4 sides randomly
        Args:
            level (_type_): _description_
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

            enemy = Enemy(
                image=pygame.Surface((30, 30)),
                x=x,
                y=y,
                width=100,
                height=30,
                dt=self.dt)
            self.enemies.add(enemy)
        return
