import os

import pyxel

from .lunar_module import (
    CRASH_LIMIT_SPEED, FUEL, LAND_LIMIT_SPEED, LunarModule,
)
from .moon import Moon

GRAVITY = 0.2
WIDTH = 192
HEIGHT = 192


class Game:

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)

        pyxel.load(
            os.path.join(os.path.dirname(__file__), 'assets', 'assets.pyxres'),
        )

        self.lunar_module = None
        self.moon = Moon(WIDTH, HEIGHT)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_S):
            self.lunar_module = LunarModule(96, 50, GRAVITY)
        elif pyxel.btnp(pyxel.KEY_M):
            self.moon = Moon(WIDTH, HEIGHT)
        elif pyxel.btnp(pyxel.KEY_R) and self.lunar_module:
            del self.lunar_module
            self.lunar_module = None

        if self.lunar_module:
            self.lunar_module.update(self.moon)

    def draw_hud(self, fuel, velocity_x, velocity_y):
        rate = fuel / FUEL

        if rate < 0.2:
            fuel_color = 8
        elif rate < 0.5:
            fuel_color = 10
        else:
            fuel_color = 7

        if velocity_x > CRASH_LIMIT_SPEED:
            x_color = 8
        elif velocity_x > LAND_LIMIT_SPEED:
            x_color = 10
        else:
            x_color = 7

        if velocity_y > CRASH_LIMIT_SPEED:
            y_color = 8
        elif velocity_y > LAND_LIMIT_SPEED:
            y_color = 10
        else:
            y_color = 7

        pyxel.text(70, 5, f'fuel: {fuel:.2f}', fuel_color)
        pyxel.text(140, 5, f'x: {velocity_x:.4f}', x_color)
        pyxel.text(140, 15, f'y: {velocity_y:.4f}', y_color)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, 'Pyxel Lander', 7)

        self.moon.draw()

        if self.lunar_module:
            self.draw_hud(
                self.lunar_module.fuel,
                self.lunar_module.velocity_x,
                self.lunar_module.velocity_y,
            )

            self.lunar_module.draw()
        else:
            pyxel.text(18, 80, 'Press "s" to start or "m" to select map', 7)
