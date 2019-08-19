import os

import pyxel

from .constans import (
    FUEL, GRAVITY, HEIGHT, MAX_IMPACT_LIMIT, PERFECT_LANDING_LIMIT, WIDTH,
)
from .lunar_module import LunarModule
from .moon import Moon


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
        elif pyxel.btnp(pyxel.KEY_M) and not self.lunar_module:
            self.moon = Moon(WIDTH, HEIGHT)
        elif pyxel.btnp(pyxel.KEY_R) and self.lunar_module:
            del self.lunar_module
            self.lunar_module = None

        if self.lunar_module:
            self.lunar_module.update(self.moon)

    def draw_hud(self, fuel, velocity_x, velocity_y, status):
        rate = fuel / FUEL

        if rate < 0.2:
            fuel_color = 8
        elif rate < 0.5:
            fuel_color = 10
        else:
            fuel_color = 7

        if velocity_x > MAX_IMPACT_LIMIT:
            x_color = 8
        elif velocity_x > PERFECT_LANDING_LIMIT:
            x_color = 10
        else:
            x_color = 7

        if velocity_y > MAX_IMPACT_LIMIT:
            y_color = 8
        elif velocity_y > PERFECT_LANDING_LIMIT:
            y_color = 10
        else:
            y_color = 7

        pyxel.text(70, 5, f'fuel: {fuel:.2f}', fuel_color)
        pyxel.text(140, 5, f'x: {velocity_x:.4f}', x_color)
        pyxel.text(140, 15, f'y: {velocity_y:.4f}', y_color)

        if status == 'landed':
            pyxel.text(50, 80, f'Lunar Module Landed \\o/', 7)
        elif status == 'damaged':
            pyxel.text(34, 80, f'Lunar Module Landed... Barely...', 10)
        elif status == 'crashed':
            pyxel.text(54, 80, f'Lunar Module Crashed!', 8)
        elif status == 'lost':
            pyxel.text(22, 80, f'Contact with Lunar Module was Lost...', 7)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, 'Pyxel Lander', 7)

        self.moon.draw()

        if self.lunar_module:
            self.draw_hud(
                self.lunar_module.fuel,
                self.lunar_module.velocity_x,
                self.lunar_module.velocity_y,
                self.lunar_module.action,
            )

            self.lunar_module.draw()
        else:
            pyxel.text(18, 80, 'Press "s" to start or "m" to select map', 7)
