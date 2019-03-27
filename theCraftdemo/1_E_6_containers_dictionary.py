#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def test1():
    print('\ntest1')

    aDict = {}
    bDict = {'a': 1, 'b': 2, 'c': 3}
    print(aDict)
    print(bDict)

    # 如果有重复元素，保留最后一个
    phonebook = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
    print(phonebook)

    # 更新
    phonebook['joe'] = 5802
    print(phonebook)

    # 添加
    phonebook['jian'] = 9999
    print(phonebook)

    # 删除
    del phonebook['ann']
    print(phonebook)

    # 更新 phonebook，把 phonebook2 中的元素更新到 phonebook
    phonebook2 = {'john': 9876, 'mike': 5603, 'stan': 6898, 'eric': 7898}
    phonebook.update(phonebook2)
    print(phonebook)


def test2():
    print('\ntest2')

    phonebook = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
    print(phonebook)
    print(phonebook.keys())
    print(phonebook.values())
    print(phonebook.items())

    print('ann' in phonebook)
    print('stan' in phonebook.keys())
    print(1225 in phonebook.values())
    print(('stan', 6898) in phonebook.items())


def test3():
    print('\ntest3')

    phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
    phonebook2 = {'john': 9876, 'mike': 5603, 'stan': 6898, 'eric': 7898}
    phonebook1.update(phonebook2)

    print(phonebook1)
    print(len(phonebook1))
    print(max(phonebook1))
    print(min(phonebook1))

    print(list(phonebook1))
    print(tuple(phonebook1))
    print(set(phonebook1))

    print(sorted(phonebook1))
    print(sorted(phonebook1, reverse=True))


def test4():
    print('\ntest4')

    phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225, 'ann': 6585}
    phonebook2 = {'john': 9876, 'mike': 5603, 'stan': 6898, 'eric': 7898}

    # 深拷贝
    phonebook3 = phonebook2.copy()
    print(phonebook3)

    phonebook3.clear()
    print(phonebook3)
    print(phonebook2)

    p = phonebook1.popitem()
    print('p =', p)
    print('phonebook1 =', phonebook1)

    p = phonebook1.pop('adam', 3538)
    print('p =', p)
    print('phonebook1 =', phonebook1)

    p = phonebook1.get('adam', 3538)
    print('p =', p)
    print('phonebook1 =', phonebook1)

    p = phonebook1.setdefault('adam', 3538)
    print('p =', p)
    print('phonebook1 =', phonebook1)


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
