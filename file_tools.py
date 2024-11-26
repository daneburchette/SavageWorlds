"""
File Tools Module
Dane Burchette
November 23, 2024
"""

from csv import DictReader


def make_dictionary(file: str):
    with open(file, newline="") as csvfile:
        reader = DictReader(csvfile)
        result = [x for x in reader]
    return result


if __name__ == "__main__":
    test = make_dictionary("./test_character.csv")
    for x in test:
        print(x)
