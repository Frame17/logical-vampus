from world import *
from agent import Agent

# WORLD = generate_world()
WORLD = [
    [set(), set(), set(), set()],
    [set(["wind", "smell"]), set(["wind"]), set(), set()],
    [set(["pit", "vampus"]), set(["pit", "smell"]), set(), set()],
    [set(["gold", "shine"]), set(), set(), set()],
]

if __name__ == '__main__':
    agent = Agent(WORLD, WORLD[0][0])
    print_world(WORLD, {"x": 0, "y": 0})
    finished = False
    while not finished:
        x, y = agent.ask()
        print_world(WORLD, {"x": y, "y": x})    # TODO - temporary fix, reverted coordinates

        agent.tell(WORLD[x][y])
        finished = agent.finished()
        if finished:
            print('\x1b[6;30;42m' + 'What a big win!' + '\x1b[0m')
