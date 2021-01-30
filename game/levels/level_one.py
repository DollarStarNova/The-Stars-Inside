import pygame
import os
import pytmx
from game.levels.level import level


class level_one(level):
    def __init__(self, screen):
        self.xoffset = 0
        self.yoffset = 0
        self.tile_list = []
        self.stop_scrolling = False
        self.scroll_speed = 0.05

        super().__init__(screen)
        self.tilemapsurface = pygame.Surface(
            (int(self.screen.get_width()*1.1), self.screen.get_height()), pygame.SRCALPHA, 32)
        tilemappath = os.path.join(
            "game", "assets", "tilemaps", "level1.tmx")
        self.tilemap = pytmx.load_pygame(tilemappath)
        self.tilesize = self.tilemap.tilewidth
        self.max_x_offset = self.tilemap.width - screen.get_width()/self.tilesize
        level.load_music(os.path.join("Gameplay Loops",
                                      "Gameplay Loop 1 (Loop @ 0_03_555 seconds).ogg"))
        level.play_music()

    def update(self):
        if not self.stop_scrolling:
            self.xoffset += self.scroll_speed
            if self.xoffset > self.max_x_offset:
                self.xoffset = self.max_x_offset
        self.player.update(self.screen)
        level.loop_music(3555, "end")

    def draw(self):
        # self.screen.blit(self.background, (0, 0))

        x = 0
        y = 0
        tile_size = self.tilesize
        tile_layer = 0
        xoffset = int(self.xoffset)
        yoffset = int(self.yoffset)
        if xoffset != self.max_x_offset:
            self.tile_list = []
            while x * tile_size < self.screen.get_width()*1.1:
                while y * tile_size < self.screen.get_height():
                    myx = x+xoffset
                    myy = y+yoffset
                    myxpos = x*64
                    myypos = y*63
                    try:
                        tiledata = [self.tilemap.get_tile_image(
                            myx, myy, tile_layer), myxpos, myypos]
                    except(ValueError):
                        self.stop_scrolling = True
                        pass
                    if type(tiledata) == list:
                        self.tile_list.append(
                            tiledata)
                    y += 1
                y = 0
                x += 1
            x = 0
        for tile in self.tile_list:
            if tile[0] is not None:
                self.tilemapsurface.blit(tile[0], (tile[1], tile[2]))
        self.screen.blit(self.tilemapsurface, (-self.tilesize -
                                               self.xoffset % 1 * self.tilesize, 0))
        self.player.draw(self.screen)
        pygame.display.flip()
