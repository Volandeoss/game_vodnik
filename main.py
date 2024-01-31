import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("some game")
        icon = pygame.image.load("data/images/icon_1.png")
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode((640, 480))

        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]
        # up    down  left   right

        self.assets = {
            "player": load_image("entities/player.png"),
        }
        self.player = PhysicsEntity(self, "player", (50, 50), (10, 15))

    def run(self):
        while True:
            #!!!!
            # self.display.blit(
            #     pygame.image.load(
            #         "C:/Users/Maxim/Downloads/4bb800c4-4ddc-4592-9ae6-06006f03995b.jpg"
            #     )
            # )
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    # if event.key == pygame.K_a:
                    #     self.movement[2] = True
                    # if event.key == pygame.K_d:
                    #     self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    # if event.key == pygame.K_a:
                    #     self.movement[2] = False
                    # if event.key == pygame.K_d:
                    #     self.movement[3] = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.update()
            self.clock.tick(60)


Game().run()
