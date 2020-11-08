from world import *
from enum import Enum
import random


# Events
class Event(Enum):
    VAMPUS_KILLED = "vampus_killed"
    GOLD_FOUND = "gold_found"


class Agent:
    def init(self, world, start_senses):
        self.x = 0
        self.y = 0
        self.world = world
        self.knowledge = []
        self.tell(start_senses)

    def tell(self, senses):
        """
        Adding information about the world.
        Tracks state in the form
        :param senses: input in the form SENSES
        """

        for sense in senses:
            self.knowledge.append((sense, neighbours(self.x, self.y)))

    def ask(self):
        """
        Decides where to go from here
        :return: next step
        """
        next_steps = set()
        for x, y in neighbours(self.x, self.y):
            info = list(filter(lambda fact: (x, y) in fact[1], self.knowledge))
            if self.decide(info):
                next_steps.add((x, y))

        return random.choice(list(next_steps))

    @staticmethod
    def decide(infos):
        for info in infos:
            if info[0] == Sense.SHINE:
                return True

        return False

    def finished(self):
        return len(list(filter(lambda fact: fact[0] == Event.GOLD_FOUND, self.knowledge))) > 0