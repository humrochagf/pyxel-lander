import time

import pyxel

from .utils import Sprite

TRUSTER_FORCE = 0.5
FUEL = 100


class LunarModule:

    sprites = {
        'idle': [
            Sprite(0, 8, 0, 8, 8),
        ],
        'dead': [
            Sprite(0, 32, 0, 8, 8),
        ],
        'bottom-thruster': [
            Sprite(0, 0, 8, 8, 8),
            Sprite(0, 8, 8, 8, 8),
        ],
        'left-thruster': [
            Sprite(0, 16, 0, 8, 8),
            Sprite(0, 24, 0, 8, 8),
        ],
        'right-thruster': [
            Sprite(0, 16, 8, 8, 8),
            Sprite(0, 24, 8, 8, 8),
        ],
    }

    def __init__(self, x, y, gravity):
        self.x = x
        self.y = y
        self.action = 'idle'
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

    def update(self):
        thruster_x = 0
        thruster_y = 0

        if pyxel.btn(pyxel.KEY_DOWN) and self.fuel > 0:
            self.action = 'bottom-thruster'
            thruster_y = TRUSTER_FORCE
            self.fuel -= TRUSTER_FORCE
        elif pyxel.btn(pyxel.KEY_LEFT) and self.fuel > 0:
            self.action = 'left-thruster'
            thruster_x = TRUSTER_FORCE
            self.fuel -= TRUSTER_FORCE
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.fuel > 0:
            self.action = 'right-thruster'
            thruster_x = -TRUSTER_FORCE
            self.fuel -= TRUSTER_FORCE
        else:
            self.action = 'idle'

        time_step = self.get_time_step()

        self.velocity_x += thruster_x * time_step
        self.velocity_y += (self.gravity - thruster_y) * time_step

    def draw(self):
        frame = self.get_frame()

        self.x += self.velocity_x
        self.y += self.velocity_y

        pyxel.blt(
            self.x, self.y, frame.img, frame.u, frame.v, frame.w, frame.h,
        )
