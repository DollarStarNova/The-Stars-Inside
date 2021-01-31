import pygame
import sys
from game.levels.menu import main_menu
from game.levels.level_one import level_one


if __name__ == "__main__":
    screen = pygame.display.set_mode(size=(1280, 720))
    pygame.init()
    # pygame.time.wait(7000)
    # current_scene = main_menu(screen)
    current_scene = level_one(screen)

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
            current_scene.handle_event(event)
        fpsClock.tick(FPS)
    pygame.quit()
    sys.exit(0)
