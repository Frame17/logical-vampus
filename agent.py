from world import *
import random


class Agent:
    def __init__(self, world, start_senses):
        self.x = 0
        self.y = 0
        self.world = world
        safe_set = set()
        safe_set.add((0, 0))
        self.knowledge = [(SAFE, safe_set)]
        self.tell(start_senses)

    def tell(self, senses):
        """
        Adding information about the world.
        Tracks state in the form
        :param senses: input in the form SENSES
        """

        if (self.x, self.y) not in list(filter(lambda fact: SAFE == fact[0], self.knowledge))[0][1]:  # ignore revisited
            # add new information
            for sense in senses:
                # neighbours - safe
                self.knowledge.append(
                    (sense,
                     set([x for x in neighbours(self.x, self.y) if
                          x not in list(filter(lambda fact: SAFE == fact[0], self.knowledge))[0][1]]))
                )

            # edit previously known information
            if not self.is_dead():
                for fact in self.knowledge:
                    if fact[0] != SAFE and (self.x, self.y) in fact[1]:
                        fact[1].remove((self.x, self.y))
                    elif fact[0] == SAFE:
                        fact[1].add((self.x, self.y))

    def ask(self):
        """
        Decides where to go from here
        :return: next step
        """
        self.x, self.y = self.decide(neighbours(self.x, self.y))
        return self.x, self.y

    def decide(self, neighbours):
        # remove possibly dangerous cases
        candidates = list(
            filter(lambda arg: len(
                list(filter(lambda fact: SAFE != fact[0] and (arg[0], arg[1]) in fact[1], self.knowledge))) == 0,
                   neighbours))

        if candidates:
            return random.choice(candidates)
        return random.choice(neighbours)

    def won(self):
        return SHINE in self.world[self.x][self.y]

    def is_dead(self):
        return VAMPUS in self.world[self.x][self.y] or PIT in self.world[self.x][self.y]
