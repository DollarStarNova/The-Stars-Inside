import pygame
import sys
from libs.text.textFunctions import wrap_and_render_text

if __name__ == "__main__":
    screen = pygame.display.set_mode(size=(800, 600))
    pygame.init()
    MainFontLarge = pygame.font.Font(
        "assets/fonts/SpaceAndAstronomy-pZRD.ttf", 32)
    quote = "Space is big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think it's a long way down the road to the chemist's, but that's just peanuts to space."
    quoterender = wrap_and_render_text(quote, MainFontLarge, (700, 500))

    background = pygame.image.load(
        "assets\images\HOr_ScrollingStarfield01.png", "starfield_background")
    background = pygame.transform.smoothscale(
        background, (int(0.75*background.get_size()[0]), int(0.75*background.get_size()[1])))

    pygame.display.update()
    FPS = 60
    fpsClock = pygame.time.Clock()

    running = True
    x = y = 0
    w, h = 800, 600
    second_image_x = w
    X_SCROLL_RATE = 0.5

    while running:

        screen.blit(background, (0, 0), pygame.Rect(x, y, w, h))
        x += X_SCROLL_RATE
        if x > background.get_size()[0] - w:
            screen.blit(
                background, (second_image_x, 0), pygame.Rect(0, y, w, h))
            second_image_x -= X_SCROLL_RATE
        if x > background.get_size()[0]:
            x = 0
            second_image_x = w
        screen.blit(quoterender, (75, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fpsClock.tick(FPS)
    pygame.quit()
    sys.exit(0)
