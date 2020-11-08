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
    finished = False
    while not finished:
        x, y = agent.ask()
        agent.tell(WORLD[x][y])
        finished = agent.finished()
