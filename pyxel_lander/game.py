import os

import pyxel
from pyxel import COLOR_BLACK, COLOR_RED, COLOR_WHITE, COLOR_YELLOW

from pyxel_lander.constants import (
    AUTHOR_HANDLE,
    FUEL,
    GRAVITY,
    HEIGHT,
    MAX_IMPACT_LIMIT,
    PERFECT_LANDING_LIMIT,
    VERSION,
    WIDTH,
)
from pyxel_lander.lunar_module import LunarModule
from pyxel_lander.moon import Moon


class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)

        pyxel.load(
            os.path.join(os.path.dirname(__file__), "assets", "assets.pyxres"),
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
            fuel_color = COLOR_RED
        elif rate < 0.5:
            fuel_color = COLOR_YELLOW
        else:
            fuel_color = COLOR_WHITE

        if velocity_x > MAX_IMPACT_LIMIT:
            x_color = COLOR_RED
        elif velocity_x > PERFECT_LANDING_LIMIT:
            x_color = COLOR_YELLOW
        else:
            x_color = COLOR_WHITE

        if velocity_y > MAX_IMPACT_LIMIT:
            y_color = COLOR_RED
        elif velocity_y > PERFECT_LANDING_LIMIT:
            y_color = COLOR_YELLOW
        else:
            y_color = COLOR_WHITE

        pyxel.text(70, 5, f"fuel: {fuel:.2f}", fuel_color)
        pyxel.text(140, 5, f"x: {velocity_x:.4f}", x_color)
        pyxel.text(140, 15, f"y: {velocity_y:.4f}", y_color)

        if status == "landed":
            pyxel.text(50, 80, "Lunar Module Landed \\o/", COLOR_WHITE)
        elif status == "damaged":
            pyxel.text(
                34, 80, "Lunar Module Landed... Barely...", COLOR_YELLOW
            )
        elif status == "crashed":
            pyxel.text(54, 80, "Lunar Module Crashed!", COLOR_RED)
        elif status == "lost":
            pyxel.text(
                22, 80, "Contact with Lunar Module was Lost...", COLOR_WHITE
            )

    def draw(self):
        pyxel.cls(COLOR_BLACK)
        pyxel.text(5, 5, "Pyxel Lander", COLOR_WHITE)

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
            pyxel.text(
                18, 60, 'Press "s" to start or "m" to select map', COLOR_WHITE
            )
            pyxel.text(44, 76, "Made with", COLOR_WHITE)
            pyxel.text(82, 76, "<3", COLOR_RED)
            pyxel.text(92, 76, f"by {AUTHOR_HANDLE}", COLOR_WHITE)
            pyxel.text(72, 92, f"Version {VERSION}", COLOR_WHITE)
