import os

import pyxel

from .lunar_module import LunarModule
from .moon import Moon

GRAVITY = 0.2


class Game:

    def __init__(self):
        pyxel.init(180, 135)

        pyxel.load(
            os.path.join(os.path.dirname(__file__), 'assets', 'assets.pyxel')
        )

        self.moon = Moon(180, 135)
        self.lunar_module = LunarModule(50, 50, GRAVITY)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.lunar_module.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, 'Pyxel Lander', 7)
        pyxel.text(70, 5, f'fuel: {self.lunar_module.fuel:.2f}', 7)
        pyxel.text(140, 5, f'x: {self.lunar_module.velocity_x:.4f}', 7)
        pyxel.text(140, 15, f'y: {self.lunar_module.velocity_y:.4f}', 7)

        self.moon.draw()
        self.lunar_module.draw()
