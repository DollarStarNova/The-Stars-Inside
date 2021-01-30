import pygame
import os
from game.libs.projectiles.player_projectile import player_projectile


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
        self.respect_map_bounds_bool = 1
        self.sprites = self.load_sprites(["Player1ship_Placeholder.png", "Player1ship_Placeholder_turnleft.png",
                                          "Player1ship_Placeholder_turnright.png", "Player1ship_Placeholder_hurt.png"], 270)
        self.current_sprite = self.sprites[0]
        self.player_projectile = player_projectile()

    def move(self, dir):
        if dir == 0:
            self.yvel = min(self.yvel+self.acc, self.max_speed)
        if dir == 1:
            self.yvel = max(self.yvel-self.acc, -self.max_speed)
        if dir == 2:
            self.xvel = max(self.xvel-self.acc, -self.max_speed)
        if dir == 3:
            self.xvel = min(self.xvel+self.acc, self.max_speed)

    def shoot(self):
        self.player_projectile.spawn(
            self.xpos, self.ypos-self.current_sprite["width"]/4, self.xvel, self.yvel)

    def update(self, surface):
        if self.player_projectile.count > 0:
            self.player_projectile.update(surface)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(0)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(1)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move(2)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move(3)
        if keys[pygame.K_SPACE]:
            self.shoot()

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

        if self.respect_map_bounds_bool:
            self.xpos = max(self.xpos, self.current_sprite["width"]/2)
            self.xpos = min(self.xpos, surface.get_width() -
                            self.current_sprite["width"]/2)
            self.ypos = max(self.ypos, self.current_sprite["height"]/2)
            self.ypos = min(self.ypos, surface.get_height() -
                            self.current_sprite["height"]/2)

    def draw(self, surface):
        if self.player_projectile.count > 0:
            self.player_projectile.draw(surface)

        if self.yvel > 6:
            self.current_sprite = self.sprites[2]
        elif self.yvel < -6:
            self.current_sprite = self.sprites[1]
        else:
            self.current_sprite = self.sprites[0]

        surface.blit(self.current_sprite["image"], (self.xpos-self.current_sprite["width"] /
                                                    2, self.ypos-self.current_sprite["height"]/2))

    def handle_event(self, event):
        #
        pass

    def load_sprites(self, sprite_list, rotation):
        sprites = []
        i = 0
        for sprite in sprite_list:
            sprite_path = os.path.join(
                "game", "assets", "Art", sprite)

            sprites.append({})
            tempimage = pygame.image.load(sprite_path).convert_alpha()
            sprites[i]["image"] = pygame.transform.rotate(tempimage, rotation)
            sprites[i]["width"] = sprites[i]["image"].get_width()
            sprites[i]["height"] = sprites[i]["image"].get_height()
            i += 1
        return sprites

    def respect_map_bounds(self, respect_bounds):
        if respect_bounds:
            self.respect_map_bounds_bool = 1
        else:
            self.respect_map_bounds_bool = 0
