from world import *
from agent import Agent

WORLD = generate_world()

if __name__ == '__main__':
    agent = Agent(WORLD, WORLD[0][0])
    print_world(WORLD, (0, 0))
    finished = False
    while not finished:
        x, y = agent.ask()
        print_world(WORLD, (x, y))

        if agent.is_lost():
            print('\x1b[6;33;46m' + 'Boi seems to lost in 3 trees!' + '\x1b[0m')
            break

        agent.tell(WORLD[x][y])
        if agent.won():
            print('\x1b[6;30;42m' + 'What a big win!' + '\x1b[0m')

        if agent.is_dead():
            print('\x1b[6;30;41m' + 'What a noob, you lost, get back to the school!' + '\x1b[0m')

        finished = agent.won() or agent.is_dead()
