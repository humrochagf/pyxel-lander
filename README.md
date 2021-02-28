# Pyxel Lander

[![PyPI](https://img.shields.io/pypi/v/pyxel-lander.svg)](https://pypi.org/project/pyxel-lander/)
[![PyPI - License](https://img.shields.io/pypi/l/pyxel-lander.svg)](https://pypi.org/project/pyxel-lander/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyxel-lander.svg)](https://pypi.org/project/pyxel-lander/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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

### Adding it to application laucher (Linux Only)

To be able to open the game without having to open a terminal and type `./pyxel-lander` you can add it as an application using the `.desktop` file.

Create a file called `pyxel-lander.desktop` inside your user applications path:

```shell
$ touch ~/.local/share/applications/pyxel-lander.desktop
```

**Obs.:** This path was tested on Debian based distros, it can be different on other linux flavours.

Add this content to the file changing just the paths to match the location were you downloaded the game:

```
[Desktop Entry]
Name=Pyxel Lander
Exec=/GAME_FOLDER_PATH/pyxel-lander
Terminal=false
Type=Application
Icon=/GAME_FOLDER_PATH/icon.png
```

Now you have the game available on your application launcher (Gnome, KDE, Xfce, etc...)

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
