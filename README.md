# Pyxel Lander

Lunar Lander game tribute written in Python with [Pyxel](https://github.com/kitao/pyxel) retro game engine.

![screenshot](https://raw.githubusercontent.com/humrochagf/pyxel-lander/master/images/screenshot.png)

## Features

- Procedural map generation
- Pixel perfect collision detection
- Fuel propulsion system
- HUD with the Lunar Module feedback
- Landing impact detection

## Controls

- Use the `arrow` keys to control the Lunar Module.
- The `s` key starts the game.
- You can change maps with the `m` key on the menu.
- The `r` key restarts the game.
- You can exit the game with the `q` or `esc` keys.

## Packaged executable

If you want to play the game without installing the development tools you can check it on [itch.io](https://humrochagf.itch.io/pyxel-lander).

## PyPI Installation

This game runs with Python 3.7 or above.

You can use [pipx](https://pipxproject.github.io/pipx/) to install the game and have it available as an standalone program:

```shell
$ pipx install pyxel-lander
```

Then you can run the game running:

```shell
$ pyxel-lander
```

**Warning:** The Pyxel requirement uses external libraries, make sure you have them all installed by looking into its [docs](https://github.com/kitao/pyxel#how-to-install).

## Running from source code

To run it from the source code you need first to clone from the repository:

```shell
$ git clone https://github.com/humrochagf/pyxel-lander.git
```

After cloned, go to the folder, set up the `venv` and install its requirements:

```shell
$ cd pyxel-lander/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

With everything installed run the game with:

```shell
$ python pyxel-lander.py
```
