import pygame
import os


class player_projectile():

    def __init__(self):
        self.count = 0
        self.spritepath = os.path.join(
            "game", "assets", "Art", "Projectiles", "Projectiles_0001_basic-shot.png")
        self.sprite = pygame.image.load(
            self.spritepath, "Projectile").convert_alpha()
        self.sprite = pygame.transform.rotate(self.sprite, 270)

        self.last_shot = 0

        self.current_projectile = {
            "speed": 20,
            "life": 30,
            "delay": 5,
            "sprite": self.sprite
        }

        self.instances = []

    def spawn(self, xpos, ypos, xvel, yvel):
        if self.last_shot <= 0:
            self.count += 1
            self.instances.append(
                {
                    "xpos": xpos,
                    "ypos": ypos,
                    "xvel": xvel+self.current_projectile["speed"],
                    "yvel": yvel,
                    "life": self.current_projectile["life"],
                    "lifetime": 0,
                    "sprite": self.current_projectile["sprite"]
                }
            )
            self.last_shot = self.current_projectile["delay"]
        self.last_shot = max(0, self.last_shot - 1)

    def update(self, surface):
        if self.count > 0:
            for bullet in self.instances:
                bullet["xpos"] += bullet["xvel"]
                bullet["ypos"] += bullet["yvel"]
                bullet["lifetime"] += 1
                if bullet["lifetime"] > bullet["life"]:
                    self.instances.pop(self.instances.index(bullet))
        self.count = len(self.instances)

    def draw(self, surface):
        for bullet in self.instances:
            surface.blit(bullet["sprite"], (bullet["xpos"], bullet["ypos"]))
