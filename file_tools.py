"""
File Tools Module
Dane Burchette
November 23, 2024
"""

from csv import DictReader, DictWriter


def make_dictionary(file: str):
    with open(file, newline="") as csvfile:
        reader = DictReader(csvfile)
        result = [x for x in reader]
    return result


def write_dictionary(file: str, dicts: list) -> None:
    fieldnames = [key for key in dicts[0].keys()]
    with open(file, "w", newline="") as csvfile:
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dicts)


if __name__ == "__main__":
    test = make_dictionary("./test/test_character.csv")
    for x in test:
        print(x)
    write_dictionary("./test/test_character2.csv", test)
