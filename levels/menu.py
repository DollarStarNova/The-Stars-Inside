import pygame
from libs.text.textFunctions import wrap_and_render_text


class main_menu():
    def __init__(self, screen):
        self.screen = screen

        MainFontLarge = pygame.font.Font(
            "assets/fonts/SpaceAndAstronomy-pZRD.ttf", 32)
        quote = "Space is big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think it's a long way down the road to the chemist's, but that's just peanuts to space."
        self.quoterender = wrap_and_render_text(
            quote, MainFontLarge, (700, 500))

        background = pygame.image.load(
            "assets\images\HOr_ScrollingStarfield01.png", "starfield_background")
        self.background = pygame.transform.smoothscale(
            background, (int(0.75*background.get_size()[0]), int(0.75*background.get_size()[1])))

        self.x = self.y = 0
        self.w, self.h = screen.get_size()
        self.second_image_x = self.w
        self.X_SCROLL_RATE = 0.5

    def update(self):
        'for future use'
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0), pygame.Rect(
            self.x, self.y, self.w, self.h))
        self.x += self.X_SCROLL_RATE
        if self.x > self.background.get_size()[0] - self.w:
            self.screen.blit(
                self.background, (self.second_image_x, 0), pygame.Rect(0, self.y, self.w, self.h))
            self.second_image_x -= self.X_SCROLL_RATE
        if self.x > self.background.get_size()[0]:
            self.x = 0
            self.second_image_x = w
        self.screen.blit(self.quoterender, (75, 200))
        pygame.display.flip()
