from world import *


class Agent:
    def __init__(self, world, start_senses):
        self.world = world
        self.knowledge = []
        self.knowledge.append(self.tell(start_senses, 0, 0))

    def tell(self, senses, x, y):
        """
        Adding information about the world.
        Tracks state in the form
        :param senses: input in the form SENSES
        """

        for sense in senses:
            self.knowledge.append((sense, neighbours(x, y)))
