from random import choice

import pyxel

from .utils import Sprite, Tile


class Moon:

    sprites = {
        'landing-spot': [
            Sprite(0, 0, 16, 16, 16),
        ],
        'filling': [
            Sprite(0, 48, 0, 16, 16),
        ],
        'flat': [
            Sprite(0, 16, 16, 16, 16),
            Sprite(0, 32, 16, 16, 16),
            Sprite(0, 48, 16, 16, 16),
        ],
        'up': [
            Sprite(0, 0, 32, 16, 16),
            Sprite(0, 16, 32, 16, 16),
        ],
        'down': [
            Sprite(0, 32, 32, 16, 16),
            Sprite(0, 48, 32, 16, 16),
        ],
    }

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.surface = []
        self.start_y = h - 16

        self.load_surface()

    def load_surface(self):
        y = self.h - 16

        for x in range(0, self.w + 16, 16):
            terrain = choice(['flat', 'up', 'down'])

            self.surface.append(
                Tile(x, y, choice(self.sprites[terrain]))
            )

            if terrain == 'up':
                y -= 16
            elif terrain == 'down':
                y += 16

    def draw(self):
        for tile in self.surface:
            pyxel.blt(
                tile.x, tile.y, tile.sprite.img,
                tile.sprite.u, tile.sprite.v,
                tile.sprite.w, tile.sprite.h,
            )
