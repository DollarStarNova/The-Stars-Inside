from game.libs.text.textFunctions import wrap_and_render_text
from game.levels.level import level
from game.libs.player.player import player
import pygame
import os


class main_menu(level):
    def __init__(self, screen):

        main_font_large = pygame.font.Font(os.path.join(
            "game", "assets", "fonts", "SpaceAndAstronomy-pZRD.ttf"), 50)
        title = "Two Michaels Games Presents"
        self.titlerender = wrap_and_render_text(
            title, main_font_large, screen.get_size(), align="center")

        super().__init__(screen)
        self.set_background("HOr_ScrollingStarfield01_720.png", 5)
        level.load_music("Gameplay Loop 1 (Loop @ 0_03_555 seconds).ogg")
        level.play_music()

        self.player = player(400, 300)

    def update(self):
        level.loop_music(3555, "end")
        super().update()

    def draw(self):
        self.scroll_background()
        self.screen.blit(self.titlerender, (0, 150))
        super().draw()
        pygame.display.flip()
