import pygame
import constants
from player import Player
from monster import Monster
from bullet import Bullet


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WDITH, constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(constants.FPS) / constants.SECOND_TO_MILLISECOND
        self.player = Player(self.screen, self.screen.get_width() / 2, self.screen.get_height() / 2, self.dt)
        self.monster = Monster(self.screen, 0, 0, self.dt)
        self.level = 0
        self.bullets = []
        self.running = True
        self.run()
        return

    def run(self) -> None:
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            player_position_x = self.player.position.x
            player_position_y = self.player.position.y
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    new_bullet = Bullet(self.screen, player_position_x, player_position_y, self.dt)
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.bullets.append([new_bullet, mouse_x, mouse_y])


                    # pygame.display.update()
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            self.player.display(constants.PLAYER_SIZE)
            self.player.register_player_move()
            self.monster.display(constants.PLAYER_SIZE)
            self.monster.move(250, player_position_x, player_position_y)
            # if self.player.player_object.colliderect(self.monster.monster_object):
            #     self.running = False
            for bullet_items in self.bullets:
                bullet = bullet_items[0]
                bullet_destination_x = bullet_items[1]
                bullet_destination_y = bullet_items[2]
                bullet.display()
                if bullet.move(bullet_destination_x, bullet_destination_y):
                    self.bullets.remove(bullet_items)
                # if bullet.bullet_object.colliderect(self.monster.monster_object):
                #     self.bullets.remove(bullet_items)
                    

            pygame.display.flip()

            self.set_clock_tick(constants.FPS)
        pygame.quit()
    
    def set_clock_tick(self, FPS) -> None:
        self.clock.tick(FPS)
        return