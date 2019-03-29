#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Order of Arguments:
#
#   Positional
#   Arbitrary Positional
#   Keyword
#   Arbitrary Keyword


def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')
    print()


def test1():
    say_hi()
    say_hi('ann')
    say_hi('mike', 'john', 'zeo')

    names = ('mike', 'john', 'zeo')
    say_hi(*names)

    a_string = 'Python'
    say_hi(*a_string)

    a_range = range(10)
    say_hi(*a_range)

    a_list = list(range(10, 0, -1))
    say_hi(*a_list)

    a_dictionary = {'ann': 2321, 'mike': 8712, 'joe': 7610}
    say_hi(*a_dictionary)


def say_hi_2(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')
    print()


def test2():
    say_hi_2('Hello', 'mike', 'john', 'zeo')
    say_hi_2('Hello', 'mike', 'john', 'zeo', capitalized=True)


def say_hi_3(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}')
    print()


def test3():
    say_hi_3(mike='Hello', ann='Oh, my darling', john='Hi')

    a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
    say_hi_3(**a_dictionary)

    say_hi_3(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
