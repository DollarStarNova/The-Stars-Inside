import pygame
import os
from game.libs.text.textFunctions import wrap_and_render_text
from game.libs.player.player import player
from game.libs.player.healthbar import healthbar
import pytmx
from game.libs.enemies.turret import turret_manager


class level():

    def __init__(self, screen):
        if not hasattr(self, "player"):
            self.player = player(0, screen.get_height()/2)
        self.healthbar = healthbar()
        self.healthbar.set_display(True)
        self.screen = screen
        self.xoffset = 0
        self.yoffset = 0
        self.tile_list = []
        self.stop_scrolling = False
        self.turret_manager = turret_manager(screen)
        # self.enemy_list = []
        # x = y = 0
        # while x < 500:
        #     self.enemy_list.append([])
        #     while y < 20:
        #         self.enemy_list[x].append(False)
        #         y += 1
        #     x += 1
        #     y = 0

        pygame.mixer.pre_init()

    def set_background(self, filename, x_scroll_rate):
        self.background = pygame.image.load(
            os.path.join("game", "assets", "Art", "Environment", filename)).convert()
        self.x_scroll_rate = x_scroll_rate
        self.bg_x = self.bg_y = 0
        self.bg_w, self.bg_h = self.screen.get_size()
        self.bg_second_image_x = self.bg_w

    def scroll_background(self):
        self.screen.blit(self.background, (0, 0), pygame.Rect(
            self.bg_x, self.bg_y, self.bg_w, self.bg_h))
        self.bg_x += self.x_scroll_rate
        if self.bg_x > self.background.get_size()[0] - self.bg_w:
            self.screen.blit(
                self.background, (self.bg_second_image_x, 0), pygame.Rect(0, self.bg_y, self.bg_w, self.bg_h))
            self.bg_second_image_x -= self.x_scroll_rate
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
        if hasattr(self, "player"):
            self.player.update(self.screen)
        if hasattr(self, "healthbar"):
            self.healthbar.update()
        if hasattr(self, "turret_manager"):
            self.turret_manager.update(
                self.player.xpos, self.player.ypos, self.xoffset)
        if hasattr(self, "scroll_speed") and not self.stop_scrolling:
            self.xoffset += self.scroll_speed
            if self.xoffset > self.max_x_offset:
                self.xoffset = self.max_x_offset

    def draw(self):
        turrets = None
        if hasattr(self, "turret_manager"):
            turrets = self.turret_manager.draw(self.screen, self.xoffset)
        tile_surface = self.draw_tiles()
        self.screen.blit(self.tilemapsurface, (-self.tilesize -
                                               self.xoffset % 1 * self.tilesize, 0))
        if turrets is not None:
            self.turret_manager.projectile.draw(self.screen)
            self.screen.blit(turrets, (-self.tilesize -
                                       self.xoffset % 1 * self.tilesize, 0))
        if hasattr(self, "player"):
            self.player.draw(self.screen)
        if hasattr(self, "healthbar"):
            self.healthbar.draw(self.screen)

    def handle_event(self, event):
        if hasattr(self, "player"):
            self.player.handle_event(event)

    def load_tilemap(self, mapname):
        self.tilemapsurface = pygame.Surface(
            (int(self.screen.get_width()*1.1), self.screen.get_height()), pygame.SRCALPHA, 32)
        tilemappath = os.path.join(
            "game", "assets", "tilemaps", mapname)
        self.tilemap = pytmx.load_pygame(tilemappath)
        self.tilesize = self.tilemap.tilewidth
        self.max_x_offset = self.tilemap.width - self.screen.get_width()/self.tilesize

    def draw_tiles(self):
        xoffset = int(self.xoffset)
        if xoffset != self.max_x_offset:
            self._advance_tiles()
        for tile in self.tile_list:
            # if tile[3] == 2:
            #     tile_size = self.tilesize*2
            # else:
            #     tile_size = self.tilesize
            if tile[0] is not None:
                if tile[3] != 2:
                    self.tilemapsurface.blit(tile[0], (tile[1], tile[2]))
                elif tile[4] is not None:
                    self.spawn_enemy(tile[1]-self.xoffset, tile[2], tile[4])
        return self.tilemapsurface

    def _advance_tiles(self):
        x = 0
        y = 0
        tile_size = self.tilesize
        tile_layer_list = [0, 1, 2]
        xoffset = int(self.xoffset)
        yoffset = int(self.yoffset)
        self.tile_list = []
        for tile_layer in tile_layer_list:
            if tile_layer == 2:
                yoffset = yoffset+1
            while x * tile_size < self.screen.get_width()*1.1:
                while y * tile_size < self.screen.get_height():
                    myx = x+xoffset
                    myy = y+yoffset
                    myxpos = x*tile_size
                    myypos = y*(tile_size-1)
                    try:
                        tiledata = [self.tilemap.get_tile_image(
                            myx, myy, tile_layer), myxpos, myypos, tile_layer]
                        if tile_layer == 2:
                            tiledata.append(
                                self.tilemap.get_tile_properties(myx, myy, tile_layer))

                    except(ValueError):
                        if tile_layer == 0:
                            self.stop_scrolling = True
                    if type(tiledata) == list:
                        self.tile_list.append(
                            tiledata)
                    y += 1
                y = 0
                x += 1
            x = 0

    def spawn_enemy(self, x, y, data):
        if data["id"] == 0:
            self.turret_manager.spawn_turret(x+self.xoffset*64, y)
