"""
Dice Rolling Module
Dane Burchette
November 22, 2024
"""

from random import randint


def roll(die: tuple) -> int:
    return (randint(1, die[0]) + die[-1])


def explode(die: tuple) -> int:
    result = roll((die[0], 0))
    if result == die[0]:
        result += explode((die[0], 0))
    return result + die[-1]


def wild(die: tuple) -> tuple(int):
    wild = explode((6, die[-1]))
    return explode(die), wild


if __name__ == "__main__":
    pass
