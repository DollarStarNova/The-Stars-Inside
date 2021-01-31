import pygame
import os


class healthbar():
    def __init__(self, position=(50, 50)):
        self.displayed = False
        self.position = position
        self.image_dir = os.path.join("game", "assets", "Art", "UI")
        self.offbarimage = pygame.image.load(os.path.join(
            self.image_dir, "UI_Health_health-baroff.png")).convert_alpha()
        self.onbarimage = pygame.image.load(os.path.join(
            self.image_dir, "UI_Health_health-baron.png")).convert_alpha()
        self.frameimage = pygame.image.load(os.path.join(
            self.image_dir, "UI_Health_healthbarframe.png")).convert_alpha()
        self.fullsize = self.offbarimage.get_width()
        self.health = self.fullsize
        self.drain_health = True

    def update(self):
        if self.displayed:
            if self.drain_health:
                self.health = max(self.health-1, 25)
            else:
                self.health = min(self.health+1, self.fullsize)
            if self.health == 25:
                self.drain_health = False
            if self.health == self.fullsize:
                self.drain_health = True

    def draw(self, screen):
        if self.displayed:
            onbar = pygame.transform.scale(
                self.onbarimage, (self.health, self.onbarimage.get_height()))
            screen.blit(self.offbarimage, self.position)
            screen.blit(onbar, self.position)
            screen.blit(self.frameimage,
                        (self.position[0]-10, self.position[1]-20))

    def set_display(self, do_display):
        if do_display:
            self.displayed = True
        else:
            self.displayed = False
