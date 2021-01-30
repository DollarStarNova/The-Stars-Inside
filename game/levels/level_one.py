import pygame
import os
from game.levels.level import level


class level_one(level):
    def __init__(self, screen):
        super().__init__(screen)
        self.scroll_speed = 0.05
        self.load_tilemap("level1.tmx")
        level.load_music(os.path.join("Gameplay Loops",
                                      "Gameplay Loop 1 (Loop @ 0_03_555 seconds).ogg"))
        level.play_music()

    def update(self):
        level.loop_music(3555, "end")
        super().update()

    def draw(self):
        self.draw_tiles()
        super().draw()
        pygame.display.flip()
