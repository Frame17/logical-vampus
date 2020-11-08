import random
from enum import Enum


# SENSES
class Sense(Enum):
    WIND = u"\33[31m☤"
    SMELL = u"\33[35m♨️"
    SHINE = u"\33[93m☼"
    SCREAM = u"\33[35m♪"


SENSES = [Sense.WIND, Sense.SMELL, Sense.SHINE, Sense.SCREAM]


# OBJECTS
class Object(Enum):
    GOLD = u"\33[93m♧"
    VAMPUS = u"\33[35m☃️"
    PIT = u"\33[31m☗"


OBJECTS = [Object.GOLD, Object.VAMPUS, Object.PIT]


world = [
    [set(), set(), set(), set()],
    [set(), set(), set(), set()],
    [set(), set(), set(), set()],
    [set(), set(), set(), set()]
]


def generate_world():
    x, y = generate_position()
    world[x][y].add(Object.VAMPUS)
    for x, y in neighbours(x, y):
        world[x][y].add(Sense.SMELL)

    # generate pit, can be under vampus
    for i in range(0, 2):
        x, y = generate_position()
        world[x][y].add(Object.PIT)
        for x, y in neighbours(x, y):
            world[x][y].add(Sense.WIND)

    # generate gold on empty position and not (0, 0)
    while len(world[x][y]) > 0 or (x == 0 and y == 0):
        x, y = generate_position()
    world[x][y].add(Object.GOLD)
    for x, y in neighbours(x, y):
        world[x][y].add(Sense.SHINE)

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

    print("-"*40)

    for i, row in enumerate(world):

        row_objects = []
        row_senses = []
        for j, cell in enumerate(row):

            icons = list()
            for object in OBJECTS:
                if object in cell:
                    icons.append(object.value)
                    icons.append("\033[0m")
            row_objects.append("|" + " ".join(icons) + " " * (
                        8 - len(icons) - len(icons) // 2) + "|")

            agent_s = ""
            if agent["x"] == j and agent["y"] == i:
                agent_s += "\33[32m♔ "

            icons = list()
            for sense in SENSES:
                if sense in cell:
                    icons.append(sense.value)
                    icons.append("\033[0m")
            row_senses.append("|" + agent_s + " ".join(icons) + " "*(8 - (2 if len(agent_s) else 0) - len(icons) - len(icons)//2) + "|")

        print("".join(row_objects))
        print("".join(row_senses))
        print("_" * 40)