import time

import pyxel
from pyxel import COLOR_BLACK

from pyxel_lander.constants import (
    FUEL,
    MAX_IMPACT_LIMIT,
    PERFECT_LANDING_LIMIT,
    PLATFORM_COLOR,
    THRUSTERS_FORCE,
)
from pyxel_lander.utils import Sprite


class LunarModule:

    sprites = {
        "idle": [
            Sprite(0, 8, 0, 8, 8, COLOR_BLACK),
        ],
        "lost": [
            Sprite(0, 8, 0, 8, 8, COLOR_BLACK),
        ],
        "landed": [
            Sprite(0, 8, 0, 8, 8, COLOR_BLACK),
        ],
        "crashed": [
            Sprite(0, 32, 0, 8, 8, COLOR_BLACK),
            Sprite(0, 32, 8, 8, 8, COLOR_BLACK),
        ],
        "damaged": [
            Sprite(0, 40, 0, 8, 8, COLOR_BLACK),
            Sprite(0, 40, 8, 8, 8, COLOR_BLACK),
        ],
        "bottom-thruster": [
            Sprite(0, 0, 8, 8, 8, COLOR_BLACK),
            Sprite(0, 8, 8, 8, 8, COLOR_BLACK),
        ],
        "left-thruster": [
            Sprite(0, 16, 0, 8, 8, COLOR_BLACK),
            Sprite(0, 24, 0, 8, 8, COLOR_BLACK),
        ],
        "right-thruster": [
            Sprite(0, 16, 8, 8, 8, COLOR_BLACK),
            Sprite(0, 24, 8, 8, 8, COLOR_BLACK),
        ],
    }

    flag = Sprite(0, 48, 0, 8, 8, COLOR_BLACK)

    def __init__(self, x, y, gravity):
        self.x = x
        self.y = y
        self.action = "idle"
        self.gravity = gravity
        self.velocity_x = 0
        self.velocity_y = 0
        self.fuel = FUEL
        self.last_time = time.time()

    def get_frame(self):
        frames = self.sprites[self.action]

        return frames[int(time.time() % len(frames))]

    def get_time_step(self):
        current_time = time.time()

        time_step = current_time - self.last_time

        self.last_time = current_time

        return time_step

    def check_collision(self, moon):
        # lost contact with lunar module
        if self.x > moon.w or self.x < -8:
            return -1

        # check for collision with the moon surface
        for surface in moon.surface:
            y = int(self.y + 8 - surface.y)

            if y >= 0 and y < 16:
                left_x = int(self.x - surface.x)
                right_x = int(self.x + 8 - surface.x)

                # check for overlapping with the module left leg
                if left_x >= 0 and left_x < 16:
                    collision_value = pyxel.image(surface.sprite.img).pget(
                        surface.sprite.u + left_x,
                        surface.sprite.v + y,
                    )

                    if collision_value:
                        return collision_value

                # check for overlapping with the module right leg
                if right_x >= 0 and right_x < 16:
                    collision_value = pyxel.image(surface.sprite.img).pget(
                        surface.sprite.u + right_x,
                        surface.sprite.v + y,
                    )

                    if collision_value:
                        return collision_value

        return 0

    def update(self, moon):
        collision_value = self.check_collision(moon)

        if collision_value:
            if collision_value == PLATFORM_COLOR:
                vx = self.velocity_x
                vy = self.velocity_y

                if vx > MAX_IMPACT_LIMIT or vy > MAX_IMPACT_LIMIT:
                    self.action = "crashed"
                elif vx > PERFECT_LANDING_LIMIT or vy > PERFECT_LANDING_LIMIT:
                    self.action = "damaged"
                else:
                    self.action = "landed"
            elif collision_value == -1:
                self.action = "lost"
            else:
                self.action = "crashed"
        else:
            thruster_x = 0
            thruster_y = 0

            if pyxel.btn(pyxel.KEY_DOWN) and self.fuel > 0:
                self.action = "bottom-thruster"

                if self.fuel > THRUSTERS_FORCE:
                    thruster_y = THRUSTERS_FORCE
                else:
                    thruster_y = self.fuel
            elif pyxel.btn(pyxel.KEY_LEFT) and self.fuel > 0:
                self.action = "left-thruster"

                if self.fuel > THRUSTERS_FORCE:
                    thruster_x = THRUSTERS_FORCE
                else:
                    thruster_x = self.fuel
            elif pyxel.btn(pyxel.KEY_RIGHT) and self.fuel > 0:
                self.action = "right-thruster"

                if self.fuel > THRUSTERS_FORCE:
                    thruster_x = -THRUSTERS_FORCE
                else:
                    thruster_x = -self.fuel
            else:
                self.action = "idle"

            self.fuel -= abs(thruster_x) + abs(thruster_y)

            time_step = self.get_time_step()

            self.velocity_x += thruster_x * time_step
            self.velocity_y += (self.gravity - thruster_y) * time_step

            self.x += self.velocity_x
            self.y += self.velocity_y

    def draw(self):
        frame = self.get_frame()

        pyxel.blt(
            self.x,
            self.y,
            frame.img,
            frame.u,
            frame.v,
            frame.w,
            frame.h,
            frame.colkey,
        )

        if self.action == "landed":
            pyxel.blt(
                self.x + 8,
                self.y,
                self.flag.img,
                self.flag.u,
                self.flag.v,
                self.flag.w,
                self.flag.h,
                self.flag.colkey,
            )
