import random
from enum import Enum

# SENSES
WIND = "wind"
SMELL = "smell"
SHINE = "shine"
SCREAM = "scream"
SENSES = [WIND, SMELL, SHINE, SCREAM]

# OBJECTS
GOLD = "gold"
VAMPUS = "vampus"
PIT = "pit"

OBJECTS = [GOLD, VAMPUS, PIT]

view = {
    WIND: u"\33[31m☤",
    SMELL: u"\33[35m♨️",
    SHINE: u"\33[93m☼",
    SCREAM: u"\33[35m♪",

    GOLD: u"\33[93m♧",
    VAMPUS: u"\33[35m☃️",
    PIT: u"\33[31m☗"
}

world = [
    [set(), set(), set(), set()],
    [set(), set(), set(), set()],
    [set(), set(), set(), set()],
    [set(), set(), set(), set()]
]


def generate_world():
    x, y = generate_position()
    world[x][y].add(VAMPUS)
    for x, y in neighbours(x, y):
        world[x][y].add(SMELL)

    # generate pit, can be under vampus
    for i in range(0, 2):
        x, y = generate_position()
        world[x][y].add(PIT)
        for x, y in neighbours(x, y):
            world[x][y].add(WIND)

    # generate gold on empty position and not (0, 0)
    while len(world[x][y]) > 0 or (x == 0 and y == 0):
        x, y = generate_position()
    world[x][y].add(GOLD)
    for x, y in neighbours(x, y):
        world[x][y].add(SHINE)

    return world


def neighbours(x, y):
    neighb = []

    if x > 0:
        neighb.append((x - 1, y))
    if x < 3:
        neighb.append((x + 1, y))
    if y > 0:
        neighb.append((x, y - 1))
    if y < 3:
        neighb.append((x, y + 1))

    return neighb


def generate_position():
    x = y = 0
    while x == 0 and y == 0:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    return x, y


def print_world(world, agent):
    print("-" * 40)

    for i, row in enumerate(world):

        row_objects = []
        row_senses = []
        for j, cell in enumerate(row):

            agent_s = ""
            if agent["x"] == j and agent["y"] == i:
                agent_s += "\33[32m♔\033[0m "

            icons = list()
            for object in OBJECTS:
                if object in cell:
                    icons.append(view[object])
                    icons.append("\033[0m")
            row_objects.append("|" + agent_s + " ".join(icons) +
                               " " * (8 - (2 if len(agent_s) else 0) - len(icons) - len(icons) // 2) + "|")

            icons = list()
            for sense in SENSES:
                if sense in cell:
                    icons.append(view[sense])
                    icons.append("\033[0m")
            row_senses.append("|" + " ".join(icons) + " " * (
                    8 - len(icons) - len(icons) // 2) + "|")

        print("".join(row_objects))
        print("".join(row_senses))
        print("_" * 40)
