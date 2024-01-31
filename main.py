import pygame
import sys
from scripts.entities import PhysicsEntity


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("some game")

        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/clouds/cloud_1.png")

        self.img.set_colorkey((0, 0, 0))

        self.img_pos = [160, 260]

        self.movement = [False, False, False, False]
        # up    down  left   right
        self.collision_area = pygame.Rect(50, 50, 200, 10)

        self.player = PhysicsEntity(self, "player", (50, 50), (32, 32))

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            img_r = pygame.Rect(
                self.img_pos[0],
                self.img_pos[1],
                self.img.get_width(),
                self.img.get_height(),
            )
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (255, 56, 200), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (255, 0, 20), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.img_pos[0] += (self.movement[3] - self.movement[2]) * 5
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_a:
                        self.movement[2] = True
                    if event.key == pygame.K_d:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
                    if event.key == pygame.K_a:
                        self.movement[2] = False
                    if event.key == pygame.K_d:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()