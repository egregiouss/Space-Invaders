import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            screen.fill((0, 0, 0))
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()
