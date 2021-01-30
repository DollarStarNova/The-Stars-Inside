from game.libs.text.textFunctions import wrap_and_render_text
from game.levels.level import level
from game.libs.player.player import player
import pygame
import os
import random


class main_menu(level):
    def __init__(self, screen):

        main_font_large = pygame.font.Font(os.path.join(
            "game", "assets", "fonts", "Unxgalaw.ttf"), 120)
        title = "the Stars Inside"
        self.titlerender = wrap_and_render_text(
            title, main_font_large, screen.get_size(), align="center", colour=pygame.Color(230, 202, 126))

        super().__init__(screen)
        self.set_background("HOr_ScrollingStarfield01_720.png", 5)
        # level.load_music(os.path.join("Gameplay Loops",
        #                               "Gameplay Loop 1 (Loop @ 0_03_555 seconds).ogg"))
        level.load_music("The-Truth-Will-Be-Far-Stranger-_Edit_.ogg")
        pygame.time.wait(6000)
        level.play_music()

        self.player = player(-5500, 700)
        self.player.respect_map_bounds(0)

    def update(self):
        level.loop_music(0, "end")
        super().update()
        if self.player.xpos < 450:
            self.player.move(3)
        if self.player.xpos > 850:
            self.player.move(2)
        if self.player.ypos < 450:
            self.player.move(0)
        if self.player.ypos > 550:
            self.player.move(1)
        if random.randint(0, 10) > 3:
            self.player.move(random.randint(0, 3))

    def draw(self):
        self.scroll_background()
        self.screen.blit(self.titlerender, (0, 150))
        super().draw()
        pygame.display.flip()
