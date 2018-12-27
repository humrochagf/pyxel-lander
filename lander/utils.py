from collections import namedtuple

Sprite = namedtuple('Sprite', ['img', 'u', 'v', 'w', 'h'])


class Tile:

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
