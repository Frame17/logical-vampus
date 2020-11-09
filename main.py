from world import *
from agent import Agent

# WORLD = generate_world()
WORLD = [
    [set(["shine"]), set(), set(), set()],
    [set(["gold"]), set(["shine"]), set(), set()],
    [set(["wind", "shine", "smell"]), set(["wind"]), set(), set()],
    [set(["pit", "vampus"]), set(["pit"]), set(), set()]
]

if __name__ == '__main__':
    agent = Agent(WORLD, WORLD[0][0])
    print_world(WORLD, {"x": 0, "y": 0})
    finished = False
    while not finished:
        x, y = agent.ask()
        agent.tell(WORLD[x][y])
        print_world(WORLD, {"x": x, "y": y})
        finished = agent.finished()
        if finished:
            print('\x1b[6;30;42m' + 'What a big win!' + '\x1b[0m')
