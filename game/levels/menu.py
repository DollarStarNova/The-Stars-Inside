from game.libs.text.textFunctions import wrap_and_render_text
from game.levels.level import level
from game.libs.player.player import player
import pygame
import os
import random


class main_menu(level):
    def __init__(self, screen):

        self.titlerender = pygame.image.load(os.path.join(
            "game", "assets", "Art", "UI", "Title.png")).convert_alpha()
        self.titlerender = pygame.transform.scale(self.titlerender, (int(
            0.5*self.titlerender.get_width()), int(0.5*self.titlerender.get_height())))

        super().__init__(screen)
        self.set_background("HOr_ScrollingStarfield01_720.png", 1)
        level.load_music("The-Truth-Will-Be-Far-Stranger-_Edit_.ogg")
        level.play_music()
        self.healthbar.set_display(False)

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
        super().draw()
        self.screen.blit(self.titlerender, (self.screen.get_width(
        )/2-self.titlerender.get_width()/2, 50))
        pygame.display.flip()
