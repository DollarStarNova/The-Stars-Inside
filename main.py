import pygame
import sys
from levels.menu import main_menu

if __name__ == "__main__":
    screen = pygame.display.set_mode(size=(800, 600))
    pygame.init()
    current_scene = main_menu(screen)

    pygame.display.update()
    FPS = 60
    fpsClock = pygame.time.Clock()
    running = True

    while running:
        current_scene.update()
        current_scene.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fpsClock.tick(FPS)
    pygame.quit()
    sys.exit(0)
