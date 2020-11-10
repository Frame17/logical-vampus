from world import *
from agent import Agent

WORLD = generate_world()
# WORLD = [
#     [set(), set(), set(), set()],
#     [{"wind", "smell"}, set(["wind"]), set(), set()],
#     [set(["pit", "vampus"]), set(["pit", "smell"]), set(), set()],
#     [set(["gold", "shine"]), set(), set(), set()],
# ]

# WORLD = [
#     [set(), set(["wind"]), set(), set(["gold", "shine"])],
#     [set(["wind"]), set(["pit"]), set(["wind"]), set()],
#     [set(), set(["wind"]), set(), set()],
#     [set(), set(), set(), set()],
# ]

if __name__ == '__main__':
    agent = Agent(WORLD, WORLD[0][0])
    print_world(WORLD, {"x": 0, "y": 0})
    finished = False
    while not finished:
        x, y = agent.ask()
        print_world(WORLD, {"x": y, "y": x})    # TODO - temporary fix, reverted coordinates

        agent.tell(WORLD[x][y])
        if agent.won():
            print('\x1b[6;30;42m' + 'What a big win!' + '\x1b[0m')

        if agent.is_dead():
            print('\x1b[6;30;41m' + 'What a noob, you lost, get back to the school!' + '\x1b[0m')

        finished = agent.won() or agent.is_dead()
