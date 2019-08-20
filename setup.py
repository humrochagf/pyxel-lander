#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

PACKAGE = 'lander'
REQUIREMENTS = [
    'pyxel==1.2.5',
]

with open('README.md') as f:
    README = f.read()


CONSTANTS = {}
with open(os.path.join(PACKAGE, 'constans.py')) as constans_file:
    exec(constans_file.read(), CONSTANTS)

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
    package_data={PACKAGE: ['assets/assets.pyxres']},
    zip_safe=False,
    install_requires=REQUIREMENTS,
    python_requires='>=3.7',
    entry_points={
        'gui_scripts': ['pyxel-lander=lander:Game'],
    },
    platforms='any',
    keywords='pyxel games',
    classifiers=[
        'Environment :: X11 Applications',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Desktop Environment',
        'Topic :: Games/Entertainment :: Arcade',
        'Topic :: Games/Entertainment :: Simulation',
    ],
)
