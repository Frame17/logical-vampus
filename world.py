import random

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