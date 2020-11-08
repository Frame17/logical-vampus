from world import *


class Agent:
    def __init__(self, world, start_senses):
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
        for x, y in neighbours(self.x, self.y):
            info = list(filter(lambda fact: (x, y) in fact[1], self.knowledge))
