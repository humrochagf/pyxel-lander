from random import choice

import pyxel
from pyxel import COLOR_BLACK, COLOR_GRAY

from pyxel_lander.utils import Sprite, Tile


class Moon:

    sprites = {
        "landing": [
            Sprite(0, 0, 16, 16, 16, COLOR_BLACK),
        ],
        "flat": [
            Sprite(0, 16, 16, 16, 16, COLOR_BLACK),
            Sprite(0, 32, 16, 16, 16, COLOR_BLACK),
            Sprite(0, 48, 16, 16, 16, COLOR_BLACK),
        ],
        "up": [
            Sprite(0, 0, 32, 16, 16, COLOR_BLACK),
            Sprite(0, 16, 32, 16, 16, COLOR_BLACK),
        ],
        "down": [
            Sprite(0, 32, 32, 16, 16, COLOR_BLACK),
            Sprite(0, 48, 32, 16, 16, COLOR_BLACK),
        ],
    }

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.surface = []

        self.load_surface()

    def load_surface(self):
        last_terrain = None
        y = self.h - 16
        overflow = 0
        surface_x_blocks = range(0, self.w, 16)
        landing_spot = choice(surface_x_blocks[1:-1])

        for x in surface_x_blocks:
            if x == landing_spot:
                terrain = "landing"
            else:
                terrain = choice(["flat", "up", "down"])

            if last_terrain in ["flat", "landing"] and terrain == "down":
                y += 16
            elif last_terrain == "up" and terrain in ["flat", "up", "landing"]:
                y -= 16
            elif last_terrain == "down" and terrain == "down":
                y += 16

            self.surface.append(
                Tile(x, y, choice(self.sprites[terrain])),
            )

            last_terrain = terrain

            terrain_overflow = y - (self.h - 16)

            if terrain_overflow > overflow:
                overflow = terrain_overflow

        if overflow:
            for tile in self.surface:
                tile.y -= overflow

    def draw(self):
        for tile in self.surface:
            pyxel.blt(
                tile.x,
                tile.y,
                tile.sprite.img,
                tile.sprite.u,
                tile.sprite.v,
                tile.sprite.w,
                tile.sprite.h,
                tile.sprite.colkey,
            )

            if tile.y < self.h - 16:
                pyxel.rect(tile.x, tile.y + 16, 16, self.h, COLOR_GRAY)
