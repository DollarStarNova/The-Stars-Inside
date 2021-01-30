import pygame
import os
from game.libs.text.textFunctions import wrap_and_render_text


class level():

    def __init__(self, screen):
        self.screen = screen
        pygame.mixer.pre_init()

    def set_background(self, filename, X_SCROLL_RATE):
        self.background = pygame.image.load(
            os.path.join("game", "assets", "Art", filename)).convert()
        self.X_SCROLL_RATE = X_SCROLL_RATE
        self.bg_x = self.bg_y = 0
        self.bg_w, self.bg_h = self.screen.get_size()
        self.bg_second_image_x = self.bg_w

    def scroll_background(self):
        self.screen.blit(self.background, (0, 0), pygame.Rect(
            self.bg_x, self.bg_y, self.bg_w, self.bg_h))
        self.bg_x += self.X_SCROLL_RATE
        if self.bg_x > self.background.get_size()[0] - self.bg_w:
            self.screen.blit(
                self.background, (self.bg_second_image_x, 0), pygame.Rect(0, self.bg_y, self.bg_w, self.bg_h))
            self.bg_second_image_x -= self.X_SCROLL_RATE
        if self.bg_x > self.background.get_size()[0]:
            self.bg_x = 0
            self.bg_second_image_x = self.bg_w

    @staticmethod
    def load_music(filename):
        pygame.mixer.music.load(
            os.path.join("game", "assets", "music", filename))

    @staticmethod
    def play_music():
        pygame.mixer.music.play()

    @staticmethod
    def loop_music(from_pos, to_pos):
        if to_pos == "end":
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.set_pos(from_pos)
                pygame.mixer.music.play()
        elif pygame.mixer.music.get_pos() > to_pos:
            pygame.mixer.music.set_pos(from_pos)
            pygame.mixer.music.play()

    def update(self):
        if self.player:
            self.player.update(self.screen)

    def draw(self):
        if self.player:
            self.player.draw(self.screen)

    def handle_event(self, event):
        if self.player:
            self.player.handle_event(event)
