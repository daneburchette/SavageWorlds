"""
Character Creator Module
Dane Burchette
November 27, 2024
"""

from pynput import keyboard
from character import Character


class Creator:

    def __init__(self):
        ...

    def get_name(self) -> None:
        self.stats["name"] = input("Enter Name:\t")


class TestUI:

    def __init__(self, stats: dict):
        self.traits = []
        for key, value in stats.items():
            setattr(self, key, value)
            self.traits.append(key)
        while True:
            self.interface()

    def interface(self) -> None:
        self.print_trait()
        self.active = self.active_trait()

    def print_trait(self) -> None:
        for trait in self.__dict__.keys():
            if self.__dict__[trait][0]:
                print(f"** {trait.title()}: {self.__dict__[trait][-1]}")
            else:
                print(f"   {trait.title()}: {self.__dict__[trait][-1]}")

    def active_trait(self) -> str:
        for trait in self.__dict__.keys():
            if self.__dict__[trait]:
                return trait
        self.__dict__[self.traits[0]][0] = True
        self.active_trait()


if __name__ == "__main__":
    stats = {
        "name": [False, ""],
        "age": [False, ""],
        "sex": [False, ""]
    }
    test = TestUI(stats)
