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
                vampus_info = list(filter(lambda fact: SMELL == fact[0], self.knowledge))
                neighbours_unsafe = set([x for x in neighbours(self.x, self.y) if
                                         x not in list(filter(lambda fact: SAFE == fact[0], self.knowledge))[0][1]])
                # second time we hear smell
                if sense == SMELL and vampus_info != [] and list(
                        filter(lambda fact: VAMPUS == fact[0], self.knowledge)) == []:
                    possible_vampus = vampus_info[0][1].intersection(neighbours_unsafe)
                    if len(possible_vampus) == 1:
                        for fact in self.knowledge:
                            if fact[0] == SMELL:
                                self.knowledge.remove(fact)
                        self.knowledge.append((VAMPUS, possible_vampus))

                pit_infos = list(filter(lambda fact: WIND == fact[0], self.knowledge))
                for pit_info in pit_infos:
                    possible_pit = pit_info[1].intersection(neighbours_unsafe)
                    if possible_pit:
                        self.knowledge.remove(pit_info)
                        self.knowledge.append((PIT, possible_pit))
                else:
                    # neighbours - safe
                    self.knowledge.append((sense, neighbours_unsafe))

            # edit previously known information
            if not self.is_dead():
                for fact in self.knowledge:
                    if fact[0] != SAFE and (self.x, self.y) in fact[1]:
                        fact[1].remove((self.x, self.y))
                    elif fact[0] == SAFE:
                        fact[1].add((self.x, self.y))

        # fact-checking
        neighbours_unsafe = set([x for x in neighbours(self.x, self.y) if
                                 x not in list(filter(lambda fact: SAFE == fact[0], self.knowledge))[0][1]])
        for fact in self.knowledge:
            if fact[0] != SAFE:
                for neighbour in neighbours_unsafe:
                    if neighbour in fact[1] and len(fact[1]) > 1 and fact[0] not in senses:
                        fact[1].remove(neighbour)

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
