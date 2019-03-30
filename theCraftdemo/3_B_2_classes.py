#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime


class Golem:
    population = 0
    __life_span = 10

    def __init__(self, name=None):
        self.name = name
        self.build_year = datetime.date.today().year
        self.__active = True
        Golem.population += 1

    def cease(self):
        self.__active = False
        Golem.population -= 1

    def is_active(self):
        if datetime.date.today().year - self.build_year >= Golem.__life_span:
            self.cease()
        return self.__active

    def say_hi(self):
        print('Hi!')

    def say_hello(self):
        print('Hello!')


class Running_Golem(Golem):

    def run(self):
        print("Can't you see? I'm running...")

    def say_hello(self):
        print('Hey! Nice day, Huh?')


def test1():
    g = Golem('Clay')
    print(g.name)
    print(g.build_year)
    print(g.say_hi)
    g.say_hi()


def test2():
    print('\ntest2')

    rg = Running_Golem('Clay')
    print(rg.run)
    rg.run()
    print(rg.name)
    print(rg.build_year)
    rg.say_hi()
    rg.say_hello()


def test3():
    print('\ntest3')
    rg = Running_Golem('Clay')
    #help(rg)
    print(dir(rg))
    print(rg.__dict__)
    print(hasattr(rg, 'build_year'))


def test4():
    print('\ntest4')

    g = Golem()
    print(hasattr(Golem, 'population')) # True
    print(hasattr(g, 'population')) # True
    print(hasattr(Golem, '__life_span')) # False
    print(hasattr(g, '__life_span')) # False
    print(hasattr(g, '__active')) # False

    print('g.population =', g.population)
    setattr(Golem, 'population', 10)
    print('g.population =', g.population)

    x = Golem()
    print('g.population =', g.population)

    x.cease()
    print('g.population =', g.population)

    print(getattr(g, 'population'))
    print(g.is_active())



def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
