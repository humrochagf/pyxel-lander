import os

import pyxel

from .lunar_module import LunarModule
from .moon import Moon

GRAVITY = 0.2
WIDTH = 192
HEIGHT = 192


class Game:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)

        pyxel.load(
            os.path.join(os.path.dirname(__file__), 'assets', 'assets.pyxres')
        )

        self.moon = Moon(WIDTH, HEIGHT)
        self.lunar_module = LunarModule(96, 50, GRAVITY)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_M):
            self.moon = Moon(WIDTH, HEIGHT)

        self.lunar_module.update(self.moon)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, 'Pyxel Lander', 7)
        pyxel.text(70, 5, f'fuel: {self.lunar_module.fuel:.2f}', 7)
        pyxel.text(140, 5, f'x: {self.lunar_module.velocity_x:.4f}', 7)
        pyxel.text(140, 15, f'y: {self.lunar_module.velocity_y:.4f}', 7)

        self.moon.draw()
        self.lunar_module.draw()
