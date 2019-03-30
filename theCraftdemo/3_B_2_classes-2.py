#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import datetime


class Golem:
    __population = 0
    __life_span = 10

    def __init__(self, name=None):
        self.name = name
        self.build_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1

    def cease(self):
        self.__active = False
        Golem.__population -= 1

    def is_active(self):
        if datetime.date.today().year - self.build_year >= Golem.__life_span:
            self.cease()
        return self.__active

    def say_hi(self):
        print('Hi!')

    @property
    def population(self):
        return Golem.__population

    @population.setter
    def population(self, value):
        Golem.__population = value


def test1():
    g = Golem('Clay')
    print(g.population)
    g.population = 100

    ga = Golem('New')
    print(g.population)
    print(ga.population)

    # help(Golem)
    print(Golem.__dict__)
    print(g.__dict__)

    print(hasattr(Golem, "population"))
    print(getattr(Golem, "population"))
    setattr(Golem, "population", 10000)
    print(g.population)


def main():
    test1()


if __name__ == "__main__":
    main()
