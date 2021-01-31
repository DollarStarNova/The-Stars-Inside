import pygame
import os
from game.libs.projectiles.projectile import projectile


class turret_manager():
    def __init__(self, screen):
        self.projectile = projectile()
        self.turret_delay = 30
        self.turret_list = {}
        self.sprite_path = os.path.join(
            "game", "assets", "Art", "Enemies", "Turret")
        self.art = [
            pygame.image.load(os.path.join(self.sprite_path,
                                           "enemy_iturret_body.png")).convert_alpha(),
            pygame.image.load(os.path.join(self.sprite_path,
                                           "enemy_iturret_head.png")).convert_alpha()
        ]
        self.blank_surface = pygame.Surface(
            (screen.get_size()[0]*1.1, screen.get_size()[1]), pygame.SRCALPHA, 32)

    def spawn_turret(self, x, y):
        rotation = 270
        if str(y) in self.turret_list:
            print("match")
        else:
            self.turret_list[str(y)] = [True, x,
                                        y, rotation, self.turret_delay]

    def draw(self, screen, xoffset):
        turret_images = self.blank_surface.copy()
        for turret in self.turret_list:
            turret_image = self.art[0]
            if self.turret_list[turret][0]:
                turret_image.blit(pygame.transform.rotate(
                    self.art[1], self.turret_list[turret][3]), (0, -20))
            turret_images.blit(
                turret_image, (self.turret_list[turret][1]-xoffset*64+xoffset*64 % 64, self.turret_list[turret][2]))
        return turret_images

    def update(self, playerxpos, playerypos, xoffset):

        for turret in self.turret_list:
            # self.turret_list[turret][3] = (
            #     self.turret_list[turret][3] + 1) % 360
            if self.turret_list[turret][4] > self.turret_delay:
                self.projectile.spawn(
                    self.turret_list[turret][1]-xoffset*64+xoffset*64 % 64, self.turret_list[turret][2], self.turret_list[turret][3])
                self.turret_list[turret][4] = 0
                print("spawn")
            self.turret_list[turret][4] += 1
            # self.turret_list[turret][3] += 1
            print(self.turret_list[turret])
        self.projectile.update()
