#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

MAIN_MODULE = 'pyxel_lander'
CONSTANTS = {}

with open(os.path.join(MAIN_MODULE, 'constants.py')) as constans_file:
    exec(constans_file.read(), CONSTANTS)

with open('README.md') as f:
    README = f.read()

setup(
    name='pyxel-lander',
    version=CONSTANTS['VERSION'],
    description=(
        'Lunar Lander game tribute written in Python with '
        'Pyxel retro game engine'
    ),
    long_description=README,
    long_description_content_type='text/markdown',
    author=CONSTANTS['AUTHOR'],
    author_email=CONSTANTS['EMAIL'],
    url='https://github.com/humrochagf/pyxel-lander',
    license='MIT',
    packages=find_packages(),
    package_data={
        MAIN_MODULE: ['assets/assets.pyxres'],
    },
    zip_safe=False,
    install_requires=[
        'pyxel>=1.4.0',
    ],
    python_requires='>=3.7',
    entry_points={
        'gui_scripts': [f'pyxel-lander={MAIN_MODULE}:Game'],
    },
    platforms='any',
    keywords='pyxel games',
    classifiers=[
        'Environment :: X11 Applications',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Desktop Environment',
        'Topic :: Games/Entertainment :: Arcade',
        'Topic :: Games/Entertainment :: Simulation',
    ],
)
