import pygame
import os


class player():
    def __init__(self, xpos, ypos, rotation=270):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = 0
        self.yvel = 0
        self.rotation = rotation
        self.acc = 1
        self.max_speed = 8
        self.breaking_force = 0.05
        sprite_path = os.path.join(
            "game", "assets", "Art", "Player1ship_Placeholder.png")
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def move(self, dir):
        if dir == "down":
            self.yvel = min(self.yvel+self.acc, self.max_speed)
        if dir == "up":
            self.yvel = max(self.yvel-self.acc, -self.max_speed)
        if dir == "right":
            self.xvel = min(self.xvel+self.acc, self.max_speed)
        if dir == "left":
            self.xvel = max(self.xvel-self.acc, -self.max_speed)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.move("down")
        if keys[pygame.K_w]:
            self.move("up")
        if keys[pygame.K_a]:
            self.move("left")
        if keys[pygame.K_d]:
            self.move("right")

        if self.yvel != 0:
            self.ypos += self.yvel
            if self.yvel > 0:
                self.yvel = max(self.yvel - self.breaking_force, 0)
            else:
                self.yvel = min(self.yvel + self.breaking_force, 0)
        if self.xvel != 0:
            self.xpos += self.xvel
            if self.xvel > 0:
                self.xvel = max(self.xvel - self.breaking_force, 0)
            else:
                self.xvel = min(self.xvel + self.breaking_force, 0)

    def draw(self, surface):
        surface.blit(self.sprite, (self.xpos-self.width /
                                   2, self.ypos-self.height/2))

    def handle_event(self, event):
        #
        pass
