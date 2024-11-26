"""
Character Module
Dane Burchette
November 23, 2024
"""

from file_tools import make_dictionary
from character_traits import attributes


class Character:

    def __init__(self, stats=None):
        # Load stats from dictionary
        if stats is not None:
            stats = self.stat_parser(stats)
            for key, value in stats.items():
                setattr(self, key, value)
        else:
            self.stat_prompt()
        # Create derived stats
        self.derive_stats()
        # Load default for session
        self.bennies = []
        self.combat = False
        self.shaken = False
        self.wounds = 0
        self.fatigue = 0
        self.action_card = []
        self.holding = False

    def __str__(self):
        # Create Charcter Sheet
        att = self.__dict__.copy()
        results = [f"Name: {self.name}"]
        results += [f"{k.title()}:  \td{att[k][0]
                                        }" for k in attributes["base"]["traits"]]
        results += [f"{k.title()}:  \td{att[k][0]}" for k in attributes["base"]
                    ["skills"] if att[k][-1] != -2]
        return "\n".join(results)

    def stat_parser(self, stats) -> None:
        result = {"name": stats["name"]}
        result["wild_card"] = bool(stats["wild_card"])
        result["experience_points"] = int(stats["experience_points"])
        result["attribute_up"] = bool(stats["attribute_up"])
        for key in attributes["base"]["traits"]:
            result[key] = tuple([int(x.strip())
                                 for x in stats[key].split(',')])
        for key in attributes["base"]["skills"]:
            stats.setdefault(key, "4, -2")
            if stats[key] is None:
                stats[key] = "4, -2"
            result[key] = tuple([int(x.strip())
                                 for x in stats[key].split(",")])
        return result

    def derive_stats(self):
        self.charisma = 0
        self.pace = 6
        self.parry = 2 + (self.fighting[0] // 2) + self.fighting[1]
        self.toughness = 2 + (self.vigor[0] // 2) + (self.vigor[1] // 2)
        match (self.experience_points // 20):
            case 0:
                self.rank = "Novice"
            case 1:
                self.rank = "Seasoned"
            case 2:
                self.rank = "Veteran"
            case 3:
                self.rank = "Heroic"
            case _:
                self.rank = "Legendary"

    def stat_prompt(self) -> None:
        self.name = "Blank"
        self.wild_card = False
        self.experience_points = 0
        self.attirubte_up = False
        # Traits
        self.agility = (4, 0)
        self.smarts = (4, 0)
        self.spirit = (4, 0)
        self.strength = (4, 0)
        self.vigor = (4, 0)
        # Skills
        # Agility Skills
        self.boating = (4, -2)
        self.driving = (4, -2)
        self.fighting = (4, -2)
        self.lockpicking = (4, -2)
        self.piloting = (4, -2)
        self.riding = (4, -2)
        self.shooting = (4, -2)
        self.stealth = (4, -2)
        self.swimming = (4, -2)
        self.taunt = (4, -2)
        self.throwing = (4, -2)
        # Smarts Skills
        self.gambling = (4, -2)
        self.healing = (4, -2)
        self.investigation = (4, -2)
        self.smarts = (4, -2)
        self.notice = (4, -2)
        self.repair = (4, -2)
        self.streetwise = (4, -2)
        self.survival = (4, -2)
        self.tracking = (4, -2)
        # Spirit Skills
        self.intimidation = (4, -2)
        self.persuasion = (4, -2)
        # Strength Skills
        self.climbing = (4, -2)


if __name__ == "__main__":
    characters = make_dictionary("./test_character.csv")
    test = Character(characters[0])
    print(test)
