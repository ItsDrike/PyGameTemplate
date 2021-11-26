# Template code for developing games with PyGame

[![gplv3](https://img.shields.io/badge/Licensed%20under-GPL%20v3-red.svg?style=flat-square)](./LICENSE)
[![validation workflow](https://github.com/ItsDrike/PyGameTemplate/actions/workflows/validation.yml/badge.svg)](https://github.com/ItsDrike/PyGameTemplate/actions/workflows/validation.yml)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python%203.9-ffe900.svg?longCache=true&style=flat-square&colorB=00a1ff&logo=python&logoColor=88889e)](https://www.python.org/)

## About this project

This project includes a set of pre-made utility classes and functions which could prove to be very helpful when making
a pygame based game. It includes a `src.util.base_game.BaseGame` class, which is supposed to be subclassed into single
game classes each with it's own logic. This class provides an abstracted way to run the game simply by initializing
this class and running `game.start` or `game.run_continually`.

To make development very easy, everything in this template has a detailed docstring informing about what given
method/class is responsible for and how should it be used. To make things even easier, there is already a pre-made file
that contains an empty definition of a class which inherits from this BaseGame ready to be used.

We know that some developers really like strong typing and for that reason, we even made sure that the whole code-base
is completely type-hinted and meets pyright type-checker standards.
